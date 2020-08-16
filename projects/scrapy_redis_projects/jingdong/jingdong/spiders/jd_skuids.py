#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider
import urllib
from mongo import op
from multiprocess.core.spider import Seed
from ast import literal_eval
from scrapy.http import Request


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_skuid'
    first_pettern = re.compile(r"search000014_log:{wids:'([,\d]*?)',")
    skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
    totalpage_perttern = re.compile(r'<div id="J_topPage"[\s\S]*?<b>\d+</b><em>/</em><i>(\d+)</i>')

    def parse1(self, response):
        print(response.meta)
        pass

    def parse(self, response):
        seed = literal_eval(response.meta["_seed"])
        page_strs = self.totalpage_perttern.findall(response.text)
        print(page_strs)
        if page_strs:
            page_strs = page_strs[0]
            for i in range(1, int(page_strs) + 1):
                page, s = 2 * i - 1, 60 * (i - 1) + 1
                cate_id, brand_id = seed
                if brand_id:
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, 2 * (i-1) - 1, 60 * (i - 2) + 1)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(en_cate_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(
                        en_cate_id, en_brand_id, 2 * (i - 1) - 1, 60 * (i - 2) + 1)
                yield Request(url=url, callback=self.parse1, meta={"headers": {"Connection": "close", "User-Agent": self.ua.chrome,
                                       "Referer": refer}})
                # request = {"url": url,
                #            "sleep_time": 0.156 + random.random() / 10,
                #            "method": "get",
                #            "proxies": {"https": self.current_proxy},
                #            "headers": {"Connection": "close", "User-Agent": self.ua.chrome,
                #                        "Referer": url}}
                # rs1 = self.do_request(request).text
                # if rs1:
                #     r1 = self.first_pettern.findall(rs1)
                #     if r1:
                #         r1 = r1[0]
                #         if r1:
                #             for pid in r1.split(","):
                #                 seed.counter.increase()
                #                 request = {"url": "https://item.jd.com/{}.html".format(pid),
                #                            "sleep_time": 0.156 + random.random() / 10,
                #                            "method": "get",
                #                            "proxies": {"https": self.current_proxy},
                #                            "headers": {"Connection": "close", "User-Agent": self.ua.chrome,
                #                                        "Referer": "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&click=1".format(
                #                                            en_cate_id, en_name, page, s)}}
                #                 rs2 = self.do_request(request).text
                #                 if rs2:
                #                     r2 = self.skuids_pettern.findall(rs2)
                #                     for skuid in r2:
                #                         buffer.append({"skuid": skuid, "cate_id": cate_id, "_seed": str(seed)})
                #
                #             seed2 = Seed(value=(seed.value[0], seed.value[1], seed.value[2], page + 1, s + 30, r1))
                #             cate_id, _, name, page, s, items = seed2.value
                #             en_cate_id, en_name = urllib.parse.urlencode(
                #                 {"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + name})
                #             url = 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={4}'.format(
                #                 en_cate_id, en_name, page, s, items)
                #             request = {"url": url,
                #                        "sleep_time": 0.156 + random.random() / 10,
                #                        "method": "get",
                #                        "proxies": {"https": self.current_proxy},
                #                        "headers": {"Connection": "close", "User-Agent": self.ua.chrome,
                #                                    "Referer": "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&click=1".format(
                #                                        en_cate_id, en_name, page - 1, s - 30)}}
                #             rs3 = self.do_request(request).text
                #             if rs3:
                #                 r3 = self.first_pettern.findall(rs3)
                #                 if r3:
                #                     r3 = r3[0]
                #                     if r3:
                #                         for pid in r3.split(","):
                #                             seed.counter.increase()
                #                             request = {"url": "https://item.jd.com/{}.html".format(pid),
                #                                        "sleep_time": 0.156 + random.random() / 10,
                #                                        "method": "get",
                #                                        "proxies": {"https": self.current_proxy},
                #                                        "headers": {"Connection": "close",
                #                                                    "User-Agent": self.ua.chrome,
                #                                                    "Referer": "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&click=1".format(
                #                                                        en_cate_id, en_name, page - 1, s - 30)}}
                #                             rs4 = self.do_request(request).text
                #                             if rs4:
                #                                 r4 = self.skuids_pettern.findall(rs4)
                #                                 for skuid in r4:
                #                                     buffer.append(
                #                                         {"skuid": skuid, "cate_id": cate_id, "_seed": str(seed)})


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()


class Master(Master):
    def __init__(self, *args, **kwargs):
        super(Master, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpsProxy()):
        super(Master, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer = []
        buffer_size = 1024
        with op.DBManger() as m:
            last_brand_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^brand20\d\d\d\d\d\d$"}})
            pipeline = [
                {"$match": {"cate_id": {"$ne": None}}},
                {"$match": {"_status": 0}},
                {"$limit" : 2}
            ]
            data_set = collections.DataSet(m.read_from(db_collect=("jingdong", last_brand_collect), out_field=("cate_id", "brand_id"), pipeline=pipeline))
            for i, seed in enumerate(data_set.distinct()):
                seed = Seed(value=seed, type=0)
                cate_id, brand_id = seed.value
                if brand_id:
                    cid1, cid2, cid3 = re.split(',', cate_id)
                    if cid1 == "1713":
                        en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                            {"ev": "expublishers_" + brand_id})
                    else:
                        en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                            {"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&cid3={2}&psort=4&click=1'.format(en_cate_id, en_brand_id, cid3)
                else:
                    url = 'https://list.jd.com/list.html?{0}&psort=4&click=1'.format(urllib.parse.urlencode({"cat": cate_id}))
                data = {"url": url, "meta": {"_seed": str(seed.value),
                                             "headers": {"Referer": "https://www.jd.com/"}}}
                buffer.append(str(data))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdskuid{0}".format(current_date)), bar_name=self.items_redis_key)
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


def run():
    master = Master(spider_name=Spider.name, spider_num=2, write_asyn=True, start_id=0)
    master.run()