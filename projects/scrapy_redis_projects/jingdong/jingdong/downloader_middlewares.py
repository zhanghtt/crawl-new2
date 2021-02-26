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
        #request.headers['user-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
        #request.headers['Connection'] = "keep-alive"
        #Proxifierrequest.headers["cookie"] = "shshshfpa=230b299e-b267-3f39-748a-5274ba04573e-1526388430; shshshfpb=0e4a63e00c3146f1205679ecef0af468fb452b7038a3edfd15afad6d12; __jdu=1595213903005116662704; pin=jd_49e6f74229a5c; unick=jd_188014ctk; _tp=f8skMf7S6k8VPMVjjhCn8S7vk6UqsuFMW8o68xx3ddc%3D; _pst=jd_49e6f74229a5c; ipLocation=%u5317%u4eac; pinId=CL2LG1jQi0fBGlwodztkXrV9-x-f3wj7; unpl=V2_ZzNtbRAFShd8AUZWfk0IB2JTRwgSBxBBfAtGUHseXFFkCxINclRCFnQURldnG1wUZwQZWUNcRhJFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRpdS1BKFnQLRlZLKV8FVwMTbUJTSxF2CERcehtdBGMDElpFUEATdA12ZHwpbDVjCxVUQVdzFEUJdhYvRVsNbwAaWw9XRx1xC0ZWcxheBGYHEl1FUEQWcwlDZHopXw%3d%3d; __jdv=76161171|direct|-|none|-|1609750532540; TrackID=14z86bRECmD_c8hnyUzWqPbiv0pHgxgGJ0tgMH9b8UmBPkuTndrN5VhNCH5t8h3LTmlYuJbzhHXbftdRKDtXKBnPgOEXXzqhXAH9ZY-6s5MAR2ncnCvnEbToPqbFrYgEt; user-key=43a6e8ea-993d-49e9-8763-4e756d81ae6f; cn=0; PCSYCityID=CN_110000_110100_110105; areaId=1; ipLoc-djd=1-72-55653-0; wxa_level=1; jxsid=16109508048628837173; webp=1; visitkey=31014972499970792; __jda=122270672.1595213903005116662704.1595213903.1610948455.1610955353.123; __jdc=122270672; 3AB9D23F7A4B3C9B=HV7XTTHFGASMIJRSRKK34KLHMYELLS47K4NBCIR2PEFYCZUMIX225JHQCMEJUTEKYFDA47E3QEMFC3TYKKQRYXFS2Q; shshshfp=8e6807b1ccf37dd2a527f63ee133d3e6; shshshsID=48908f8b4d08dd6a4ad6ea045c548f30_2_1610955836722; wq_logid=1610955927.1063071573; retina=1; cid=9; wqmnx1=MDEyNjM4NHMubXQxMzQyL25yOzVNQUszTEdoLjFsaTFzZjQyRUgmUg%3D%3D; __jdb=122270672.12.1595213903005116662704|123.1610955353; mba_muid=1595213903005116662704; mba_sid=16109559266537842608963232693.1"
        if request.meta.get("headers"):
            for k in request.meta.get("headers"):
                request.headers[k] = request.meta.get("headers")[k]
        if self.http_proxies_enabled:
            if request.meta.get("need_switch_proxy"):
                old = self.current_proxy
                self.current_proxy = self.get_new_proxy()
                print("switch new proxy from {} to {}".format(old, self.current_proxy))
            print(self.current_proxy)
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
            #time.sleep(19*60)
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
            ret = self._retry(request, exception, spider)
            if ret:
                return ret
            else:
                # 重试次数达到状态
                response = HtmlResponse(url='', request=request)
                response._status = 1
                if isinstance(exception, Exception):
                    reason = global_object_name(exception.__class__)
                self.logger.debug("max retries had reached because of {}!".format(reason))
                return response
            #return self._retry(request, exception, spider)

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


class DydmicDelayMiddleware:

    def __init__(self, delay_time=0, enabled=False):
        self.delay_time = delay_time
        self.enabled = enabled

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings.getfloat('DYDMIC_DELAY_DEFAULT'), crawler.settings.getbool('DYDMIC_DELAY_ENABLED'))
        return o

    def process_request(self, request, spider):
        if self.enabled:
            if request.meta.get("dydmc_delay"):
                time.sleep(request.meta.get("dydmc_delay"))
            elif self.delay_time:
                time.sleep(self.delay_time)
