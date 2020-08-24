#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiprocess.core.spider import SpiderManger, Seed
from multiprocess.core import HttpProxy
from multiprocess.tools import process_manger
import re
import sys
from multiprocess.tools import timeUtil
from mongo import op
from tqdm import tqdm
import time
from datetime import date
import json
import random
from fake_useragent import UserAgent


class SecooMonthJob(SpiderManger):
    def __init__(self, current_date, **kwargs):
        super(SecooMonthJob, self).__init__(**kwargs)
        self.ua = UserAgent()
        self.current_date = current_date
        with op.DBManger() as m:
            total = m.count(db_collect=("secoo", "CleanListNew"))
            for pid, price in tqdm(m.read_from(db_collect=("secoo", "CleanListNew"), out_field=("pid", "price")),
                                   total=total, desc="reading"):
                self.seeds_queue.put(Seed((pid, price), kwargs["retries"], type=0))
        self.seed_retries = kwargs["retries"]
        self.page_pattern = re.compile(r'totalCurrCommentNum":.*?,')
        self.block_pattern = re.compile(r'{"isShow.*?}')
        self.bench = timeUtil.getdate(-90, format='%Y%m%d')
        self.log.info("bench: " + self.bench)
        self.id_pattern = re.compile(r'"id":\d+')
        self.pid_pattern = re.compile(r'productId":\d+')
        self.time_pattern = re.compile(r'createDate":\d+')
        self.user_pattern = re.compile(r'userName":".*?"')
        self.device_pattern = re.compile(r'sourceDevice":".*?"')

    def make_request(self, seed):
        url = 'https://las.secoo.com/api/comment/show_product_comment?filter=0&page=1' \
              '&pageSize=10&productBrandId=&productCategoryId=&productId={0}&type=0&callback=jsonp1'.format(seed.value[0])
        request = {"url": url,
                   "sleep_time": 0,
                   "timeout": 20,
                   "method": "get",
                   "proxies": {"http": self.current_proxy},
                   "headers": {"Connection": "close", "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}}
        return request

    def parse_item(self, content, seed):
        if content.find('"retCode":"0"') == -1:
            self.write([{"_status":3, "_seed":seed.value}])
            seed.ok()
            return
        pid, price = seed.value
        page = self.page_pattern.findall(content)
        if len(page) > 0:
            temp = page[0]
            totalpage = int(temp[21:len(temp) - 1])
            temp = int(totalpage / 10)
            if totalpage > temp * 10:
                pagecount = temp + 1
            else:
                pagecount = temp
        else:
            return
        result = []
        for pageid in range(1, pagecount + 1):
            url = 'https://las.secoo.com/api/comment/show_product_comment?filter=0&page={0}' \
                  '&pageSize=10&productBrandId=&productCategoryId=&productId={1}&type=0&callback=jsonp1'.format(pageid,pid)
            request = {"url": url,
                       "sleep_time": 0,
                       "timeout": 20,
                       "method": "get",
                       "proxies": {"http": self.current_proxy},
                       "headers": {"Connection": "close",
                                   "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}}
            respone = self.do_request(request)
            content = respone.text

            pid_rel, price = seed.value
            block = self.block_pattern.findall(content)

            for item in block:
                cid = self.id_pattern.findall(item)
                if len(cid) > 0:
                    temp = cid[0]
                    cid = temp[5:len(temp)]
                else:
                    cid = 'NA'

                pid = self.pid_pattern.findall(item)
                if len(pid) > 0:
                    temp = pid[0]
                    pid = temp[11:len(temp)]
                else:
                    pid = 'NA'

                time2 = self.time_pattern.findall(item)
                if len(time2) > 0:
                    temp = time2[0]
                    time1 = temp[12:len(temp)]
                    datestr = date.fromtimestamp(float(time1) / 1000).strftime('%Y%m%d')
                else:
                    datestr = 'NoDate'

                user = self.user_pattern.findall(item)
                if len(user) > 0:
                    temp = user[0]
                    user = temp[11:len(temp) - 1]
                else:
                    user = 'NA'

                device = self.device_pattern.findall(item)
                if len(device) > 0:
                    temp = device[0]
                    device = temp[15:len(temp) - 1]
                else:
                    device = 'NA'
                if datestr != 'NoDate':
                    if (self.bench <= datestr):
                        result.append({"cid": cid, "pid_rel": pid_rel, "pid":pid, "user": user, "device": device,
                                       "price": price, "date": datestr, "_date": self.current_date, "_status":0})
                    else:
                        if result:
                            self.write(result)
                            seed.ok()
                            return
        if result:
            self.write(result)
            seed.ok()

    def compute_result(self):
        from mongo import op
        from multiprocess.tools import timeUtil
        current_date = self.current_date
        current_month = current_date[:-2]
        last_1_month, last_2_month, last_3_month = timeUtil.get_month(-1, current_month), timeUtil.get_month(-2,current_month), timeUtil.get_month(-3, current_month),
        comment_table = "secoComment{}".format(current_date)
        with op.DBManger() as m:
            for month in [last_1_month,last_2_month,last_3_month]:
                # 合并属于一个月的List
                m.drop_db_collect(db_collect=("secoo", "List{}".format(month)))
                dic = {}
                for listday in m.list_tables(dbname="secoo", filter={"name": {"$regex": r"List{}\d\d$".format(month)}}):
                    print(listday, "List{}".format(month))
                    for item in m.read_from(db_collect=("secoo", listday), out_field=("pid", "price", "self")):
                        dic.update({item[0]: (item[1], item[2])})
                date_tuple_list = []
                for k, (p, s) in dic.items():
                    date_tuple_list.append((k, k, p, s))
                m.insert_many_tupe(db_collect=("secoo", "List{}".format(month)), data_tupe_list=date_tuple_list,
                                   fields=("_id", "pid", "price", "self"))
                # 有销量
                pipeline1 = [
                    {
                        "$match": {
                            "$and": [{"_status": 0}, {"pid": {"$ne": None}}]
                        }
                    },
                    {
                        "$project": {
                            "cid": "$cid",
                            "pid_rel": "$pid_rel",
                            "pid": "$pid",
                            "user": "$user",
                            "device": "$device",
                            "price": "$price",
                            "date": "$date",
                            "month": {"$substr": ["$date", 0, 6]},
                            "self": "$self",
                        }
                    },
                    {
                        "$match": {
                            "month": "{}".format(month)
                        }
                    },
                    {
                        "$lookup": {
                            "from": "CleanListNew",
                            "localField": "pid",
                            "foreignField": "_id",
                            "as": "tableb"
                        }
                    },
                    {
                        "$group": {
                            "_id": {
                                "month": "$month",
                                "cid": "$cid",
                                "pid": "$pid",
                                "pid_rel": "$pid_rel",

                            },
                            "user": {
                                "$last": "$user",
                            },
                            "device": {
                                "$last": "$device",
                            },
                            "price": {
                                "$last": "$price",
                            },
                            "tmp_price": {
                                "$last": {
                                    "$arrayElemAt": [
                                        "$tableb.price",
                                        0
                                    ]
                                }

                            },
                            "tmp_self": {
                                "$last": {
                                    "$arrayElemAt": [
                                        "$tableb.self",
                                        0
                                    ]
                                }

                            },
                        },
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "month": "$_id.month",
                            "cid": "$_id.cid",
                            "pid_rel": "$_id.pid_rel",
                            "pid": "$_id.pid",
                            "user": "$user",
                            "device": "$device",
                            "price": {
                                "$cond": {
                                    "if": {"$ne": ["$tmp_price", None]}, "then": "$tmp_price",
                                    "else": "$price"
                                }
                            },
                            "tmp_self": "$tmp_self",
                        }
                    },
                    {
                        "$lookup": {
                            "from": "CleanListNew",
                            "localField": "pid_rel",
                            "foreignField": "_id",
                            "as": "tablec"
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "month": "$month",
                            "cid": "$cid",
                            "pid_rel": "$pid_rel",
                            "pid": "$pid",
                            "user": "$user",
                            "device": "$device",
                            "price": "$price",
                            "tmp_self": "$tmp_self",
                            "tmp_self1": {
                                "$arrayElemAt": [
                                    "$tablec.self",
                                    0
                                ]
                            },
                        }
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "month": "$month",
                            "cid": "$cid",
                            "pid_rel": "$pid_rel",
                            "pid": "$pid",
                            "user": "$user",
                            "device": "$device",
                            "price": "$price",
                            "self": {
                                "$cond": {
                                    "if": {"$ne": ["$tmp_self", None]}, "then": "$tmp_self",
                                    "else": {
                                        "if": {"$ne": ["$tmp_self1", None]}, "then": "$tmp_self1",
                                        "else": "其他"
                                    }
                                }
                            },
                        }
                    },
                    {
                        "$group": {
                            "_id": {
                                "month": "$month",
                                "cid": "$cid",
                                "pid": "$pid",
                                "price": "$price",
                            },
                            "self": {
                                "$last": "$self"
                            }
                        },
                    },
                    {
                        "$group": {
                            "_id": {
                                "month": "$_id.month",
                                "pid": "$_id.pid",
                                "price": "$_id.price",
                            },
                            "sales": {"$sum": 1},
                            "self": {"$last": "$self"},
                        },
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "month": "$_id.month",
                            "pid": "$_id.pid",
                            "sales": "$sales",
                            "price": "$_id.price",
                            "self": {
                                "$cond": {
                                    "if": {"$ne": ["$self", "自营"]}, "then": "0",
                                    "else": "1"
                                }
                            },
                        }
                    },
                    {
                        "$out": "secoSales{}".format(month)
                    }
                ]
                # 无销量
                pipeline2 = [
                    {
                        "$match": {
                            "$and": [{"_status": {"$ne": 0}}, {"_seed": {"$ne": None}}]
                        }
                    },
                    {
                        "$project": {
                            "pid_rel": {"$arrayElemAt": [
                                "$_seed",
                                0
                            ]
                            },
                            "price": {"$arrayElemAt": [
                                "$_seed",
                                1
                            ]
                            },
                        }
                    },
                    {
                        "$lookup": {
                            "from": "List{}".format(month),
                            "localField": "pid_rel",
                            "foreignField": "_id",
                            "as": "tableb"
                        }
                    },
                    {
                        "$project": {
                            "pid_rel": "$pid_rel",
                            "price": "$price",
                            "self": {
                                "$arrayElemAt": [
                                    "$tableb.self",
                                    0
                                ]
                            },
                        }
                    },
                    {
                        "$match": {
                            "self": {"$exists": True}
                        }
                    },
                    {
                        "$group": {
                            "_id": {
                                "pid_rel": "$pid_rel",
                                "price": "$price",
                            },
                            "self": {
                                "$last": "$self"
                            },
                        },
                    },
                    {
                        "$project": {
                            "_id": 0,
                            "month": "{}".format(month),
                            "pid": "$_id.pid_rel",
                            "sales": "0",
                            "price": "$_id.price",
                            "self": {
                                "$cond": {
                                    "if": {"$ne": ["$self", "自营"]}, "then": "0",
                                    "else": "1"
                                }
                            },
                        }
                    },
                    {
                        "$out": "secoNosales{}".format(month)
                    }
                ]
                m.aggregate(db_collect=("secoo", comment_table), pipeline=pipeline1)
                m.aggregate(db_collect=("secoo", comment_table), pipeline=pipeline2)
                dic = {}
                for item in m.read_from(db_collect=("secoo", "secoNosales{}".format(month)),
                                        out_field=("pid", "price", "sales", "self")):
                    dic.update({item[0]: (item[1], item[2], item[3])})
                for item in m.read_from(db_collect=("secoo", "secoSales{}".format(month)),
                                        out_field=("pid", "price", "sales", "self")):
                    dic.update({item[0]: (item[1], item[2], item[3])})
                date_tuple_list = []
                for k, (p, s, self) in dic.items():
                    date_tuple_list.append((k, k, p, s, self))
                m.drop_db_collect(db_collect=("secoo", "secoResult{}".format(month)))
                m.insert_many_tupe(db_collect=("secoo", "secoResult{}".format(month)), data_tupe_list=date_tuple_list,
                                   fields=("_id", "pid", "price", "sales", "self"))


if __name__ == "__main__":
    current_date = timeUtil.current_time()
    process_manger.kill_old_process(sys.argv[0])
    import logging
    config = {"job_name": "secoo_month_job"
              , "spider_num": 40
              , "retries": 3
              , "rest_time": 1
              , "complete_timeout": 3*60
              , "mongo_config": {"addr": "mongodb://192.168.0.13:27017", "db": "secoo", "collection": "secoComment" + current_date}
              , "log_config": {"level": logging.ERROR, "filename": sys.argv[0] + '.logging', "filemode":'a',"format":'%(asctime)s - %(filename)s - %(processName)s - [line:%(lineno)d] - %(levelname)s: %(message)s'}
              , "proxies_pool": HttpProxy.getHttpProxy()
              }
    p = SecooMonthJob(current_date, **config)
    p.main_loop(show_process=True)
    p.compute_result()
