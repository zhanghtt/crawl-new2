#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_comment2'
    allcnt_pattern = re.compile(r'"commentCount":(\d+),')

    def parse(self, response):
        count = self.allcnt_pattern.findall(response.text)
        if not count:
            yield {"skuid": response.meta["_seed"], "comment": 0, }
        else:
            yield {"skuid": response.meta["_seed"], "comment": int(count[0])}

from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpsProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer = []
        buffer_size = 1024
        with open("jingdong/resource/month202007") as infile:
            data_set = collections.DataSet(infile)
            for i, seed in enumerate(data_set.map(lambda line: line.strip('\n').split("\t")[0])
                                             .shuffle(2048)):
                seed = seed.strip()
                url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                      "&productId={0}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1".format(seed)
                data = {"url": url, "meta": {"_seed": seed,
                                             "headers": {"Referer": "https://item.jd.com/{0}.html".format(seed)}}}
                buffer.append(str(data))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdcomment{0}".format(current_date)), bar_name=self.items_redis_key)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, bar_name=self.items_redis_key,
        #                                  out_file="shoujiguishudi/result/shoujiguishudi.txt",
        #                                table_header=["_seed","_status","phonenumber", "province", "city", "company"])
        thread_writer.setDaemon(True)
        return thread_writer

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


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
