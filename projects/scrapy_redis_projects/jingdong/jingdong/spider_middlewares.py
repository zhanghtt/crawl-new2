# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import logging
# -*- coding: utf-8 -*-
import random
import pickle
from fake_useragent import UserAgent
from scrapy.item import Item
from multiprocess.core.spider import Seed
from scrapy.http import Response
from multiprocess.scrapy_redis.spiders import Request

class ExceptionCheckSpider(object):

    def __init__(self, settings):
        self.retry_http_codes = set(int(x) for x in settings.getlist('RETRY_HTTP_CODES'))

    #捕捉parse代码异常
    def process_spider_exception(self, response, exception, spider):
        self.logger.exception(exception)
        yield {"_seed": response.request.serialize(), "_status": 3}

    def process_spider_input(self, response, spider):
        if response._status == 0 :
            return None
        elif response._status == 1:
            raise Exception("retry times reached!")
        else:
            raise Exception("task failed! request.status is {} request._status is {}".format(response.status, response._status))

    def process_spider_output(self, response, result, spider):
        sucess = False
        for r in result:
            sucess = True
            if isinstance(r, (dict, Item)):
                r.update({"_status": response._status})
            yield r

        if not sucess and response.status == 200 and not response.text:
            request = response.request.copy()
            request.dont_filter = True
            if not hasattr(request, "_text_retry"):
                response.request._text_retry = 0
            if response.request._text_retry > 100:
                yield {"_seed": response.request.serialize(), "_status": 3}
            else:
                response.request._text_retry = response.request._text_retry + 1
                yield request
    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        return logging.LoggerAdapter(logger, {'spidermiddleware': self})

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
