#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil

current_date = timeUtil.current_time()


class JDCommentMaster(Master):
    def __init__(self, *args, **kwargs):
        super(JDCommentMaster, self).__init__(*args, **kwargs)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer = []
        buffer_size = 1024
        with open("jingdong/resource/month202006") as infile:
            data_set = collections.DataSet(infile)
            for i, seed in enumerate(data_set.map(lambda line: line.strip('\n').split("\t")[0])
                                             .shuffle(2048)):
                seed = seed.strip()
                url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                      "&productId={0}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1".format(seed)
                data = {"url": url, "meta": {"_seed": seed}}
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


if __name__ == '__main__':
     master = JDCommentMaster(spider_name="jd_comment", spider_num=2, write_asyn=True, start_id=0)
     master.run()
