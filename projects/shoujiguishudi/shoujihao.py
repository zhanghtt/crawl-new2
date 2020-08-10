#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiprocess.core.spider import SpiderManger, Seed
from multiprocess.core import HttpProxy
from multiprocess.tools import process_manger
from multiprocess.tools import stringUtils
import re
import sys
from fake_useragent import UserAgent
import random
import requests


class NewPhone2(SpiderManger):
    def __init__(self, seeds_file, **kwargs):
        super(NewPhone2, self).__init__(**kwargs)
        self.proxies = HttpProxy.getHttpProxy()
        self.ua = UserAgent()
        self.phone_regx = re.compile(r'^\d{11,11}$')
        self.phone_number_checker = stringUtils.check_legality(pattern=r'^\d{11,11}$')
        for seed in open(seeds_file):
            seed = seed.strip("\n")
            if(self.phone_number_checker(seed)):
                self.seeds_queue.put(Seed(seed, kwargs["retries"]))
            else:
                self.log.info("legal_format: " + seed)
        self.pro_city_pattern = re.compile(r'<dd><span>号码归属地：</span>(.*?) (.*?)</dd>')
        self.telcompany_pattern = re.compile(r'<dd><span>手机卡类型：</span>(.*?)</dd>')

    def make_request(self, seed):
        url = "http://shouji.xpcha.com/{0}.html".format(seed.value)
        request = {"url": url,
                   "timeout": 10,
                   "method": "get",
                   "proxies": {"http": random.choice(self.proxies)},
                   "headers": {"Connection": "keep-alive", "User-Agent": self.ua.chrome}}
        return request

    def parse_item(self, content, seed):
            pro_city = self.pro_city_pattern.findall(content)
            tel_compay = self.telcompany_pattern.findall(content)
            result = {"_id": seed.value, "phonenumber": seed.value, "province": pro_city[0][0], "city": (
                pro_city[0][0] if pro_city[0][1] == "" else pro_city[0][1]), "company": tel_compay[0]}
            self.write([result])
            seed.ok()
    # def process(self, seed):
    #     url = "http://shouji.xpcha.com/{0}.html".format(seed.value)
    #     request = {"url": url,
    #                "timeout": 10,
    #                "method":"get",
    #                "proxies": {"http": random.choice(self.proxies)},
    #                "headers": {"Connection": "keep-alive", "User-Agent": self.ua.chrome}}
    #     respone = self.do_request(request)
    #     if respone and respone.status_code == requests.codes.ok:
    #         if respone.text:
    #             pro_city = self.pro_city_pattern.findall(respone.text)
    #             tel_compay = self.telcompany_pattern.findall(respone.text)
    #             result = {"_id": seed.value, "phonenumber": seed.value, "province": pro_city[0][0], "city": (
    #                 pro_city[0][0] if pro_city[0][1] == "" else pro_city[0][1]), "company": tel_compay[0]}
    #             self.write([result])
    #             seed.ok()


if __name__ == "__main__":
    process_manger.kill_old_process(sys.argv[0])
    import logging
    config = {"job_name": "shoujiguishudi"
        , "spider_num": 1
        , "retries": 3
        , "complete_timeout": 1 * 60
        , "seeds_file": "resource/buyer_phone.3"
        , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "jicheng", "collection": "shoujiguishudi"}
        , "log_config": {"level": logging.INFO, "filename": sys.argv[0] + '.logging', "filemode": 'a',
                         "format": '%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
        , "proxies_pool": HttpProxy.getHttpProxy()
        }
    p = NewPhone2(**config)
    p.main_loop(show_process=True)
