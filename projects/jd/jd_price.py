#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiprocess.core.spider import SpiderManger, Seed
from multiprocess.tools import process_manger
import re
import sys
import random
from multiprocess.tools import timeUtil
from fake_useragent import UserAgent
import json


class JDPrice(SpiderManger):
    def __init__(self, seeds_file, **kwargs):
        super(JDPrice, self).__init__(**kwargs)
        self.ua = UserAgent()
        with open(seeds_file) as infile:
            for i, seed in enumerate(infile):
                current = seed.strip('\n').split("\t")[0]
                if i % 60 == 0:
                    if i != 0:
                        self.seeds_queue.put(Seed(strr, kwargs["retries"]))
                    strr = current
                else:
                    strr = strr + '%2CJ_' + current
        if strr:
            self.seeds_queue.put(Seed(strr, kwargs["retries"]))

        self.block_pattern = re.compile(r'{.*?}')
        self.innerid_pattern = re.compile(r'\d+')
        self.innerprice_pattern = re.compile(r'"\d+.\d+"')
        self.op_pattern = re.compile(r'"op":"(\d+.\d+)"')
        self.p_pattern = re.compile(r'"(\d+.\d+)"')
        self. p2_pattern = re.compile(r'"(-\d+.\d+)"')
        self.p1 = re.compile(r'"id":.*?"}')
        self.id_pattern = re.compile(r'id:"J_(\d+)"')
        self.first_pattern = re.compile(r'([a-zA-Z]*)":')
        self.rid = random.randint(100000000, 999999999)
        self.usrid = str(self.rid)
        self.up_pattern = re.compile('"up":"tpp"')

    def make_request(self, seed):
        price_address = "http://p.3.cn/prices/mgets?&type=1&skuIds=J_" + seed.value + '&pduid=' + self.usrid
        request = {"url": price_address,
                   "timeout": self.kwargs.get("request_timeout", 10),
                   "method":"get",
                   "sleep_time": 0.5,
                   "proxies": None,
                   "headers": {"Connection":"keep-alive", "User-Agent": self.ua.chrome}}
        return request

    def parse_item(self, content, seed):
        items = json.loads(content)
        if items:
            for item in items:
                if item.get("id"):
                    item["id"] = item["id"][2:]
            self.write(items)
        else:
            self.write([{"_seed": seed.value}])
        seed.ok()

    def parse_item1(self, content, seed):
        items = json.loads(content)
        print(items)
        blocks = self.block_pattern.findall(content)
        result = []
        for i in blocks:
            print(i)
            #p1s = self.p1.findall(i)
            p1s = [i]
            print(p1s[0])
            if len(p1s) > 0:
                lines = re.split(',', p1s[0])
                if len(lines) >= 2:
                    print(lines)
                    id1 = self.id_pattern.findall(lines[0])[0]
                    info = id1
                    for j in lines:
                        up = self.up_pattern.findall(j)
                        if up != []:
                            sale = [-1]
                        else:
                            sale = self.p2_pattern.findall(j)

                            if sale == []:
                                sale = self.p_pattern.findall(j)
                        info = str(info) + '\t' + str(sale[0])
                    info = info.lstrip("\t")
                    result.append({"values": info})
        print(result)
        if result:
            self.write(result)
        else:
            self.write([{"_seed": seed.value}])
        print(result)
        seed.ok()


if __name__ == "__main__":
    current_date = timeUtil.current_time()
    process_manger.kill_old_process(sys.argv[0])
    import logging
    from multiprocess.core import HttpProxy
    config = {"job_name": "jdprice"
              , "spider_num": 40
              , "retries": 3
              , "request_timeout": 10
              , "complete_timeout": 5*60
              , "sleep_interval": 0.5
              , "rest_time": 5
              , "write_seed" : False
              , "seeds_file": "resource/month202007"
              , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "jicheng", "collection": "jdprice"+current_date}
              , "log_config": {"level": logging.INFO,  "format":'%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
              ,"proxies_pool": HttpProxy.getHttpProxy()}
    p = JDPrice(**config)
    p.main_loop(show_process=True)
