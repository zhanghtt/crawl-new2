#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import urllib
from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
from scrapy_redis.utils import bytes_to_str
from multiprocess.core.spider import Seed
from multiprocess.tools.collections import city2prov


class ShoujiSpider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'shoujiguishudi'
    pattern = re.compile(r'<div class="locate_text">[\s]*?<div class="upper_text">(.*?) (.*?)</div>[\s]*?<div class="upper_text">手机号码: (\d.*?)</div>[\s]*?</div>')
    pro_city_pattern = re.compile(r'<dd><span>号码归属地：</span>(.*?) (.*?)</dd>')
    telcompany_pattern = re.compile(r'<dd><span>手机卡类型：</span>(.*?)</dd>')

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            phonenumber = seed.value.strip()
            url = "http://shouji.xpcha.com/{0}.html".format(phonenumber)
            return Request(url=url, meta={"_seed": str_seed}, priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse1(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        phonenumber = seed.value
        res = self.pattern.findall(response.text)
        if res:
            city, company, phonenumber = res[0]
            yield {"phonenumber": phonenumber, "province": city2prov(city),
                   "city": city,
                   "company": company}
        else:
            yield {"phonenumber": phonenumber, "province": "未发现",
                   "city": "未发现",
                   "company": "未发现"}

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        phonenumber = seed.value
        pro_city = self.pro_city_pattern.findall(response.text)
        tel_compay = self.telcompany_pattern.findall(response.text)
        if pro_city:
            if pro_city[0][0] != "未知":
                yield {"phonenumber": phonenumber, "province": pro_city[0][0],
                       "city": pro_city[0][0] if pro_city[0][1] == "" else pro_city[0][1],
                       "company": tel_compay[0]}
            else:
                #失败写出
                yield Request(url="https://haoma.baidu.com/phoneSearch?search={0}".format(phonenumber),
                              meta={"_seed": response.meta["_seed"], "headers": {"Referer": "https://www.baidu.com/"}},
                              priority=1, callback=self.parse1)
        else:
            yield Request(url="https://haoma.baidu.com/phoneSearch?search={0}".format(phonenumber),
                          meta={"_seed": response.meta["_seed"], "headers": {"Referer": "https://www.baidu.com/"}},
                          priority=1, callback=self.parse1)


