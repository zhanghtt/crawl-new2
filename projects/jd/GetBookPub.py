#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import sys

from multiprocess.core.spider import SpiderManger, Seed
from multiprocess.tools import process_manger
from multiprocess.tools import timeUtil, collections
import random
from fake_useragent import UserAgent


class GetBrands(SpiderManger):
    def __init__(self, seeds_file, **kwargs):
        super(GetBrands, self).__init__(**kwargs)
        self.ua = UserAgent()
        with open(seeds_file) as infile:
            data_set = collections.DataSet(infile)
            for i, seed in enumerate(data_set.map(lambda line: line.strip('\n').split("\t")[0].replace('-', ','))
                                             .shuffle(1024)):
                self.seeds_queue.put(Seed(seed, kwargs["retries"]))
        self.pattern = re.compile(r'<li id="brand-(\d+)[\s\S]*?品牌::([\s\S]*?)\'\)"')

    def make_request(self, seed):
        cats = re.split(',', seed.value)
        format_value = (seed.value, 2, "pub") if cats[0] == '1713' else (seed.value, 1, "brand")
        url = 'http://list.jd.com/list.html?cat={0}&trans=1&md={1}&my=list_{2}'.format(*format_value)
        request = {"url": url,
                   "method": "get","sleep_time":1,
                   "timeout": self.kwargs.get("request_timeout", 10),
                   "proxies": {"http": self.current_proxy},
                   "headers": {"Connection": "close", "User-Agent": self.ua.chrome}}
        return request

    def parse_item(self, content, seed):
        result = []
        tuples = self.pattern.findall(content)
        if len(tuples) > 0:
            for item in tuples:
                result.append({"brand_id": item[0], "name": item[1], "cate_id":seed.value,"_seed": seed.value,"_status":0})
        if result:
            self.write(result)
        else:
            self.write([{"cate_id":seed.value,"_seed": seed.value, "_status":1}])
        seed.ok()


if __name__ == "__main__":
    current_date = timeUtil.current_time()
    process_manger.kill_old_process(sys.argv[0])
    import logging
    from multiprocess.core import HttpProxy
    config = {"job_name": "jdbrand"
              , "spider_num": 40
              , "retries": 3
              , "request_timeout": 10
              , "complete_timeout": 5*60
              , "sleep_interval": 0.5
              , "rest_time": 5
              , "write_seed": False
              , "seeds_file": "resource/newCateName"
              , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "jingdong",
                                 "collection": "brand" + current_date}
              , "log_config": {"level": logging.ERROR, "filename": sys.argv[0] + '.logging', "filemode":'a', "format":'%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
              ,"proxies_pool": HttpProxy.getHttpProxy()}
    p = GetBrands(**config)
    p.main_loop(show_process=True)
