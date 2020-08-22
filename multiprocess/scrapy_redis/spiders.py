#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import threading
import time

import psutil
import pymongo
import redis
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from tqdm import tqdm

from scrapy_redis.spiders import RedisSpider
from scrapy_redis.utils import bytes_to_str


class Request(Request):

    def serialize(self):
        dumps = {"encoding": self.encoding, "method": self.method, "priority": self.priority,
                 "callback": self.callback.__name__ if self.callback else None,
                 "errback": self.errback.__name__ if self.errback else None,
                 "cookies": self.cookies,
                 "headers": self.headers, "dont_filter": self.dont_filter, "meta": self.meta, "url": self.url,
                 "cb_kwargs": self._cb_kwargs, "flags": self.flags}
        return str(dumps)

    @classmethod
    def deserialize(cls, str_request, self):
        item_dict = eval(str_request)
        item_dict["callback"] = getattr(self, item_dict["callback"]) if item_dict["callback"] else None
        item_dict["errback"] = getattr(self, item_dict["errback"]) if item_dict["errback"] else None
        return cls(**item_dict)


class JiChengSpider(RedisSpider):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(JiChengSpider, cls).from_crawler(crawler, *args, **kwargs)
        obj.params = kwargs
        return obj

    def make_request_from_data(self, data):
        data = bytes_to_str(data, self.redis_encoding)
        data = eval(data)
        return Request(url=data["url"], meta=data["meta"], priority=0, callback=self.parse)


class ThreadMonitor(threading.Thread):
    def __init__(self, redis_key, start_urls_num_redis_key, interval=1, bar_name=None):
        threading.Thread.__init__(self)
        self.start_urls_num_redis_key = start_urls_num_redis_key
        self.setDaemon(True)
        self.setting = get_project_settings()
        self.redis = get_redis_from_settings(self.setting)
        self.redis_key = redis_key
        self.total = int(self.redis.get(self.start_urls_num_redis_key))
        self.interval = interval
        if bar_name:
            self.bar_name = bar_name
        else:
            self.bar_name = self.redis_key
        self.stop = False

    def run(self):
        with tqdm(total=self.total, desc=self.bar_name) as pbar:
            last_size = self.total
            while not self.stop:
                end = time.time() + self.interval
                current_size = self.redis.scard(self.redis_key)
                pbar.update(last_size - current_size)
                if time.time() < end:
                    time.sleep(end - time.time())
                last_size = current_size
                if current_size == 0:
                    self.stop = True


class ThreadWriter(threading.Thread):
    def __init__(self, redis_key, bar_name=None, buffer_size=512, show_pbar=True, stop_epoch=12*30, distinct_field=None):
        threading.Thread.__init__(self)
        self.distinct_field = distinct_field
        self.show_pbar = show_pbar
        self.stop = False
        self.stop_epoch = stop_epoch
        self.buffer_size = buffer_size
        self.counter = 0
        self.setting = get_project_settings()
        self.redis = get_redis_from_settings(self.setting)
        self.redis_key = redis_key
        self.total = self.redis.llen(self.redis_key)
        if bar_name:
            self.bar_name = bar_name
        else:
            self.bar_name = self.redis_key
        self.distinct_set = set()

    def write(self, item):
        raise NotImplementedError

    def flush(self):
        raise NotImplementedError

    def setup(self):
        pass

    def cleanup(self):
        pass

    @property
    def logger(self):
        logger = logging.getLogger(__name__)
        return logging.LoggerAdapter(logger, {'ThreadWriter': self})

    def run(self):
        if self.show_pbar:
            with tqdm(total=self.total, desc=self.bar_name) as pbar:
                retries = self.stop_epoch
                while not self.stop:
                    current_element = self.redis.lpop(self.redis_key)
                    if current_element:
                        pbar.update(1)
                        self.write(current_element)
                        retries = self.stop_epoch
                    else:
                        self.flush()
                        retries = retries - 1
                        time.sleep(5)
                    if retries <= 0:
                        self.stop = True
                self.flush()
                self.cleanup()
        else:
            retries = self.stop_epoch
            while not self.stop:
                current_element = self.redis.lpop(self.redis_key)
                if current_element:
                    self.write(current_element)
                    retries = self.stop_epoch
                else:
                    self.flush()
                    retries = retries - 1
                    time.sleep(5)
                if retries <= 0:
                    self.stop = True
            self.flush()
            self.cleanup()


class ThreadFileWriter(ThreadWriter):
    def __init__(self, redis_key, out_file, table_header, stop_epoch=12*1, bar_name=None, buffer_size=32, distinct_field=None, encoding="utf-8",file_mode="w"):
        super(ThreadFileWriter, self).__init__(redis_key=redis_key, stop_epoch=stop_epoch,
                                               bar_name=bar_name, buffer_size=buffer_size,distinct_field=distinct_field)
        self.out_file = out_file
        self.out = open(self.out_file, file_mode, encoding=encoding)
        self.table_header = table_header
        self.out.write("\t".join(self.table_header) + "\n")
        self.buffer = []

    def is_already_write(self, item):
        if self.distinct_field:
            if item.get(self.distinct_field) is None:
                return False
            if item.get(self.distinct_field) in self.distinct_set:
                return True
            else:
                self.distinct_set.add(item.get(self.distinct_field))
                return False
        else:
            return False

    def stop(self):
        self.stop = True

    def write(self, item):
        item = item.decode("utf-8")
        try:
            item = eval(item)
        except NameError as e:
            self.logger.exception(e)
            old = item
            item = eval(item.replace("null","None"))
            item = {key: item[key] for key in item if item[key] is not None}
            self.logger.warning("replace item: {} to {}".format(str(old),str(item)))
        if self.is_already_write(item):
            return
        self.counter = self.counter + 1
        self.buffer.append(item)
        if self.counter % self.buffer_size == 0:
            self.flush()

    def flush(self):
        if self.buffer:
            #values = ["\t".join([str(item[key]) for key in self.table_header]) for item in self.buffer]
            values = []
            for item in self.buffer:
                value = ""
                for key in self.table_header:
                    if key in item:
                        if value:
                            value = value + "\t" + str(item.get(key))
                        else:
                            value = str(item.get(key))
                    else:
                        value = value + "\t" + "NA"
                if value:
                    values.append(value)
            self.out.write("\n".join(values) + "\n")
            self.buffer = []
            self.counter = 0

    def cleanup(self):
        self.out.close()


class ThreadMongoWriter(ThreadWriter):
    def __init__(self, redis_key, db_collection, out_mongo_url=None, stop_epoch=12*1, bar_name=None, buffer_size=512, distinct_field=None):
        super(ThreadMongoWriter, self).__init__(redis_key=redis_key, stop_epoch=stop_epoch, bar_name=bar_name, buffer_size=buffer_size, distinct_field=distinct_field)
        if out_mongo_url is None:
            self.setting = get_project_settings()
            out_mongo_url = self.setting.get("MONGO_URL")
        if out_mongo_url is None:
            raise Exception("out_mongo_url must be setted!")
        self.db = pymongo.MongoClient(out_mongo_url)
        self.out = self.db[db_collection[0]][db_collection[1]]
        self.buffer = []

    def stop(self):
        self.stop = True

    def is_already_write(self, item):
        if self.distinct_field:
            if item.get(self.distinct_field) is None:
                return False
            if item.get(self.distinct_field) in self.distinct_set:
                return True
            else:
                self.distinct_set.add(item.get(self.distinct_field))
                return False
        else:
            return False

    def write(self, item):
        item = item.decode("utf-8")
        try:
            item = eval(item)
        except NameError as e:
            #self.logger.exception(e)
            old = item
            item = eval(item.replace("null","None"))
            item = {key: item[key] for key in item if item[key] is not None}
            self.logger.warning("replace item: {} to {}".format(str(old),str(item)))

        if self.is_already_write(item):
            return
        self.counter = self.counter + 1

        self.buffer.append(item)
        if self.counter % self.buffer_size == 0:
            self.flush()

    def flush(self):
        if self.buffer:
            self.out.insert_many(self.buffer)
            self.buffer = []
            self.counter = 0

    def cleanup(self):
        self.db.close()


from scrapy.utils.project import get_project_settings
from scrapy_redis.connection import get_redis_from_settings
import logging
from scrapy.utils.log import configure_logging


class ClusterRunner(object):
    def __init__(self, spider_name, spider_num=psutil.cpu_count(logical=True),  write_asyn=True):
        self.write_asyn = write_asyn
        self.spider_name = spider_name
        self.spider_num = spider_num
        self.start_urls_redis_key = "%(name)s:start_urls" % {"name": self.spider_name}
        self.items_redis_key = "%(name)s:items" % {"name": self.spider_name}
        self.setting = get_project_settings()
        self.logger = self.get_loger()
        self.redis = get_redis_from_settings(self.setting)
        self.redis = redis.Redis(host='192.168.0.117', port=6379, db=0)
        self.logger.info(self.redis)

    def get_loger(self):
        log_config = {}
        parmer_map = {"LOG_LEVEL":"level","LOG_FILE":"filename","LOG_FORMAT":"format"}
        for key in self.setting:
            if key in parmer_map:
                log_config[parmer_map[key]] = self.setting[key]
        logging.basicConfig(**log_config)
        return logging.getLogger(__name__)

    def get_thread_writer(self):
        return None

    def get_thread_monitor(self):
        return None

    @classmethod
    def run_spider(cls, spider_name):
        from scrapy.cmdline import execute
        execute(['scrapy', 'crawl', spider_name])

    def init_start_urls(self):
        raise NotImplementedError

    def run(self):
        if self.spider_num <= 0:
            return
        #初始化种子URL
        self.init_start_urls()
        #开启监控线程
        self.thread_monitor = self.get_thread_monitor()
        if self.thread_monitor:
            self.thread_monitor.start()
            self.logger.info("start monitor success !")

        if self.write_asyn:
            #开启爬虫
            if self.spider_num > 1:
                process = CrawlerProcess(get_project_settings())
                for spider in [self.spider_name]*self.spider_num:
                    process.crawl(spider)  # 根据爬虫名列表爬取
                process.start()
            elif self.spider_num == 1:
                self.logger.info("mode : run in standalone !")
                self.run_spider(spider_name=self.spider_name)


            self.thread_writer = self.get_thread_writer()
            if self.thread_writer:
                # 开启写线程
                self.thread_writer.start()
                self.logger.info("start writer success !")
                # 开启爬虫
                if self.spider_num > 1:
                    process = CrawlerProcess(get_project_settings())
                    for spider in [self.spider_name] * self.spider_num:
                        process.crawl(spider)  # 根据爬虫名列表爬取
                    process.start()
                elif self.spider_num == 1:
                    self.logger.info("mode : run in standalone !")
                    self.run_spider(spider_name=self.spider_name)
                self.thread_writer.join()
        else:
            # 开启爬虫
            if self.spider_num > 1:
                process = CrawlerProcess(get_project_settings())
                for spider in [self.spider_name] * self.spider_num:
                    process.crawl(spider)  # 根据爬虫名列表爬取
                process.start()
            elif self.spider_num == 1:
                self.logger.info("mode : run in standalone !")
                self.run_spider(spider_name=self.spider_name)

            # 开启写线程
            self.thread_writer = self.get_thread_writer()
            if self.thread_writer:
                self.thread_writer.start()
                self.logger.info("start writer success !")
                self.thread_writer.join()


class Cluster(object):
    def __init__(self, spider_name, spider_num=psutil.cpu_count(logical=True), start_id=0):
        self.spider_name = spider_name
        self.spider_num = spider_num
        self.setting = get_project_settings()
        configure_logging(self.setting)
        self.start_urls_redis_key = self.setting.get("START_URLS_KEY",
                                                     "%(name)s:start_urls") % {"name": self.spider_name}
        self.items_redis_key = self.setting.get("RESULT_ITEMS_REDIS_KEY", "%(name)s:items") % {"name": self.spider_name}
        self.start_urls_num_redis_key = self.setting.get("START_URLS_NUM_KEY",
                                                         "%(name)s:start_urls_num") % {"name": self.spider_name}
        self.http_proxies_queue_redis_key = self.setting.get("HTTP_PROXIES_QUEUE_REDIS_KEY",
                                                              "%(name)s:http_proxies_queue") % {"name": self.spider_name}
        self.dupefilter_redis_key = self.setting.get("SCHEDULER_DUPEFILTER_KEY",
                                                             "%(spider)s:dupefilter") % {"spider": self.spider_name}
        self.logger = logging.getLogger(__name__)
        self.redis = get_redis_from_settings(self.setting)
        self.logger.info(self.redis)
        self.start_id = start_id #范围start_id>=0 and start_id+self.spider_num<=237
        if not (self.start_id >= 0 and start_id + self.spider_num <= 237):
            raise InterruptedError("not valid start_id, spider_num")

    def run(self):
        raise NotImplementedError


class Slaver(Cluster):
    def __init__(self, *args, **kwargs):
        super(Slaver, self).__init__(*args, **kwargs)

    def get_thread_monitor(self):
        thread_monitor = ThreadMonitor(redis_key=self.start_urls_redis_key,
                                       start_urls_num_redis_key=self.start_urls_num_redis_key,
                                       bar_name=self.start_urls_redis_key)
        thread_monitor.setDaemon(True)
        return thread_monitor

    def check_avaliable_proxiex(self):
        if self.redis.llen(self.http_proxies_queue_redis_key) < self.spider_num:
            raise Exception("alivalid proxies {} must be greater than spider_num {}".format(self.redis.llen(self.http_proxies_queue_redis_key), self.spider_num))

    def run(self):
        self.check_avaliable_proxiex()
        #开启监控线程
        self.thread_monitor = self.get_thread_monitor()
        if self.thread_monitor:
            self.thread_monitor.start()
            self.logger.info("start monitor success !")
        process = CrawlerProcess(get_project_settings())
        for i, spider in enumerate([self.spider_name] * self.spider_num, start=self.start_id):
            process.crawl(spider, **{"id": i})  # 根据爬虫名列表爬取
        process.start()


from multiprocess.core.HttpProxy import getHttpProxy


class Master(Cluster):
    def __init__(self, write_asyn=True, *args, **kwargs):
        super(Master, self).__init__(*args, **kwargs)
        self.write_asyn = write_asyn

    def get_thread_writer(self):
        return NotImplementedError

    def get_thread_monitor(self):
        return NotImplementedError

    def clear_dupefilter_redis(self):
        self.redis.delete(self.dupefilter_redis_key)

    def check_avaliable_proxiex(self):
        if self.redis.llen(self.http_proxies_queue_redis_key) < self.spider_num:
            raise Exception("alivalid proxies {} must be greater than spider_num {}".format(self.redis.llen(self.http_proxies_queue_redis_key), self.spider_num))

    def init_proxies_queue(self, proxies=getHttpProxy()):
        self.redis.delete(self.http_proxies_queue_redis_key)
        buffer = [str(None)]
        for proxy in proxies:
            buffer.append(str(proxy))
        self.redis.rpush(self.http_proxies_queue_redis_key, *buffer)
        self.check_avaliable_proxiex()

    def init_start_urls(self):
        raise NotImplementedError

    def run(self):
        if self.spider_num == 0 and not self.write_asyn:
            return
        self.clear_dupefilter_redis()
        #初始化代理池
        self.init_proxies_queue()
        #初始化种子URL
        self.init_start_urls()
        self.redis.set(self.start_urls_num_redis_key, self.redis.scard(self.start_urls_redis_key))
        #开启监控线程
        self.thread_monitor = self.get_thread_monitor()
        if self.thread_monitor:
            self.thread_monitor.start()
            self.logger.info("start monitor success !")
        if self.write_asyn:
            self.thread_writer = self.get_thread_writer()
            if self.thread_writer:
                self.thread_writer.show_pbar = False
                if self.spider_num == 0:
                    #如果master不开爬虫任务，只负责init_start_urls()，并且self.thread_writer一直等待 需要手动关闭
                    self.thread_writer.stop_epoch = 10000000000
                # 开启写线程
                self.thread_writer.start()
                self.logger.info("start writer success !")
                # 开启爬虫
                process = CrawlerProcess(get_project_settings())
                for i, spider in enumerate([self.spider_name] * self.spider_num, start=self.start_id):
                    process.crawl(spider, **{"id": i})  # 根据爬虫名列表爬取
                process.start()
                #self.thread_writer.join()
        else:
            # 开启爬虫
            process = CrawlerProcess(get_project_settings())
            for i, spider in enumerate([self.spider_name] * self.spider_num, start=self.start_id):
                process.crawl(spider, **{"id": i})  # 根据爬虫名列表爬取
            process.start()
            # 开启写线程
            self.thread_writer = self.get_thread_writer()
            if self.thread_writer:
                self.thread_writer.start()
                self.logger.info("start writer success !")
                #self.thread_writer.join()

