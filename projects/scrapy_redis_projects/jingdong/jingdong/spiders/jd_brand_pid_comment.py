#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from multiprocess.scrapy_redis.spiders import JiChengSpider, Request
from mongo import op
from multiprocess.core.spider import Seed
from scrapy_redis.utils import bytes_to_str
import urllib
import json


class Spider(JiChengSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'jd_brand_pid_comment'
    pattern = re.compile(r'<li id="brand-(\d+)[\s\S]*?品牌::([\s\S]*?)\'\)"')
    allcnt_pattern = re.compile(r'"commentCount":(\d+),')
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
    json_pettern = re.compile(r"(\[.*?\])")

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        obj = super(Spider, cls).from_crawler(crawler, *args, **kwargs)
        return obj

    def make_request_from_data(self, data):
        str_seed = bytes_to_str(data, self.redis_encoding)
        seed = Seed.parse_seed(str_seed)
        if seed.status == 0:
            cats = re.split(',', seed.value)
            format_value = (seed.value, 2, "pub") if cats[0] == '1713' else (seed.value, 1, "brand")
            url = 'https://list.jd.com/list.html?cat={0}&trans=1&md={1}&my=list_{2}'.format(*format_value)
            return Request(url=url, meta={"_seed": str_seed}, priority=0, callback=self.parse, headers={"Referer": "https://www.jd.com/"})
        elif seed.status == 3:
            str_seed = seed.value
            request = Request.deserialize(str_seed, self)
            return request

    def parse(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        if response.text.find("""<span class="result">抱歉，没有找到与“<em></em>”相关的商品</span>""") != -1:
            # 不存在的分类
            yield {"cate_id": seed.value, "_seed": seed.value, "_status": -1}
        tuples = self.pattern.findall(response.text)
        if len(tuples) > 0:
            for item in tuples:
                cate_id = seed.value
                brand_id = item[0]
                brand_name = item[1]
                seed = Seed(value=(cate_id, brand_id, brand_name))
                cate_id, brand_id, _ = seed.value
                cid1, cid2, cid3 = re.split(',', cate_id)
                if cid1 == "1713":
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                        {"ev": "expublishers_" + brand_id})
                else:
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode(
                        {"ev": "exbrand_" + brand_id})
                url = 'https://list.jd.com/list.html?{0}&{1}&cid3={2}&psort=4&click=1'.format(en_cate_id, en_brand_id,
                                                                                              cid3)
                yield Request(url=url, meta={"_seed": str(seed), "headers": {"Referer": "https://www.jd.com/"}},
                               priority=0, callback=self.parse1)
        else:
            #没有品牌的分类
            cate_id = seed.value
            brand_id = None
            brand_name = None
            seed = Seed(value=(cate_id, brand_id, brand_name))
            url = 'https://list.jd.com/list.html?{0}&psort=4&click=1'.format(urllib.parse.urlencode({"cat": cate_id}))
            yield Request(url=url, meta={"_seed": str(seed), "headers": {"Referer": "https://www.jd.com/"}},
                           priority=0, callback=self.parse1)

    def parse5(self, response):
        count = self.allcnt_pattern.findall(response.text)
        if not count:
            result = response.meta["data"]
            result["comment"]=0
            yield result
        else:
            result = response.meta["data"]
            result["comment"] = count[0]
            yield result

    def parse4(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, page, s, brand_name = seed.value
        for item in json.loads(self.json_pettern.findall(response.text)[0]):
            if item:
                data = {"pid": item.get("pid"), "cate_id": cate_id, "brand_id": brand_id, "shopid": item.get("shopId"),
                       "venderid": item.get("venderId", None), "shop_name": item.get("seller"),
                       "ziying": 1 if item.get("seller") and item.get("seller").find("京东自营") != -1 else 0 }
                print(Request(url="https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                      "&productId={0}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1".format(data["pid"])
                              , callback=self.parse5, meta={"_seed": response.meta["_seed"], "data":data}, priority=5,
                              headers={"Referer": "https://item.jd.com/{0}.html".format(data["pid"])}))
                yield Request(url="https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98" \
                      "&productId={0}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1".format(data["pid"])
                              , callback=self.parse5, meta={"_seed": response.meta["_seed"], "data":data}, priority=5,
                              headers={"Referer": "https://item.jd.com/{0}.html".format(data["pid"])})

    def parse3(self, response):
        last_page_pids = response.meta["last_page_pids"]
        if response.text.find("""<span class="result">抱歉，没有找到与“<em></em>”相关的商品</span>""") != -1:
            # 说明没有下半页
            yield Request(
                url="https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083".format(last_page_pids),
                callback=self.parse4, meta={"_seed": response.meta["_seed"]}, priority=4)
        else:
            r1 = self.first_pettern.findall(response.text)
            print(r1)
            if r1:
                r1 = r1[0]
                if r1:
                    yield Request(url="https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083".format(last_page_pids + "," + r1), callback=self.parse4, meta={"_seed": response.meta["_seed"]}, priority=4)

    def parse2(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        cate_id, brand_id, page, s, brand_name = seed.value
        print(seed.value)
        r1 = self.first_pettern.findall(response.text)
        if r1:
            r1 = r1[0]
            if r1:
                cate_id, brand_id, page, s, items = cate_id, brand_id, page + 1, s + 30, r1
                if brand_id:
                    en_cate_id, en_brand_id = urllib.parse.urlencode(
                        {"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&psort=4&page={2}&s={3}&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={4}'.format(
                        en_cate_id, en_brand_id, page, s, items)
                    request = Request(url=url, callback=self.parse3, priority=3)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1".format(
                        en_cate_id, en_brand_id, page-1, s-30)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&psort=4&page={1}&s={2}&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items={3}'.format(
                        en_cate_id, page, s, items)
                    request = Request(url=url, callback=self.parse3, priority=3)
                    request.headers["Referer"] = "https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1".format(
                        en_cate_id, page - 1, s - 30)
                request.meta["_seed"] = str(Seed(value=(cate_id, brand_id, page, s, brand_name), type=2))
                request.meta["last_page_pids"] = r1
                yield request

    def parse1(self, response):
        seed = Seed.parse_seed(response.meta["_seed"])
        page_strs = self.totalpage_perttern.findall(response.text)
        if page_strs:
            page_strs = page_strs[0]
            for i in range(1, int(page_strs) + 1):
                page, s = 2 * i - 1, 60 * (i - 1) + 1
                cate_id, brand_id, brand_name = seed.value
                if brand_id:
                    en_cate_id, en_brand_id = urllib.parse.urlencode({"cat": cate_id}), urllib.parse.urlencode({"ev": "exbrand_" + brand_id})
                    url = 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, page, s, brand_name)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&{1}&page={2}&s={3}&psort=4&click=1'.format(en_cate_id, en_brand_id, 2 * (i-1) - 1, 60 * (i - 2) + 1)
                else:
                    en_cate_id = urllib.parse.urlencode({"cat": cate_id})
                    url = 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(en_cate_id, page, s)
                    refer = "https://www.jd.com/" if i == 1 else 'https://list.jd.com/list.html?{0}&page={1}&s={2}&psort=4&click=1'.format(
                        en_cate_id, 2 * (i - 1) - 1, 60 * (i - 2) + 1)
                yield Request(url=url, callback=self.parse2, meta={"_seed": str(Seed(value=(cate_id, brand_id, page, s, brand_name), type=1))}, headers={"Connection": "close", "Referer": refer}, priority=2)


from multiprocess.scrapy_redis.spiders import ClusterRunner,ThreadFileWriter, ThreadMonitor,Master,Slaver,ThreadMongoWriter
from multiprocess.tools import collections, timeUtil
from multiprocess.core.HttpProxy import getHttpProxy,getHttpsProxy
current_date = timeUtil.current_time()


class FirstMaster(Master):
    def __init__(self, *args, **kwargs):
        super(FirstMaster, self).__init__(*args, **kwargs)

    def init_proxies_queue(self, proxies=getHttpProxy()):
        super(FirstMaster, self).init_proxies_queue(proxies=proxies)

    def init_start_urls(self):
        self.redis.delete(self.start_urls_redis_key)
        self.redis.delete(self.items_redis_key)
        buffer_size = 1024
        with op.DBManger() as m:
            with open("jingdong/resource/newCateName",encoding="utf-8") as infile:
                buffer=[]
                data_set = collections.DataSet(infile)
                # for i, seed in enumerate(data_set.map(lambda line: line.strip('\n').split("\t")[0].replace('-', ','))
                #                                  .shuffle(1024)):
                for i , seed in enumerate(["4051,4059,4140"]):
                    seed = Seed(value=seed, status=0)
                    buffer.append(str(seed))
                    if len(buffer) % buffer_size == 0:
                        self.redis.sadd(self.start_urls_redis_key, *buffer)
                        buffer = []
                if buffer:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*3000,buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong","jdbrandpidcomment{0}".format(current_date)), bar_name=self.items_redis_key, distinct_field="pid")
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


class RetryMaster(FirstMaster):
    def __init__(self, *args, **kwargs):
        super(RetryMaster, self).__init__(*args, **kwargs)
        with op.DBManger() as m:
            self.last_retry_collect = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdbrandpidcomment20\d\d\d\d\d\d(retry\d+)?$"}})
            self.new_retry_collect = self.last_retry_collect[:self.last_retry_collect.find("retry") + 5] + str(int(self.last_retry_collect[self.last_retry_collect.find("retry") + 5:]) + 1) if self.last_retry_collect.find("retry") != -1 else self.last_retry_collect+"retry1"
            self.logger.info((self.last_retry_collect, self.new_retry_collect))

    def get_thread_writer(self):
        thread_writer = ThreadMongoWriter(redis_key=self.items_redis_key, stop_epoch=12*30, buffer_size=2048,
                                          out_mongo_url="mongodb://192.168.0.13:27017",
                                          db_collection=("jingdong", self.new_retry_collect), bar_name=self.items_redis_key, distinct_field="pid")
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
            for i, (seed, status) in enumerate(data_set.distinct()):
                seed = Seed(value=seed, status=status)
                buffer.append(str(seed))
                if len(buffer) % buffer_size == 0:
                    self.redis.sadd(self.start_urls_redis_key, *buffer)
                    buffer = []
            if buffer:
                self.redis.sadd(self.start_urls_redis_key, *buffer)


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
