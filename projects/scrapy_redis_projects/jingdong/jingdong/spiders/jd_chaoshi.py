#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
from mongo import op
from multiprocess.core.spider import Seed
from scrapy_redis.utils import bytes_to_str


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_chaoshi'
    totalpage_perttern = re.compile(r'<div id="J_topPage"[\s\S]*?<b>\d+</b><em>/</em><i>(\d+)</i>')

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            return Request(url=seed.value, meta={"_seed": str_seed}, priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse1(self, response):
        pass
    
    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        page_strs = self.totalpage_perttern.findall(response.text)
        if int(page_strs[0]) < 100:
            #no need to flip
            pass
        else:
            #need to flip
            pass
        if page_strs:
            page_strs = page_strs[0]


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer_size = 1024
        with op.DBManger() as m:
            m.create_db_collection(db_collection=("jingdong", "jdchaoshi{0}_sep".format(current_date)))
            buffer=[]
            import requests
            request = {"url": "https://chaoshi.jd.com/",
                       "headers": {
                           'Connection': 'close',
                           "Referer": "https://www.jd.com",
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
                       }}
            nav_pattern = re.compile(r'navThird[1-9]: (\[.*\])')
            import time
            from ast import literal_eval
            src = requests.get(**request).text
            for i in nav_pattern.findall(src):
                for j in literal_eval(i):
                    for k in j["children"]:
                        seed = Seed(value=k["URL"].replace("\\", ""), type=0)
                        buffer.append(str(seed))
                        if len(buffer) % buffer_size == 0:
                            self.redis.sadd(self.start_urls_redis_key, *buffer)
                            buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*3000,buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdchaoshi{0}retry0".format(current_date)), bar_name=self.items_redis_key, distinct_field=None)
        thread_writer.setDaemon(True)
        return thread_writer

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


class RetryMaster(FirstMaster):
    def __init__(self, *args, **kwargs):
        super(RetryMaster, self).__init__(*args, **kwargs)
        with op.DBManger() as m:
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdchaoshi20\d\d\d\d\d\d(retry\d+)?$"}})
            self.new_retry_collect = self.last_retry_collect[:self.last_retry_collect.find("retry") + 5] + str(int(self.last_retry_collect[self.last_retry_collect.find("retry") + 5:]) + 1) if self.last_retry_collect.find("retry") != -1 else self.last_retry_collect+"retry1"
            self.logger.info((self.last_retry_collect, self.new_retry_collect))

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.new_retry_collect), bar_name=self.items_redis_key, distinct_field=None)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*30, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid.txt",
        #                                table_header=["_seed","_status","phonenumber", "province", "city", "company"])
        thread_writer.setDaemon(True)
        return thread_writer

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer = []
        buffer_size = 1024
        with op.DBManger() as m:
            pipeline = [
                {"$match": {"_status": 3}
                }
            ]
            data_set = collections.DataSet(m.read_from(db_collect=("jingdong", self.last_retry_collect), out_field=("_seed","_status"), pipeline=pipeline))
            should_exit = True
            for i, (seed, status) in enumerate(data_set.distinct()):
                should_exit = False
                seed = Seed(value=seed, type=3)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)
            if should_exit:
                import sys
                sys.exit(0)


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
