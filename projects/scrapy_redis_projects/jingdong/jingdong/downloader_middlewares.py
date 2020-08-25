# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
from multiprocess.core.HttpProxy import getHttpProxy, getHttpsProxy
http_proxies, https_proxies = getHttpProxy(), getHttpsProxy()
from scrapy_redis.connection import get_redis_from_settings


class CustomHeadersDownLoadMiddleware(object):

    def __init__(self, crawler):
        self.crawler = crawler
        self.setting = crawler.settings
        self.spider = crawler.spider
        self.spider_name = self.spider.name
        self.http_proxies_queue_redis_key = self.setting.get("HTTP_PROXIES_QUEUE_REDIS_KEY",
                                                             "%(name)s:http_proxies_queue") % {"name": self.spider_name}
        self.http_proxies_enabled = self.setting.getbool("HTTP_PROXIES_ENABELD", True)
        self.logger.info(self.http_proxies_queue_redis_key)
        self.user_agent = UserAgent()
        self.redis = get_redis_from_settings(self.setting)
        self.current_proxy = self.get_new_proxy()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def get_new_proxy(self):
        if not hasattr(self, "current_proxy"):
            str_proxy = self.redis.lpop(self.http_proxies_queue_redis_key).decode("utf-8")
            if str_proxy == str(None):
                return None
            else:
                return str_proxy
        self.redis.rpush(self.http_proxies_queue_redis_key, str(self.current_proxy))
        str_proxy = self.redis.lpop(self.http_proxies_queue_redis_key).decode("utf-8")
        if str_proxy == str(None):
            return None
        else:
            return str_proxy

    def process_request(self, request, spider):
        request.headers['user-agent'] = self.user_agent.chrome
        request.headers['Connection'] = "keep-alive"
        if request.meta.get("headers"):
            for k in request.meta.get("headers"):
                request.headers[k] = request.meta.get("headers")[k]
        if self.http_proxies_enabled:
            if request.meta.get("need_switch_proxy"):
                old = self.current_proxy
                self.current_proxy = self.get_new_proxy()
                print("switch new proxy from {} to {}".format(old, self.current_proxy))
            request.meta['proxy'] = self.current_proxy

    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        return logging.LoggerAdapter(logger, {'middleware': self})


from scrapy.http import HtmlResponse


class ProcessAllExceptionMiddleware(object):
    def process_exception(self, request, exception, spider):
        response = HtmlResponse(url='', request=request)
        response._status = 2
        self.logger.debug('not contained exception: %s' % exception)
        return response

    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        return logging.LoggerAdapter(logger, {'middleware': self})


import logging

from twisted.internet import defer
from twisted.internet.error import (
    ConnectError,
    ConnectionDone,
    ConnectionLost,
    ConnectionRefusedError,
    DNSLookupError,
    TCPTimedOutError,
    TimeoutError,
)
from twisted.web.client import ResponseFailed

from scrapy.exceptions import NotConfigured
from scrapy.utils.response import response_status_message
from scrapy.core.downloader.handlers.http11 import TunnelError
from scrapy.utils.python import global_object_name


class RetryMiddleware(object):

    # IOError is raised by the HttpCompression middleware when trying to
    # decompress an empty response
    EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
                           ConnectionRefusedError, ConnectionDone, ConnectError,
                           ConnectionLost, TCPTimedOutError, ResponseFailed,
                           IOError, TunnelError)

    def __init__(self, crawler):
        settings = crawler.settings
        if not settings.getbool('RETRY_ENABLED'):
            raise NotConfigured
        self.max_retry_times = settings.getint('RETRY_TIMES')
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))
        self.priority_adjust = settings.getint('RETRY_PRIORITY_ADJUST')
        self.need_switch_proxy = settings.getbool('NEED_SWICH_PROXY')

    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        return logging.LoggerAdapter(logger, {'middleware': self})

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            response._status = 0
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            ret = self._retry(request, reason, spider)
            if ret:
                return ret
            else:
                #重试次数达到状态
                response._status = 1
                return response
        elif response.status == 200 and not response.text:
            self.logger.info("because: response.text is {}".format(response.text))
            reason = response_status_message(response.status)
            ret = self._retry(request, reason, spider)
            if ret:
                return ret
            else:
                # 重试次数达到状态
                response._status = 1
                return response
        response._status = 0
        return response

    # def process_response(self, request, response, spider):
    #     if request.meta.get('dont_retry', False):
    #         return response
    #     if response.status in self.retry_http_codes:
    #         reason = response_status_message(response.status)
    #         return self._retry(request, reason, spider) or response
    #     return response

    def process_exception(self, request, exception, spider):
        if (
            isinstance(exception, self.EXCEPTIONS_TO_RETRY)
            and not request.meta.get('dont_retry', False)
        ):
            if isinstance(exception, (TunnelError, defer.TimeoutError, TimeoutError)):
                if self.need_switch_proxy:
                    request.meta["need_switch_proxy"] = True
            return self._retry(request, exception, spider)

    def _retry(self, request, reason, spider):
        retries = request.meta.get('retry_times', 0) + 1

        retry_times = self.max_retry_times

        if 'max_retry_times' in request.meta:
            retry_times = request.meta['max_retry_times']

        stats = spider.crawler.stats
        if retries <= retry_times:
            self.logger.debug("Retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})
            retryreq = request.copy()
            retryreq.meta['retry_times'] = retries
            retryreq.dont_filter = True
            retryreq.priority = request.priority + self.priority_adjust

            if isinstance(reason, Exception):
                reason = global_object_name(reason.__class__)

            stats.inc_value('retry/count')
            stats.inc_value('retry/reason_count/%s' % reason)
            return retryreq
        else:
            stats.inc_value('retry/max_reached')
            self.logger.error("Gave up retrying %(request)s (failed %(retries)d times): %(reason)s",
                         {'request': request, 'retries': retries, 'reason': reason},
                         extra={'spider': spider})


import random
from scrapy import signals
import time


class RandomDelayMiddleware:

    def __init__(self, random_time=0):
        self._random_time = random_time

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings.getfloat('RANDOM_DELAY'))
        return o

    def process_request(self, request, spider):
        if self._random_time:
            time.sleep(random.randint(0, self._random_time*100000)/100000.0)