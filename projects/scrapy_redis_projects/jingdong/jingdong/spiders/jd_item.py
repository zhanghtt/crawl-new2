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


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_item'
    cat_pettern = re.compile(r'cat: \[([,\d]*)\],')
    brand_pettern = re.compile(r'brand: (\d*),')


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            sku_id = seed.value
            url = "https://item.jd.com/{0}.html".format(sku_id)
            return Request(url=url, meta={"_seed": str_seed,
                                          "headers": {"Connection": "close", "Referer": "https://www.jd.com"}},
                           priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        sku_id = seed.value
        cate = self.cate_pattern1.findall(response.text)
        brand_id = self.brand_pettern.findall(response.text)
        if cate and brand_id:
            yield {"new_cate_id": cate[0], "new_brand_id": brand_id[0], "skuid": sku_id}
        elif cate:
            yield {"new_cate_id": cate[0], "new_brand_id":'0', "skuid": sku_id}
        elif brand_id:
            yield {"new_cate_id": "0,0,0", "new_brand_id": brand_id[0], "skuid": sku_id}
        else:
            yield {"new_cate_id": "0,0,0", "new_brand_id": '0', "skuid": sku_id}


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()
import random


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)
        self.out_table = "jdnewcatid{0}retry0".format(current_date)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            m.create_db_collection(db_collection=("jingdong", "jdnewcatid{0}_sep".format(current_date)))
            pipeline = [
                {
                    "$match": {
                        "$and": [{"_status": 0}, {"comment": {"$ne": 0}}]
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
            buffer_size = 10000
            for i, seed in enumerate(skuid_set):
                seed = Seed(value=seed, type=0)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    random.shuffle(buffer)
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                random.shuffle(buffer)
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*3000,buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.out_table), bar_name=self.items_redis_key)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor

    def cleanup(self):
        pipeline = [
            {
                "$match": {
                    "$and": [{"_status": 0}, {"new_cate_id": {"$ne": None}}]
                }
            },
            {
                "$project": {
                    "new_cate_id": "$new_cate_id",
                }
            },
        ]
        with op.DBManger() as m:
            cate_id_old = set()
            for item in m.read_from(db_collect=("jingdong", "newCateName"), out_field=("cate_id",)):
                cate_id_old.add(item[0])
            # skuids in last result
                cate_id_new = set()
            for item in m.read_from(db_collect=("jingdong", self.out_table), out_field=("new_cate_id",),pipeline=pipeline):
                cate_id_new.add(item[0])
            differ = cate_id_new - cate_id_old
            self.logger.info("total new cat_id is: {}".format(len(differ)))
            buffer = []
            for cat_id in differ:
                buffer.append((cat_id,cat_id))
            if buffer:
                m.insert_many_tupe(db_collect=("jicheng","newCateName"), data_tupe_list=buffer,fields=("_id","cate_id"))


class RetryMaster(FirstMaster):
    def __init__(self, *args, **kwargs):
        super(RetryMaster, self).__init__(*args, **kwargs)
        with op.DBManger() as m:
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdnewcatid20\d\d\d\d\d\dretry\d+$"}})
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
