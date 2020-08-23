#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
import re
import sys

import numpy as np
from fake_useragent import UserAgent

from multiprocess.core import HttpProxy
from multiprocess.core.spider import SpiderManger, Seed
from multiprocess.tools import process_manger
from multiprocess.tools import timeUtil


class SecooWeekJob(SpiderManger):
    def __init__(self, current_date, **kwargs):
        super(SecooWeekJob, self).__init__(**kwargs)
        self.ua = UserAgent()
        self.current_date = current_date
        space = np.linspace(0, 5800000, kwargs["spider_num"] + 1)
        ranges = [(int(space[i]), int(space[i + 1])) for i in range(len(space) - 1)]
        totalpages_pattern = re.compile(r'<strong>共<i>(\d+)</i>页，到第 <b>')
        self.block_pattern = re.compile(r'dlProId=[\s\W\w]*?</dl>')
        self.pid_pattern = re.compile(r'ProId="\d+"')
        self.name_pattern = re.compile(r'title=".*?"')
        self.lo_pattern = re.compile(r'"s1"[\s\W\w]*?</span>')
        self.price_pattern = re.compile(r'secoo_price.*?</span>')
        self.br_pattern = re.compile(r'</i>.*?</span')
        for r in ranges:
            request = {"url": "http://list.secoo.com/all/0-0-0-0-0-7-0-0-0-10-{0}_{1}-0-100-0.shtml".format(r[0], r[1]),
                       "method":"get",
                       "sleep_time": 1,
                       "timeout": 20,
                       "headers": {"Connection": "close",
                                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
                       }
            respone = self.do_request(request)
            tmp = totalpages_pattern.findall(respone.text)
            if tmp:
                page_num = int(tmp[0])
                self.log.info((page_num, r[0], r[1]))
                for pageindex in range(1, page_num + 1):
                    self.seeds_queue.put(Seed((pageindex, r[0], r[1]), retries=kwargs["retries"]))
            else:
                self.log.info((0, r[0], r[1]))

    def make_request(self, seed):
        url = "http://list.secoo.com/all/0-0-0-0-0-7-0-0-{0}-10-{1}_{2}-0-100-0.shtml".format(*seed.value)
        request = {"url": url,
                   "sleep_time":1,
                   "timeout": 20,
                   "method": "get",
                   "proxies": {"http": self.current_proxy},
                   "headers": {"Connection": "keep-alive",
                               "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}}
        return request

    def parse_item(self, content, seed):
        try:
            results = []
            block = self.block_pattern.findall(content)
            for item in block:
                pid = self.pid_pattern.findall(item)
                if len(pid) > 0:
                    temp = pid[0]
                    pid = temp[7:len(temp) - 1]
                else:
                    pid = 'NA'

                name = self.name_pattern.findall(item)
                if len(name) > 0:
                    temp = name[0]
                    name = temp[7:len(temp) - 1]
                else:
                    name = 'NA'

                lo = self.lo_pattern.findall(item)
                if len(lo) > 0:
                    if len(lo) == 1:
                        temp = lo[0]
                        ziying = temp[5:len(temp) - 7]
                        lo = 'M'
                    else:
                        temp = lo[0]
                        temp1 = lo[1]
                        lo = temp[5:len(temp) - 7]
                        ziying = temp1[5:len(temp) - 7]
                else:
                    lo = 'NA'
                    ziying = 'NA'

                price = self.price_pattern.findall(item)
                if len(price) > 0:
                    temp = self.br_pattern.findall(price[0])
                    if len(temp) > 0:
                        temp = temp[0]
                        price = temp[4:len(temp) - 6]
                    else:
                        price = 'NA'
                else:
                    price = 'NA'

                results.append({"_seed":seed.value,"code": 0, "pid": pid, "name": name, "lo": lo, "self": ziying,"price": price,"_date":self.current_date})
        except:
            results.append({"code": 1,"_seed":seed.value,"_status": 1})
        if results:
            self.write(results)
            seed.ok()

    def clean_price(self):
        from mongo import op
        pipeline = [
            {"$match":
                 {"pid": {"$ne": None}}
             }
        ]
        with op.DBManger() as m:
            dic = {}
            m.drop_db_collect(db_collect=("secoo", "CleanListOld"))
            m.rename_collection(old_db_collection=("secoo", "CleanListNew"),
                                new_db_collection=("secoo", "CleanListOld"))
            for pid, price, self1 in m.read_from(db_collect=("secoo", "CleanListOld"), out_field=("pid", "price","self")):
                dic.update({pid: (price, self1)})
            for pid, price, self1 in m.read_from(db_collect=("secoo", "List" + self.current_date), out_field=("pid", "price","self"),
                                          pipeline=pipeline):
                dic.update({pid: (price, self1)})
            date_tuple_list = []
            for k,(p,s) in dic.items():
                date_tuple_list.append((k,k,p,s))
            m.date_tuple_to_db(date_tuple_list=date_tuple_list, db_collect=("secoo", "CleanListNew"),
                               fields_tupe=("_id", "pid", "price","self"), buffer_size=128, attach_dict={"_date": self.current_date},
                               show_pbar=True, pbar_name="clean_price")

    def init_clean_price(self):
        from mongo import op
        from tqdm import tqdm
        pipeline = [
            {"$match":
                 {"pid": {"$ne": "null"}}
             }
        ]
        with op.DBManger() as m:
            dic = {}
            m.drop_db_collect(db_collect=("secoo", "CleanListNew"))
            for collection in tqdm(m.list_tables("secoo", filter={"name": {"$regex": r"List20\d\d\d\d\d\d"}}),desc="init_clean_price"):
                for pid, price, self1 in m.read_from(db_collect=("secoo", collection), out_field=("pid", "price", "self"), pipeline=pipeline):
                    dic.update({pid: (price, self1)})
            date_tuple_list = []
            for k, (p, s) in dic.items():
                date_tuple_list.append((k, k, p, s))
            m.date_tuple_to_db(date_tuple_list=date_tuple_list,db_collect=("secoo", "CleanListNew"),
                               fields_tupe=("_id", "pid","price","self"), buffer_size=1024, attach_dict={"_date": self.current_date})


if __name__ == "__main__":
    current_date = timeUtil.current_time()
    process_manger.kill_old_process(sys.argv[0])
    import logging
    config = {"job_name": "secoo_month_job"
        , "spider_num": 40
        , "retries": 3
        , "request_timeout": 10
        , "complete_timeout": 1 * 60
        , "rest_time": 15
        , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "secoo",
                           "collection": "List" + current_date}
        , "log_config": {"level": logging.ERROR,"filename": sys.argv[0] + '.logging', "filemode":'a',
                         "format": '%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
        , "proxies_pool": HttpProxy.getHttpProxy()
        }
    p = SecooWeekJob(current_date, **config)
    p.main_loop(show_process=True)
    p.clean_price()

