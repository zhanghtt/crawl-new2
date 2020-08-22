#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.core.spider import Seed


class ShouJiMaster(Master):
    def __init__(self, *args, **kwargs):
        super(ShouJiMaster, self).__init__(*args, **kwargs)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer = []
        buffer_size = 1024
        for i, seed in enumerate(open("shoujiguishudi/resource/buyer_phone")):
            seed = Seed(value=seed.strip(), type=0)
            buffer.append(str(seed))
            if len(buffer) % buffer_size == 0:
                self.redis.sadd(self.start_urls_redis_key, *buffer)
                buffer = []
        if buffer:
            self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*1,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jicheng","shoujiguishudi"), bar_name=self.items_redis_key)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, bar_name=self.items_redis_key,
        #                                  out_file="shoujiguishudi/result/shoujiguishudi.txt",
        #                                table_header=["_seed","_status","phonenumber", "province", "city", "company"])
        thread_writer.setDaemon(False)
        return thread_writer

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


if __name__ == '__main__':
    master = ShouJiMaster(spider_name="shoujiguishudi", spider_num=16, write_asyn=True)
    master.run()
