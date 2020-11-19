#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
import urllib
from mongo import op
from multiprocess.core.spider import Seed
from scrapy_redis.utils import bytes_to_str
import json
from ast import literal_eval

class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_comment_detail'
    allcnt_pattern = re.compile(r'"CommentCount": \"(\d+)\",')
    comments_pattern = re.compile(r'"comments":[\s\S]*?(\[[\s\S]*\])')

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            skuid = seed.value
            url = "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku={0}&sorttype=6&page=0".format(skuid)
            return Request(url=url, meta={"_seed": str_seed,
                                          "headers": {"Connection": "close", "Referer": "https://item.m.jd.com/{0}.html".format(skuid)}},
                           priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        skuid = seed.value
        count = self.allcnt_pattern.findall(response.text)
        for item in literal_eval(self.comments_pattern.findall(response.text)[0].replace("\t","").replace("\n","").replace(",}","}").replace("false",'False').replace("true",'True').replace('False,','"False",').replace('True,','"True",')):
            yield {"id":item.get("id"),"creationTime":item.get("creationTime"),"isTop": str(item.get('isTop')),
                   "isMobile":item.get("isMobile"),"userLevelName":item.get("userLevelName"),
                   "userClientShow":item.get("userClientShow"),"plusAvailable":item.get("plusAvailable"),
                   "firstCategory": item.get("firstCategory"), "secondCategory": item.get("secondCategory"),"thirdCategory": item.get("thirdCategory"),
                   "discussionId":item.get("discussionId"),"referenceId":item.get("referenceId"),
                   "referenceTime":item.get("referenceTime"),"nickname":item.get("nickname"),"commentcout":count[0]}
        maxpagesindex = max(0, min((int(count[0])-1)//10, 99))
        for pindex in range(maxpagesindex+1):
            url = "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku={0}&sorttype=6&page={1}".format(skuid, pindex)
            yield Request(url=url, meta={"_seed": response.meta["_seed"],"commentcount":count[0],
                                          "headers": {"Connection": "close",
                                                      "Referer": "https://item.m.jd.com/{0}.html".format(skuid)}},
                           priority=1, callback=self.parse1)

    def parse1(self, response):
        for item in literal_eval(self.comments_pattern.findall(response.text)[0].replace("\t","").replace("\n","").replace(",}","}").replace("false",'False').replace("true",'True').replace('False,','"False",').replace('True,','"True",')):
            yield {"id":item.get("id"),"creationTime":item.get("creationTime"),"isTop":str(item.get('isTop')),
                   "isMobile":item.get("isMobile"),"userLevelName":item.get("userLevelName"),
                   "userClientShow":item.get("userClientShow"),"plusAvailable":item.get("plusAvailable"),
                   "firstCategory": item.get("firstCategory"), "secondCategory": item.get("secondCategory"),"thirdCategory": item.get("thirdCategory"),
                   "discussionId":item.get("discussionId"),"referenceId":item.get("referenceId"),
                   "referenceTime":item.get("referenceTime"),"nickname":item.get("nickname"),"commentcount":response.meta["commentcount"]}


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()
import random
from multiprocess.tools.collections import TopK


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpsProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            #创建临时表本月任务的分界线
            m.create_db_collection(db_collection=("jingdong","jdcommentdetail{0}_sep".format(current_date)))
            skuid_set = {}
            top1000w = TopK(1000000)
            #skuids in last result
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
            pipeline = [
                {
                    "$project": {
                        "skuid": "$skuid",
                        "comment_{}".format(last_result[-6:]):"$comment_{}".format(last_result[-6:])
                    }
                },
                #{"$limit": 1000}
            ]
            for item, comments in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid","comment_{}".format(last_result[-6:])),pipeline=pipeline):
                if int(item) not in skuid_set:
                    top1000w.push(int(comments))
                    skuid_set[int(item)] = int(comments)
            top1000w = set(top1000w.get_topk())
            buffer = []
            buffer_size = 10000
            for i, seed in enumerate(skuid_set):
                if skuid_set[seed] in top1000w:
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
                                          db_collection=("jingdong","jdcommentdetail{0}retry0".format(current_date)), bar_name=self.items_redis_key, distinct_field=None)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field=None)
        thread_writer.setDaemon(False)
        thread_writer.start()

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


class ContinueMaster(Master):
    def __init__(self, *args, **kwargs):
        super(ContinueMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpsProxy()):
        super(ContinueMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            #创建临时表本月任务的分界线
            m.create_db_collection(db_collection=("jingdong","jdcommentdetail{0}_sep".format(current_date)))
            skuid_set = {}
            top1000w = TopK(100000)
            #skuids in last result
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
            pipeline = [
                {
                    "$project": {
                        "skuid": "$skuid",
                        "comment_{}".format(last_result[-6:]):"$comment_{}".format(last_result[-6:])
                    }
                },
                #{"$limit": 1000}
            ]
            for item, comments in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid","comment_{}".format(last_result[-6:])),pipeline=pipeline):
                if int(item) not in skuid_set:
                    top1000w.push(int(comments))
                    skuid_set[int(item)] = int(comments)
            for item in m.read_from(db_collect=("jingdong", "jdcommentdetail20201113retry0"), out_field=("referenceId",),pipeline=pipeline):
                if item[0] and int(item[0]) in skuid_set:
                    skuid_set.pop(int(item[0]))
            top1000w = set(top1000w.get_topk())
            buffer = []
            buffer_size = 10000
            for i, seed in enumerate(skuid_set):
                if skuid_set[seed] in top1000w:
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
                                          db_collection=("jingdong","jdcommentdetail{0}retry0".format(current_date)), bar_name=self.items_redis_key, distinct_field=None)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field=None)
        thread_writer.setDaemon(False)
        thread_writer.start()

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
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcommentdetail20\d\d\d\d\d\dretry\d+$"}})
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
        with op.DBManger() as m:
            pipeline = [
                {"$match": {"_status": 3}},
            ]
            data_set = collections.DataSet(m.read_from(db_collect=("jingdong", self.last_retry_collect), out_field=("_seed","_status"), pipeline=pipeline))
            buffer = []
            buffer_size = 10000
            should_exit = True
            for i, (seed, status) in enumerate(data_set.distinct()):
                should_exit = False
                seed = Seed(value=seed, type=3)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    random.shuffle(buffer)
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                random.shuffle(buffer)
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


def run_writer(tablename,spider_name=Spider.name):
    master = FirstMaster(spider_name=spider_name, spider_num=0)
    master.process_items(tablename=tablename)


def run_init_proxies(spider_name=Spider.name):
    master = FirstMaster(spider_name=spider_name, spider_num=0, write_asyn=True)
    master.init_proxies_queue()


def run_continue_master(spider_name=Spider.name):
    master = ContinueMaster(spider_name=spider_name, spider_num=1, write_asyn=True)
    master.run()
