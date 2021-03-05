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
    name = 'jd_comment'
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
            #url = "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku={0}&sorttype=6&page=0".format(skuid)
            url = "https://wq.jd.com/commodity/comment/getcommentlist?callback=skuJDEvalB&version=v2&pagesize=10&sceneval=2&skucomment=1&score=0&sku={}&sorttype=6&page=1&t=0.5156075450518778".format(
                skuid)
            headers = {
               'Connection': 'close',
               'Host':'wq.jd.com',
               'accept':'*/*',
               'sec-fetch-site':'same-site',
               'sec-fetch-mode':'no-cors',
               'sec-fetch-dest':'script',
               "Referer": "https://item.m.jd.com/ware/view.action?wareId={}&sid=null".format(skuid),
               'accept-encoding':'gzip, deflate, br',
               'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
               'User-Agent': 'Mozilla/5.0 (Linux; Android 10; HRY-AL00a; HMSCore 5.1.1.303) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.7.303 Mobile Safari/537.36',
               "cookie":"__jdc=122270672; mba_muid=16087105855231456793479; shshshfpa=b86c237d-b506-9cc9-730d-39db2f5ea48c-1608710586; shshshfpb=aW2xjA0PZevBiTvJrQ6rk4A%3D%3D; retina=1; webp=1; visitkey=31140776387466944; sbx_hot_h=null; deviceVersion=83.0.4103.106; deviceOS=android; deviceOSVersion=10; deviceName=Chrome; rurl=https%3A%2F%2Fwqs.jd.com%2Ffaqs%2Findex.html%3Fsceneval%3D2%26ptag%3D7001.1.124%26productId%3D12991458%26ispg%3D%26_fd%3Djdm%26jxsid%3D16109541564584400343; equipmentId=A75Q6PQS36IHI62HBEUGC44IVLERE7257UWVYTGEXPMR6NOKARSVVF2Q6EBPSVGNR537LK6GQN3ENW47JREOEXNAVI; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1614224630058; sc_width=360; shshshfp=c6774e911e47825ddd51cefc23f9b157; wxa_level=1; cid=9; jxsid=16145705280303310338; __jda=122270672.16087105855231456793479.1608710585.1614224630.1614570529.10; wq_ug=14; fingerprint=794164a430090764096f40466260c718; mt_xid=V2_52007VwMVU1ReUlsbQB1YBmUDF1ZaXlpYGk8RbFVuBEBVWV9RRkhIGw4ZYlcRWkFQWwlIVR5aAjAAR1BZX1tZHnkaXQZnHxNQQVlSSx9JElgFbAEbYl9oUmoXSB5dDWYKE1BZXlNeF08cVQNvMxJbWV8%3D; wq_logid=1614571192.282863947; wqmnx1=MDEyNjM5M3AuL3d3MiY2NjQ1eGQtTTFBaSBsby8zd3IzZTUyNy00UkghKQ%3D%3D; __jdb=122270672.9.16087105855231456793479|10.1614570529; mba_sid=16145705290954323095988279117.9; __wga=1614571199267.1614570547761.1614225998734.1610954174749.5.6; PPRD_P=UUID.16087105855231456793479-LOGID.1614571199300.300139660; jxsid_s_t=1614571199496; jxsid_s_u=https%3A//item.m.jd.com/ware/view.action; sk_history=70241615154%2C101609%2C615036%2C54761686610%2C1399903%2C10024515889185%2C10381689654%2C12991458%2C100010062010%2C58070892025%2C100007627009%2C; shshshsID=e45b3b58ca53b7ab42489de6ebc02d6b_5_1614571200418"
           }
            return Request(url=url, meta={"_seed": str_seed,"dydmc_delay": 0.15 + random.random() * 0.1,
                                          "headers": headers},
                           priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        skuid = seed.value
        count = self.allcnt_pattern.findall(response.text)
        yield {"skuid":skuid,"comment":count[0]}

from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()
import random


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            #创建临时表本月任务的分界线
            m.create_db_collection(db_collection=("jingdong","jdcomment{0}_sep".format(current_date)))
            skuid_set = set()
            pipeline = [
                {
                    "$match": {
                        "$and": [{"_status": 0}, {"skuid": {"$ne": None}}]
                    }
                 },
                {
                    "$project": {
                        "skuid": "$skuid",
                    }
                },
                {"$limit": 400}
            ]
            # last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep$"}})
            # for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
            last_sep = m.get_lasted_collection("jingdong",
                                               filter={"name": {"$regex": r"^jdskuid20200920_sep$"}})
            for table in m.list_tables(dbname="jingdong",
                                       filter={"name": {"$regex": r"^jdskuid20200920retry\d*$"}}):
                if not last_sep or table > last_sep:
                    self.logger.info("valid table : {}".format(table))
                    for item in m.read_from(db_collect=("jingdong", table), out_field=("skuid",), pipeline=pipeline):
                        skuid_set.add(int(item[0]))
            #skuids in last result
            pipeline = [
                {"$limit": 40}
            ]
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^month20\d\d\d\d$"}})
            for item in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid",),pipeline=pipeline):
                skuid_set.add(int(item[0]))
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
                                          db_collection=("jingdong","jdcomment{0}retry0".format(current_date)), bar_name=self.items_redis_key, distinct_field="skuid")
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field="skuid")
        thread_writer.setDaemon(False)
        thread_writer.start()

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


class ContinueMaster(Master):
    def __init__(self, table_name, *args, **kwargs):
        self.table_name = table_name
        super(ContinueMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(ContinueMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            #创建临时表本月任务的分界线
            m.create_db_collection(db_collection=("jingdong","jdcomment{0}_sep".format(current_date)))
            skuid_set = set()
            pipeline = [
                {
                    "$match": {
                        "$and": [{"_status": 0}, {"skuid": {"$ne": None}}]
                    }
                 },
                {
                    "$project": {
                        "skuid": "$skuid",
                    }
                },
                #{"$limit": 40}
            ]
            # last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep$"}})
            # for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
            last_sep = m.get_lasted_collection("jingdong",
                                               filter={"name": {"$regex": r"^jdskuid20200920_sep$"}})
            for table in m.list_tables(dbname="jingdong",
                                       filter={"name": {"$regex": r"^jdskuid20200920retry\d*$"}}):
                if not last_sep or table > last_sep:
                    self.logger.info("valid table : {}".format(table))
                    for item in m.read_from(db_collect=("jingdong", table), out_field=("skuid",), pipeline=pipeline):
                        skuid_set.add(int(item[0]))
            #skuids in last result
            last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
            for item in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid",)):
                skuid_set.add(int(item[0]))
            skuid_set1 = set()
            for item in m.read_from(db_collect=("jingdong", self.table_name), out_field=("skuid",),pipeline=pipeline):
                skuid_set1.add(int(item[0]))
            buffer = []
            buffer_size = 10000
            for i, seed in enumerate(skuid_set):
                if seed not in skuid_set1:
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
                                          db_collection=("jingdong",self.table_name), bar_name=self.items_redis_key, distinct_field="skuid")
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field="skuid")
        thread_writer.setDaemon(False)
        thread_writer.start()

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


class TmpMaster(Master):
    def __init__(self, intable, outtable, *args, **kwargs):
        self.intable = intable
        self.outtable = outtable
        super(TmpMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(TmpMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        with op.DBManger() as m:
            skuid_set = set()
            for item in m.read_from(db_collect=("jingdong", self.intable), out_field=("skuid",)):
                skuid_set.add(int(item[0]))
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
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.outtable),
                                          bar_name=self.items_redis_key, distinct_field="skuid")
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*3000, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid{0}".format(current_date),
        #                                table_header=["_seed","_status","skuid", "cate_id", "brand_id", "shopid","venderid","shop_name","ziying"])
        thread_writer.setDaemon(True)
        return thread_writer

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field="skuid")
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
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20\d\d\d\d\d\dretry\d+$"}})
            self.new_retry_collect = self.last_retry_collect[:self.last_retry_collect.find("retry") + 5] + str(int(self.last_retry_collect[self.last_retry_collect.find("retry") + 5:]) + 1) if self.last_retry_collect.find("retry") != -1 else self.last_retry_collect+"retry1"
            self.logger.info((self.last_retry_collect, self.new_retry_collect))

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.new_retry_collect), bar_name=self.items_redis_key, distinct_field="skuid")
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
            #data_set = collections.DataSet(m.read_from(db_collect=("jingdong", self.last_retry_collect), out_field=("_seed","_status"), pipeline=pipeline))
            buffer = []
            buffer_size = 10000
            should_exit = True
            for i, (seed, status) in enumerate(m.read_from(db_collect=("jingdong", self.last_retry_collect), out_field=("_seed","_status"), pipeline=pipeline)):
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


def run_tmp_master(intable, outtable, spider_name=Spider.name, spider_num=1, write_asyn=True):
    master = TmpMaster(intable, outtable, spider_name=spider_name, spider_num=spider_num, write_asyn=write_asyn)
    master.run()


def run_init_proxies(spider_name=Spider.name):
    master = FirstMaster(spider_name=spider_name, spider_num=0, write_asyn=True)
    master.init_proxies_queue()


def run_continue_master(table_name, spider_name=Spider.name):
    master = ContinueMaster(table_name=table_name, spider_name=spider_name, spider_num=1, write_asyn=True)
    master.run()
