#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
import urllib
from mongo import op
from multiprocess.core.spider import Seed
from scrapy_redis.utils import bytes_to_str
import json


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_skuid_v3'
    first_pettern = re.compile(r"search000014_log:{wids:'([,\d]*?)',")
    skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
    totalpage_perttern = re.compile(r'<div id="J_topPage"[\s\S]*?<b>\d+</b><em>/</em><i>(\d+)</i>')
    shopid_pettern = re.compile(r'shopId:\'(\d*)\',')
    venderid_pettern = re.compile(r'venderId:(\d*),')
    brand_pettern = re.compile(r'brand: (\d*),')
    skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
    shop_name_pettern = re.compile(r'target="_blank" title="(\S*?)" clstag="shangpin')
    ziying_pettern = re.compile(r'<div class="contact fr clearfix">[\s]*?<div class="name goodshop EDropdown">[\s]*?<em class="u-jd">[\s]*?(\S*?)[\s]*?</em>[\s]*?</div>')
    cat_pettern = re.compile(r'cat: \[([,\d]*)\],')
    json_pettern = re.compile(r"jQuery8117083\((\[.*?\])\)")
    sku_pattern1 = re.compile(r'<li data-sku="(\d+)"[\s\S]*?class="gl-item">[\s\S]*?<em>([^￥][\s\S]*?)</em>[\s\S]*?</li>')

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.type == 0:
            cate_id, brand_id, name = seed.value
            if brand_id:
                cid1, cid2, cid3 = re.split(',', cate_id)
                # if cid1 == "1713":
                #     en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                #         {"ev": "expublishers_" + brand_id})
                # else:
                #en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + name})
                url = 'https://list.jd.com/list.html?{0}&{1}&cid3={2}&psort=4&click=1'.format(
                    urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + name}), cid3)
            else:
                url = 'https://list.jd.com/list.html?{0}&psort=4&click=1'.format(urllib.parse.urlencode({"cat": cate_id}))
            return Request(url=url, meta={"_seed": str_seed, "headers": {"Referer": "https://www.jd.com/"}}, priority=0, callback=self.parse)
        elif seed.type == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse3(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, page, s = seed.value
        r = json.loads(self.json_pettern.findall(response.text)[0])
        if r:
            for item in r:
                if item:
                    yield {"skuid": item.get("pid"), "cate_id": cate_id, "brand_id": brand_id, "shopid": item.get("shopId"),
                           "venderid": item.get("venderId", None), "shop_name": item.get("seller"),
                           "ziying": 1 if item.get("seller") and item.get("seller").find("自营") != -1 else 0,
                           "title":response.meta["sku2title"][str(item.get("pid"))],"chaoshi":1 if "京东超市" in response.meta["sku2title"][str(item.get("pid"))] else 0}
                else:
                    self.logger.info("jd_skuids 2")
        else:
            raise Exception(response.request.url)

    def parse2(self, response):
        last_page_pids = response.meta["last_page_pids"]
        r1 = self.first_pettern.findall(response.text)
        if r1:
            r1 = r1[0]
            if r1:
                sku2title = {}
                for sku in self.sku_pattern1.findall(response.text):
                    sku2title[sku[0]] = re.sub("<[\s\S]*?>|\t|\n", "", sku[1])
                response.meta["sku2title"].update(sku2title)
                yield Request(url="https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083".format(last_page_pids + "," + r1), callback=self.parse3, meta=response.meta)
            else:
                # 说明没有下半页"https://chat1.jd.com/api/checkChat?pidList=10020242230938,1999899692,72276507174,19999997645,1999899692,100000002015,100000002686,200134637813&callback=jQuery8117083"
                yield Request(
                    url="https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083".format(last_page_pids),
                    callback=self.parse3, meta=response.meta)
        else:
            if response.meta["currentpage"] <= 2*response.meta["totalpage"]-1:
                raise Exception(response.request.url)
            else:
                #说明没有下半页"https://chat1.jd.com/api/checkChat?pidList=10020242230938,1999899692,72276507174,19999997645,1999899692,100000002015,100000002686,200134637813&callback=jQuery8117083"
                yield Request(url="https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083".format(last_page_pids), callback=self.parse3, meta=response.meta)

    def parse1(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, name, page, s = seed.value
        sku2title = {}
        for sku in self.sku_pattern1.findall(response.text):
            sku2title[sku[0]] = re.sub("<[\s\S]*?>|\t|\n", "", sku[1])
        r1 = self.first_pettern.findall(response.text)
        if r1:
            r1 = r1[0]
            if r1:
                cate_id, brand_id, page, s, items = cate_id, brand_id, page + 1, s + 30, r1
                if brand_id:
                    en_cate_id, ename = urllib.parse.urlencode(
                        {"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + name})
                    url = 'https://list.jd.com/list.html?{0}&{1}&psort=4&page={2}&s={3}&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={4}'.format(
                        en_cate_id, ename, page, s, items)
                    request = Request(url=url, callback=self.parse2, priority=2)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                        en_cate_id, ename, page-1, s-30)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&psort=4&page={1}&s={2}&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={3}'.format(
                        en_cate_id, page, s, items)
                    request = Request(url=url, callback=self.parse2, priority=2)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1".format(
                        en_cate_id, page - 1, s - 30)
                request.meta["_seed"] = str(Seed((cate_id, brand_id, page, s), type=2))
                request.meta["last_page_pids"] = r1
                request.meta["sku2title"] = sku2title
                request.meta["totalpage"] = response.meta["totalpage"]
                request.meta["currentpage"] = page - 1
                yield request
            else:
                raise Exception(response.request.url)
        else:
            raise Exception(response.request.url)

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        page_strs = self.totalpage_perttern.findall(response.text)
        if page_strs:
            page_strs = page_strs[0]
            for i in range(1, int(page_strs) + 1):
                page, s = 2 * i - 1, 60 * (i - 1) + 1
                cate_id, brand_id, name = seed.value
                if brand_id:
                    en_cate_id, ename = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + name})
                    url = 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, ename, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, ename, 2 * (i-1) - 1, 60 * (i - 2) + 1)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(en_cate_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(
                        en_cate_id, 2 * (i - 1) - 1, 60 * (i - 2) + 1)
                yield Request(url=url, callback=self.parse1, meta={"totalpage":int(page_strs),"currentpage":page,"_seed": str(Seed((cate_id, brand_id, name, page, s), type=1)), "headers": {"Connection": "close", "Referer": refer}}, priority=1)
        else:
            raise Exception(response.request.url)


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
        with op.DBManger() as m:
            m.create_db_collection(db_collection=("jingdong", "jdskuid{0}_sep".format(current_date)))
            last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdbrand20\d\d\d\d\d\d_sep$"}})
            seed_set = set()
            for table in  m.list_tables("jingdong", filter={"name": {"$regex": r"^jdbrand20\d\d\d\d\d\dretry\d*$"}}):
                if not last_sep or table > last_sep:
                    self.logger.info("valid table : {}".format(table))
                    pipeline = [
                        {"$match": {
                            "$and": [{"_status": 0}, {"$or": [{"status": 0}, {"status": -1}]}]
                            }
                        },
                        {
                            "$limit":1
                        }
                    ]
                    for seed in m.read_from(db_collect=("jingdong", table), out_field=("cate_id", "brand_id","name"), pipeline=pipeline):
                        seed_set.add(seed)
            for i, seed in enumerate(seed_set):
                seed = Seed(value=seed, type=0)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*3000,buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdskuid{0}retry0".format(current_date)), bar_name=self.items_redis_key, distinct_field="skuid")
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

    def process_items(self, tablename):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12 * 3000, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", tablename),
                                          bar_name=self.items_redis_key, distinct_field="skuid")
        thread_writer.setDaemon(False)
        thread_writer.start()


class RetryMaster(FirstMaster):
    def __init__(self, *args, **kwargs):
        super(RetryMaster, self).__init__(*args, **kwargs)
        with op.DBManger() as m:
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\dretry\d+$"}})
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
        buffer = []
        buffer_size = 1024
        with op.DBManger() as m:
            pipeline = [
                {"$match": {"_status": 3}},
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


def run_writer(tablename, spider_name=Spider.name):
    master = FirstMaster(spider_name=spider_name, spider_num=0)
    master.process_items(tablename=tablename)
