#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
import urllib
from mongo import op
from multiprocess.core.spider import Seed
from scrapy_redis.utils import bytes_to_str
import json
from ..Tools import format_cat_id
import random


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_price_miss'
    rid = random.randint(100000000, 999999999)
    usrid = str(rid)
    price_pattern = re.compile(r'^\d+\.\d\d$')
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            sku_ids = seed.value
            url = "http://p.3.cn/prices/mgets?&type=1&skuIds=J_" + sku_ids + '&pduid=' + self.usrid
            return Request(url=url, meta={"_seed": str_seed,
                                          "headers": {"Connection": "keep-alive"}},
                           priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def clean_price(self, item):
        price = 0
        k = 0
        if 'l' in item and 'm' in item:
            if item['l'] < item['m']:
                for key in item:
                    str_price_list = self.price_pattern.findall(item[key])
                    if key != 'l' and key != 'm' and str_price_list:
                        price = price + float(str_price_list[0])
                        k = k + 1
            else:
                for key in item:
                    str_price_list = self.price_pattern.findall(item[key])
                    if key != 'l' and str_price_list:
                        price = price + float(str_price_list[0])
                        k = k + 1
        if price == 0:
            price = 79.90
            k = 1
        return round(price/k, 2)

    def parse(self, response):
        items = json.loads(response.text)
        if items:
            for item in items:
                if item.get("id"):
                    item["id"] = item["id"][2:]
                    # item['clean_price'] = self.clean_price(item)
            yield dict(item)
        else:
            raise Exception("unvalid error!")


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()
import random


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)
        self.out_table = "jdpricemiss{0}retry0".format(current_date)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            m.create_db_collection(db_collection=("jingdong", "jdpricemiss{0}_sep".format(current_date)))
            pipeline = [
                {
                    "$match": {
                        "$and": [{"_status": 0}, {"comment": {"$gt": 0}}]
                    }
                },
                {
                    "$project": {
                        "skuid": "$skuid",
                    }
                },
            ]
            skuid_set = set()
            last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20\d\d\d\d\d\d_sep"}})
            for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20\d\d\d\d\d\d)retry\d*$"}}):
                if not last_sep or table > last_sep:
                    self.logger.info("valid table : {}".format(table))
                    for item in m.read_from(db_collect=("jingdong", table), out_field=("skuid",), pipeline=pipeline):
                        skuid_set.add(int(item[0]))
            #skuids in last result
            skuid_set1 = set()
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
            for item in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid",)):
                skuid_set1.add(int(item[0]))
            skuid_set = skuid_set - skuid_set1
            self.logger.info("total new skuid of comment larger than 0 is: {}".format(len(skuid_set)))
            buffer = []
            for i, seed in enumerate(skuid_set):
                seed = str(seed)
                current = seed.strip()
                if i % 60 == 0:
                    if i != 0:
                        seed = Seed(value=strr, type=0)
                        buffer.append(str(seed))
                    strr = current
                else:
                    strr = strr + '%2CJ_' + current
            if strr:
                seed = Seed(value=strr, type=0)
                buffer.append(str(seed))
            if buffer:
                buffer1 = []
                buffer_size = 10000
                for i, seed in enumerate(buffer):
                    buffer1.append(str(seed))
                    if len(buffer1) % buffer_size == 0:
                        random.shuffle(buffer1)
                        self.redis.sadd(self.start_urls_redis_key, *buffer1)
                        buffer1 = []
                if buffer1:
                    random.shuffle(buffer1)
                    self.redis.sadd(self.start_urls_redis_key, *buffer1)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*3000,buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.out_table), bar_name=self.items_redis_key)
        thread_writer.setDaemon(True)
        return thread_writer

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor

    def cleanup(self):
        pass


class RetryMaster(FirstMaster):
    def __init__(self, *args, **kwargs):
        super(RetryMaster, self).__init__(*args, **kwargs)
        with op.DBManger() as m:
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdpricemiss20\d\d\d\d\d\dretry\d+$"}})
            self.new_retry_collect = self.last_retry_collect[:self.last_retry_collect.find("retry") + 5] + str(int(self.last_retry_collect[self.last_retry_collect.find("retry") + 5:]) + 1) if self.last_retry_collect.find("retry") != -1 else self.last_retry_collect+"retry1"
            self.logger.info((self.last_retry_collect, self.new_retry_collect))
        self.out_table = self.new_retry_collect

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.out_table), bar_name=self.items_redis_key)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*30, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid.txt",
        #                                table_header=["_seed","_status","phonenumber", "province", "city", "company"])
        thread_writer.setDaemon(True)
        return thread_writer

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            pipeline = [
                {"$match": {"_status": 3}},
            ]
            data_set = collections.DataSet(m.read_from(db_collect=("jingdong", self.last_retry_collect), out_field=("_seed","_status"), pipeline=pipeline))
            buffer = []
            buffer_size = 10000
            for i, (seed, status) in enumerate(data_set.distinct()):
                seed = Seed(value=seed, type=3)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    random.shuffle(buffer)
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                random.shuffle(buffer)
                self.redis.sadd(self.start_urls_redis_key, *buffer)


def run_master(retry=False, spider_name=Spider.name, spider_num=1, write_asyn=True):
    if retry:
        master = RetryMaster(spider_name=spider_name, spider_num=spider_num, write_asyn=write_asyn)
        master.run()
    else:
        master = FirstMaster(spider_name=spider_name, spider_num=spider_num, write_asyn=write_asyn)
        master.run()


def run_slaver(spider_name=Spider.name, spider_num=1):
    slaver = Slaver(spider_name=spider_name, spider_num=spider_num)
    slaver.run()
