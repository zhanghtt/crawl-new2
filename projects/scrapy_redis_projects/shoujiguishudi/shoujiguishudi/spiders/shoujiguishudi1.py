#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import urllib
from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
from scrapy_redis.utils import bytes_to_str
from multiprocess.core.spider import Seed



class ShoujiSpider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'shoujiguishudi'
    pro_city_pattern = re.compile(r'<dd><span>号码归属地：</span>(.*?) (.*?)</dd>')
    telcompany_pattern = re.compile(r'<dd><span>手机卡类型：</span>(.*?)</dd>')

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            phonenumber = seed.value.strip()
            url = "http://shouji.xpcha.com/{0}.html".format(phonenumber)
            return Request(url=url, meta={"_seed": str_seed, "headers": {"Referer": "https://www.baidu.com/"}}, priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse(self, response):
        if response._status == 0 and response.text:
            pro_city = self.pro_city_pattern.findall(response.text)
            tel_compay = self.telcompany_pattern.findall(response.text)
            yield {"phonenumber": response.meta["_seed"], "province": pro_city[0][0],
                   "city": pro_city[0][0] if pro_city[0][1] == "" else pro_city[0][1],
                   "company": tel_compay[0]}
        else:
            yield {}

