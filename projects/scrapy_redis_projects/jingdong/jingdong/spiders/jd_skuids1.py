#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider
import urllib
from mongo import op
from multiprocess.core.spider import Seed
from ast import literal_eval
from scrapy.http import Request
from scrapy_redis.utils import bytes_to_str
from ast import literal_eval
import types


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_skuid1'
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

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        print(seed.value)
        print(seed.type)
        if seed.type == 0:
            cate_id, brand_id = seed.value
            if brand_id:
                cid1, cid2, cid3 = re.split(',', cate_id)
                if cid1 == "1713":
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                        {"ev": "expublishers_" + brand_id})
                else:
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                        {"ev": "exbrand_" + brand_id})
                url = 'https://list.jd.com/list.html?{0}&{1}&cid3={2}&psort=4&click=1'.format(en_cate_id, en_brand_id,
                                                                                              cid3)
            else:
                url = 'https://list.jd.com/list.html?{0}&psort=4&click=1'.format(urllib.parse.urlencode({"cat": cate_id}))
            return Request(url=url, meta={"_seed": str(seed), "headers": {"Referer": "https://www.jd.com/"}}, priority=0)
        elif seed.type == 1:
            return Request(url=seed.url, callback=self.parse1, meta={"_seed": str_seed, "headers": seed.headers}, priority=1)
        elif seed.type == 2:
            return Request(url=seed.url, callback=self.parse2, meta={"_seed": str_seed, "headers": seed.headers}, priority=1)
        elif seed.type == 3:
            return Request(url=seed.url, callback=self.parse3, meta={"_seed": str_seed, "headers": seed.headers}, priority=1)

    def parse3(self, response):
        cate_id, brand_id, page, s = response.meta["_seed"]
        shopid = self.shopid_pettern.findall(response.text)
        if shopid:
            shopid = shopid[0]
        else:
            shopid = None
        venderid = self.venderid_pettern.findall(response.text)
        if venderid:
            venderid = venderid[0]
        else:
            venderid = None
        brand_new_id = self.brand_pettern.findall(response.text)
        if brand_new_id:
            brand_new_id = brand_new_id[0]
        else:
            brand_new_id = None
        shop_name = self.shop_name_pettern.findall(response.text)
        if shop_name:
            shop_name = set(shop_name).pop()
        else:
            shop_name = None
        ziying = self.ziying_pettern.findall(response.text)
        if ziying:
            ziying = 1
        else:
            ziying = 0
        cat_new = self.cat_pettern.findall(response.text)
        if cat_new:
            cat_new = cat_new[0]
        else:
            cat_new = None
        r2 = self.skuids_pettern.findall(response.text)
        for skuid in r2:
            yield {"skuid": skuid, "cate_id": cate_id, "brand_id": brand_id, "shopid": shopid, "venderid":venderid, "brand_new_id":brand_new_id, "shop_name":shop_name,"ziying":ziying, "cat_new":cat_new}

    def parse2(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, page, s = seed.value
        r1 = self.first_pettern.findall(response.text)
        if r1:
            r1 = r1[0]
            if r1:
                for pid in r1.split(","):
                    if brand_id:
                        en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                            {"ev": "exbrand_" + brand_id})
                        request = Request(url="https://item.jd.com/{}.html".format(pid), callback=self.parse3,
                                          priority=3)
                        request.headers[
                            "Referer"] = "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                            en_cate_id, en_brand_id, page, s)
                    else:
                        en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                        request = Request(url="https://item.jd.com/{}.html".format(pid), callback=self.parse3,
                                          priority=3)
                        request.headers[
                            "Referer"] = "https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1".format(
                            en_cate_id, page, s)
                    request.meta["_seed"] = str(Seed((cate_id, brand_id, page, s), type=3))
                    yield request

    def parse1(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, page, s = seed.value
        r1 = self.first_pettern.findall(response.text)
        if r1:
            r1 = r1[0]
            if r1:
                for pid in r1.split(","):
                    if brand_id:
                        en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                        request = Request(url="https://item.jd.com/{}.html".format(pid), callback=self.parse3, priority=3)
                        request.headers["Referer"]="https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                                                   en_cate_id, en_brand_id, page, s)
                    else:
                        en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                        request = Request(url="https://item.jd.com/{}.html".format(pid), callback=self.parse3, priority=3)
                        request.headers[
                            "Referer"] = "https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1".format(
                            en_cate_id, page, s)
                    request.meta["_seed"] = str(Seed((cate_id, brand_id, page, s), type=3))
                    yield request

                cate_id, brand_id, page, s, items = cate_id, brand_id, page + 1, s + 30, r1
                if brand_id:
                    en_cate_id, en_brand_id = urllib.parse.urlencode(
                        {"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&psort=4&page={2}&s={3}&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={4}'.format(
                        en_cate_id, en_brand_id, page, s, items)
                    request = Request(url=url, callback=self.parse2, priority=2)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                        en_cate_id, en_brand_id, page-1, s-30)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&psort=4&page={1}&s={2}&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={4}'.format(
                        en_cate_id, page, s, items)
                    request = Request(url=url, callback=self.parse2, priority=2)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                        en_cate_id, en_brand_id, page - 1, s - 30)
                request.meta["_seed"] = str(Seed((cate_id, brand_id, page, s), type=2))
                yield request

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        page_strs = self.totalpage_perttern.findall(response.text)
        print(page_strs)
        if page_strs:
            page_strs = page_strs[0]
            for i in range(1, int(page_strs) + 1):
                page, s = 2 * i - 1, 60 * (i - 1) + 1
                cate_id, brand_id= seed.value
                if brand_id:
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, 2 * (i-1) - 1, 60 * (i - 2) + 1)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(en_cate_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(
                        en_cate_id, 2 * (i - 1) - 1, 60 * (i - 2) + 1)
                yield Request(url=url, callback=self.parse1, meta={"_seed": str(Seed((cate_id, brand_id, page, s), type=1)), "headers": {"Connection": "close", "Referer": refer}}, priority=1)


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
                #{"$limit": 10}
            ]
            data_set = collections.DataSet(m.read_from(db_collect=("jingdong", last_brand_collect), out_field=("cate_id", "brand_id"), pipeline=pipeline))
            #for i, seed in enumerate(data_set.distinct()):
            # for i, seed in enumerate([("737,794,798","8557")]):
            #     seed = Seed(value=seed, type=0)
            #     cate_id, brand_id = seed.value
            #     if not (cate_id == "737,794,798" and brand_id == "8557"):
            #         continue
            #     if brand_id:
            #         cid1, cid2, cid3 = re.split(',', cate_id)
            #         if cid1 == "1713":
            #             en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
            #                 {"ev": "expublishers_" + brand_id})
            #         else:
            #             en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
            #                 {"ev": "exbrand_" + brand_id})
            #         url = 'https://list.jd.com/list.html?{0}&{1}&cid3={2}&psort=4&click=1'.format(en_cate_id, en_brand_id, cid3)
            #     else:
            #         url = 'https://list.jd.com/list.html?{0}&psort=4&click=1'.format(urllib.parse.urlencode({"cat": cate_id}))
            #     data = {"url": url, "meta": {"_seed": str(seed),
            #                                  "headers": {"Referer": "https://www.jd.com/"}}}
            #     buffer.append(str(data))
            #     if len(buffer) % buffer_size == 0:
            #         self.redis.sadd(self.start_urls_redis_key, *buffer)
            #         buffer = []
            # if buffer:
            #     self.redis.sadd(self.start_urls_redis_key, *buffer)

            for i, seed in enumerate([("737,794,798","8557")]):
                seed = Seed(value=seed, type=0)
                url = None
                data = {"url": url, "meta": {"_seed": str(seed),
                                             "headers": {"Referer": "https://www.jd.com/"}}}
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdskuid{0}".format(current_date)), bar_name=self.items_redis_key)
        # thread_writer = ThreadFileWriter(redis_key=self.items_redis_key, stop_epoch=12*30, bar_name=self.items_redis_key,
        #                                  out_file="jingdong/result/jdskuid.txt",
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