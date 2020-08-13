#!/usr/bin/env python
# -*- coding: utf-8 -*-
from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter


class ShouJiSlaver(Slaver):
    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor


if __name__ == '__main__':
    slaver = ShouJiSlaver(spider_name="shoujiguishudi", spider_num=16)
    slaver.run()
