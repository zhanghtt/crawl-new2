#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ctypes
import random
import threading
import time
import urllib
from io import BytesIO
from multiprocessing import Process, Value, Queue, Lock, Manager
import chardet
import pymongo
import requests
from requests.adapters import HTTPAdapter
from tqdm import tqdm
from queue import Empty


class SuccessResult(Exception):
    pass


class Counter(object):
    def __init__(self, value=0):
        self.counter = value

    def increase(self, num=1):
        self.counter = self.counter + num

    def reset_count(self):
        self.counter = 0

    def get_count(self):
        return self.counter

from ast import literal_eval


class Seed(object):

    def __init__(self, value, retries=3, type = None, last_time=time.time(), rest_time=0,
                 is_faid_task_write=True, is_ok=False, url=None, headers=None, status=0):
        self.retries = retries
        self.value = value
        self.type = type
        self.last_time = last_time
        self.rest_time = rest_time
        self.is_faid_task_write = is_faid_task_write
        self.is_ok = is_ok
        self.counter = Counter()
        self.url = url
        self.headers = headers
        self.status = status

    def __str__(self):
        return str((self.value, self.type, self.url, self.headers))

    def sleep(self, rest_time):
        self.last_time = time.time()
        self.rest_time = rest_time

    def ok(self):
        self.is_ok = True

    def fail(self):
        self.is_ok = False

    def retry(self):
        self.retries = self.retries - 1

    @classmethod
    def parse_seed(cls, str_seed):
        tmp = literal_eval(str_seed)
        return cls(value=tmp[0], type=tmp[1], url=tmp[2], headers=tmp[3])





class ThreadMonitor(threading.Thread):
    def __init__(self, total, comlete, lock, interval=1, bar_name=None, ):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.total = total
        self.comlete = comlete
        self.interval = interval
        self.bar_name = bar_name
        self.lock = lock

    def run(self):
        with tqdm(total=self.total, desc=self.bar_name) as pbar:
            last_size = 0
            while True:
                end = time.time() + self.interval
                with self.lock:
                    current_size = self.comlete.value
                pbar.update(current_size - last_size)
                if time.time() < end:
                    time.sleep(end - time.time())
                last_size = current_size


class SpiderManger(object):
    def __init__(self, spider_num, mongo_config, complete_timeout=5*60,
                 job_name=None, log_config=None, proxies_pool=None, write_buffer_size=1024, **kwargs):
        self.proxies_pool = Queue()
        for proxy in proxies_pool:
            self.proxies_pool.put(proxy)
        self.kwargs = kwargs
        self.complete_timeout = complete_timeout
        self.job_name = job_name
        self.seeds_queue = Queue()
        self.seeds_queue.cancel_join_thread()
        self.comlete = Value(ctypes.c_int, 0)
        self.lock = Lock()
        self.spider_num = spider_num
        self.mongo_config = mongo_config
        import logging
        logging.basicConfig(**log_config)
        self.log = logging
        self.log.info("output_db_collection: " + self.mongo_config["db"] + ","+ self.mongo_config["collection"])
        self.db_collect = None
        self.id = None
        self.current_proxy = None
        self.write_buffer_size = write_buffer_size

    def fetch_task(self, timeout=None):
        seed = self.seeds_queue.get(timeout=timeout)
        if seed.retries > 0:
            if time.time() - seed.last_time < seed.rest_time:
                self.log.debug("in rest_time!")
                self.seeds_queue.put(seed)
                return None
            else:
                self.log.debug("get seed success!")
                self.progress_increase()
                return seed
        else:
            self.progress_increase()
            return seed

    def progress_increase(self, step=1):
        with self.lock:
            self.comlete.value += step

    def progress_decrease(self, step=1):
        with self.lock:
            self.comlete.value -= step

    def overwrite_download_opt(self, pycurl):
        pass

    @staticmethod
    def convert_proxy_format(proxy="http://u0:crawl@192.168.0.71:3128"):
        password = proxy[proxy.find("//") + 2: proxy.find("@")]
        proxy = proxy.replace(password + "@", "")
        return proxy, password

    # def download(self, request):
    #     request_url = request.get("url")
    #     headers = request.get("headers")
    #     if isinstance(headers, dict):
    #         headers = [k+":"+v for k,v in headers.items()]
    #     proxies = request.get("proxy")
    #     mothed = request.get("mothed")
    #     encoding = request.get("encoding")
    #
    #     c = pycurl.Curl()
    #     body = BytesIO()
    #     if self.pycurl_config:
    #         #default
    #         c.setopt(pycurl.FOLLOWLOCATION, 1)
    #         c.setopt(pycurl.MAXREDIRS, 5)
    #         c.setopt(pycurl.TIMEOUT, 3)
    #         c.setopt(pycurl.CONNECTTIMEOUT, 1)
    #         c.setopt(pycurl.URL, request_url)
    #         if headers:
    #             c.setopt(pycurl.HTTPHEADER, headers)
    #         c.setopt(pycurl.ENCODING, 'gzip,deflate')
    #         c.setopt(pycurl.SSL_VERIFYPEER, False)
    #         c.setopt(pycurl.SSL_VERIFYHOST, False)
    #         if mothed is None:
    #             mothed = "get"
    #         if mothed.lower() == "post":
    #             c.setopt(pycurl.POST, 1)
    #             data = request.get("data")
    #             if data:
    #                 c.setopt(pycurl.POSTFIELDS, urllib.urlencode(data))
    #         c.setopt(pycurl.WRITEFUNCTION, body.write)
    #         if self.use_proxy:
    #             if proxies:
    #                 proxy, password = self.convert_proxy_format(proxies)
    #                 self.log.debug((proxy,password))
    #                 c.setopt(pycurl.PROXY, proxy)
    #                 c.setopt(pycurl.PROXYUSERPWD, password)
    #             else:
    #                 if self.used_proxy:
    #                     proxy, password = self.convert_proxy_format(self.used_proxy)
    #                     self.log.debug((proxy, password ))
    #                     c.setopt(pycurl.PROXY, proxy)
    #                     c.setopt(pycurl.PROXYUSERPWD, password)
    #         #set pycurl_config
    #         for k, v in self.pycurl_config.items():
    #             c.setopt(k, v)
    #         # set yourself
    #         self.overwrite_download_opt(c)
    #     else:
    #         c.setopt(pycurl.FOLLOWLOCATION, 1)
    #         c.setopt(pycurl.MAXREDIRS, 5)
    #         c.setopt(pycurl.TIMEOUT, 3)
    #         c.setopt(pycurl.CONNECTTIMEOUT, 1)
    #         c.setopt(pycurl.URL, request_url)
    #         if headers:
    #             c.setopt(pycurl.HTTPHEADER, headers)
    #         c.setopt(pycurl.ENCODING, 'gzip,deflate')
    #         c.setopt(pycurl.SSL_VERIFYPEER, False)
    #         c.setopt(pycurl.SSL_VERIFYHOST, False)
    #         if mothed is None:
    #             mothed = "get"
    #         if mothed.lower() == "post":
    #             c.setopt(pycurl.POST, 1)
    #             data = request.get("data")
    #             if data:
    #                 c.setopt(pycurl.POSTFIELDS, urllib.urlencode(data))
    #         c.setopt(pycurl.WRITEFUNCTION, body.write)
    #         if self.use_proxy:
    #             if proxies:
    #                 proxy, password = self.convert_proxy_format(proxies)
    #                 self.log.debug((proxy, password))
    #                 c.setopt(pycurl.PROXY, proxy)
    #                 c.setopt(pycurl.PROXYUSERPWD, password)
    #             else:
    #                 if self.used_proxy:
    #                     proxy, password = self.convert_proxy_format(self.used_proxy)
    #                     self.log.debug((proxy, password))
    #                     c.setopt(pycurl.PROXY, proxy)
    #                     c.setopt(pycurl.PROXYUSERPWD, password)
    #
    #         self.overwrite_download_opt(c)
    #     try:
    #         c.perform()
    #         code = c.getinfo(pycurl.HTTP_CODE)
    #         if code != 200:
    #             raise pycurl.error(code, "")
    #     except pycurl.error as err:
    #         #if err[0] not in (7,28,56):
    #          #   self.log.error(err)
    #         self.log.exception(err)
    #         #raise err
    #         return ""
    #     finally:
    #         c.close()
    #     result = body.getvalue()
    #     if not encoding:
    #         coding = chardet.detect(result)['encoding']
    #     return result.decode(coding)

    def do_request(self, request):
        #自定义参数
        sleep_time = request.get("sleep_time", 0)
        if "sleep_time" in request:
            request.pop("sleep_time")
        if sleep_time > 0:
            time.sleep(sleep_time)
        #requests参数
        max_retries = request.get("max_retries", 3)
        if not request.get("method"):
            request["method"] = 'get'
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=max_retries))
        s.mount('https://', HTTPAdapter(max_retries=max_retries))
        try:
            r = s.request(**request)
            return r
        except requests.exceptions.ProxyError as e :
            self.log.exception(e)
            old = self.current_proxy
            self.proxies_pool.put(old)
            self.current_proxy = self.proxies_pool.get()
            self.log.info("swith new proxy from {} to {}".format(old, self.current_proxy))
        except Exception as e:
            self.log.exception(e)
            return None

    def make_request(self, seed):
        pass

    def parse_item(self, content, seed):
        pass

    def process(self, seed):
        request = self.make_request(seed)
        respone = self.do_request(request)
        print(respone.text)
        if respone and respone.status_code == requests.codes.ok:
            if respone.text:
                self.parse_item(respone.text, seed)

    # def process(self, seed):
    #     try:
    #         request_dict = self.make_request(seed)
    #     except Exception as e:
    #         self.log.exception(e)
    #         request_dict = None
    #         seed.retries = seed.retries - 1
    #         if seed.retries > 0:
    #             if self.rest_time:
    #                 time.sleep(self.rest_time)
    #             self.seeds_queue.put(seed)
    #             self.progress_decrease()
    #         else:
    #             return [{"_status": 3, "_seed": seed}]
    #     if request_dict:
    #         if self.use_new_download_api:
    #             content = self.download(request_dict)
    #         else:
    #             content = self.do_request(request_dict)
    #         if content == "":
    #             seed.retries = seed.retries - 1
    #             if seed.retries > 0:
    #                 if self.rest_time:
    #                     time.sleep(self.rest_time)
    #                 self.seeds_queue.put(seed)
    #                 self.progress_decrease()
    #                 #失败后切换代理
    #                 #self.used_proxy = random.choice(self.proxies_pool)
    #                 #return [{"_status": 3,"_seed":seed}]
    #             else:
    #                 return [{"_status": 1,"_seed": str(seed)}]
    #         else:
    #             try:
    #                 result = self.parse_item(content, seed)
    #                 if result:
    #                     if isinstance(result, list):
    #                         result = list(map(lambda x: dict(list(x.items()) + [("_status", 0), ("_seed",str(seed))]),
    #                                           result))
    #                         return result
    #                     else:
    #                         result.update({"_status":0,"_seed":str(seed)})
    #                         return [result]
    #                 else:
    #                     return [{"_status": 4, "_seed": str(seed)}]
    #             except Exception as e:
    #                 return [{"_status": 2, "_seed": str(seed)}]

    def run(self, id):
        self.id = id
        self.current_proxy = self.proxies_pool.get()
        self.log.info((self.id,self.current_proxy))
        client = pymongo.MongoClient(self.mongo_config["addr"])
        self.db_collect = client[self.mongo_config["db"]][self.mongo_config["collection"]]
        self.write_buffer = []
        while True:
            try:
                seed = self.fetch_task(self.complete_timeout)
            except Empty as e:
                self.log.exception(e)
                self.log.info("fetch task over time {}, spider will shutdown normally!")
                self.flush()
                break
            except Exception as e:
                self.log.exception(e)
                continue
            try:
                if seed:
                    if seed.retries <= 0:
                        self.log.debug("seed {} failed!".format(str(seed)))
                        if seed.is_faid_task_write:
                            self.write([{"_status": 3, "_seed": seed.value}])
                    else:
                        #待处理的seed默认是fail的
                        seed.fail()
                        self.process(seed)
                        if not seed.is_ok:
                            self.log.debug("seed {} retry!".format(str(seed)))
                            seed.retry()
                            seed.sleep(self.kwargs.get("rest_time", 3))
                            self.seeds_queue.put(seed)
                            self.progress_decrease()
            except Exception as e:
                if not seed.is_ok:
                    self.log.debug("seed {} retry!".format(str(seed)))
                    seed.retry()
                    seed.sleep(self.kwargs.get("rest_time", 3))
                    self.seeds_queue.put(seed)
                    self.progress_decrease()
                self.log.exception(e)

    # def write(self, documents, buffer_size=1024):
    #     if len(self.write_buffer) % buffer_size == 0:
    #         for doc in  documents:
    #             if doc.get("_status") is None:
    #                 doc["_status"] = 0
    #         self.db_collect.insert_many(documents)

    def write(self, documents, immdeately=False):
        if isinstance(documents, list):
            self.write_buffer.extend(documents)
        elif isinstance(documents, dict):
            self.write_buffer.append(documents)
        if immdeately or len(self.write_buffer) % self.write_buffer_size == 0:
            self.flush()

    def flush(self):
        if self.write_buffer:
            for doc in self.write_buffer:
                if doc.get("_status") is None:
                    doc["_status"] = 0
            self.db_collect.insert_many(self.write_buffer)
            self.write_buffer = []

    def main_loop(self, show_process=True):
        if show_process:
            m = ThreadMonitor(self.seeds_queue.qsize(), self.comlete, lock=self.lock, bar_name="进度")
            m.start()

        if self.spider_num > 1:
            self.spider_list = []
            for i in range(self.spider_num):
                self.spider_list.append(Process(target=self.run, name="Spider-" + str(i), kwargs={"id": i}))
            for p in self.spider_list:
                p.start()
            for p in self.spider_list:
                p.join()
        else:
            if self.spider_num == 1:
                self.run(id=0)
