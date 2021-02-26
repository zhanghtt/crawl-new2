#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import chardet
from  io import BytesIO
import re
def download(request):
    request_url = request.get("url")
    headers = request.get("headers")
    if isinstance(headers, dict):
        headers = [k + ":" + v for k, v in headers.items()]
    proxies = request.get("proxies")
    mothed = request.get("mothed")

    c = pycurl.Curl()
    body = BytesIO()
    c.setopt(pycurl.VERBOSE, True)
    c.setopt(pycurl.HEADER, False)
    c.setopt(pycurl.TIMEOUT, 3)
    c.setopt(pycurl.CONNECTTIMEOUT, 1)
    c.setopt(pycurl.URL, request_url)
    if headers:
        print(headers)
        c.setopt(pycurl.HTTPHEADER, headers)
    c.setopt(pycurl.ENCODING, 'gzip,deflate')
    c.setopt(pycurl.SSL_VERIFYPEER, False)
    c.setopt(pycurl.SSL_VERIFYHOST, False)
    if mothed is None:
        mothed = "get"
    if mothed.lower() == "post":
        c.setopt(pycurl.POST, 1)
        data = request.get("data")
        if data:
            c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.WRITEFUNCTION, body.write)
    if proxies:
        proxy, password = convert_proxy_format(proxies)
        c.setopt(pycurl.PROXY, proxy)
        c.setopt(pycurl.PROXYUSERPWD, password)
    try:
        c.perform()
        code = c.getinfo(pycurl.RESPONSE_CODE)
        content = c.getinfo(pycurl.CONTENT_TYPE)
        if code != 200:
            raise pycurl.error(code, "")
    except pycurl.error as err:
        print(repr(err))
        raise err
    finally:
        c.close()
    return body.getvalue().decode("gbk")

def convert_proxy_format(proxy="http://u0:crawl@192.168.0.71:3128"):
    password = proxy[proxy.find("//") + 2: proxy.find("@")]
    proxy = proxy.replace(password + "@", "")
    return proxy, password
import requests
from multiprocess.core.HttpProxy import getHttpProxy
# for proxy in getHttpProxy():
#     request = {"url": "https://www.baidu.com/s?wd=ip",
#                        "proxies": {"http":proxy},
#                        "headers":{
#              'Connection': 'close',
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#             }}
#
#
#     first_pettern = re.compile(r'<span class="c-gap-right">本机IP:&nbsp;(.*?)</span>',re.MULTILINE)
#     print((proxy,first_pettern.findall(requests.get(**request))))
request = {"url": "https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&psort=4&page=2&s=31&scrolling=y&log_id=1596108547754.6591&tpl=1_M&isList=1&show_items=1187321,1176773,1176807,1176776,1176800,1664380,1176781,1176777,924867,1176799,1071948084,1071948083,1420002797,1071948085,15275770246,1420002795,1420002798,15073327323,15275770245,11045835368,1071948082,1420002796,29768462743,46596822961,41749986737,1420002794",
           "headers": {
               'Connection': 'close',
               "Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}
request1 = {"url": "https://api03.6bqb.com/jd/goods/comment?apikey=11187001536",
           "headers": {
               'Connection': 'close',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer":"https://www.jd.com",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}
request = {"url": "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku=100001550349&sorttype=6&page=51",
           "headers": {
               'Connection': 'close',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer": "https://item.m.jd.com/100000006005.html",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}
request = {"url": "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku=57160888695&sorttype=6&page=90",
           "headers": {
               'Connection': 'keep-alive',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer": "https://item.m.jd.com/100000006005.html",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}
request = {"url": "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku=10020785876486&sorttype=6&page=0",
           "headers": {
               'Connection': 'keep-alive',
               'Host':'wq.jd.com',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer": "https://item.m.jd.com/72321801855.html",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
               #"cookie":"shshshfpa=230b299e-b267-3f39-748a-5274ba04573e-1526388430; shshshfpb=0e4a63e00c3146f1205679ecef0af468fb452b7038a3edfd15afad6d12; __jdu=1595213903005116662704; pin=jd_49e6f74229a5c; unick=jd_188014ctk; _tp=f8skMf7S6k8VPMVjjhCn8S7vk6UqsuFMW8o68xx3ddc%3D; _pst=jd_49e6f74229a5c; ipLocation=%u5317%u4eac; pinId=CL2LG1jQi0fBGlwodztkXrV9-x-f3wj7; unpl=V2_ZzNtbRAFShd8AUZWfk0IB2JTRwgSBxBBfAtGUHseXFFkCxINclRCFnQURldnG1wUZwQZWUNcRhJFCEdkeB5fA2AFEFlBZxBFLV0CFi9JH1c%2bbRpdS1BKFnQLRlZLKV8FVwMTbUJTSxF2CERcehtdBGMDElpFUEATdA12ZHwpbDVjCxVUQVdzFEUJdhYvRVsNbwAaWw9XRx1xC0ZWcxheBGYHEl1FUEQWcwlDZHopXw%3d%3d; __jdv=76161171|direct|-|none|-|1609750532540; TrackID=14z86bRECmD_c8hnyUzWqPbiv0pHgxgGJ0tgMH9b8UmBPkuTndrN5VhNCH5t8h3LTmlYuJbzhHXbftdRKDtXKBnPgOEXXzqhXAH9ZY-6s5MAR2ncnCvnEbToPqbFrYgEt; user-key=43a6e8ea-993d-49e9-8763-4e756d81ae6f; cn=0; PCSYCityID=CN_110000_110100_110105; areaId=1; ipLoc-djd=1-72-55653-0; wxa_level=1; jxsid=16109508048628837173; webp=1; visitkey=31014972499970792; __jda=122270672.1595213903005116662704.1595213903.1610948455.1610955353.123; __jdc=122270672; 3AB9D23F7A4B3C9B=HV7XTTHFGASMIJRSRKK34KLHMYELLS47K4NBCIR2PEFYCZUMIX225JHQCMEJUTEKYFDA47E3QEMFC3TYKKQRYXFS2Q; shshshfp=8e6807b1ccf37dd2a527f63ee133d3e6; shshshsID=48908f8b4d08dd6a4ad6ea045c548f30_2_1610955836722; wq_logid=1610955927.1063071573; retina=1; cid=9; wqmnx1=MDEyNjM4NHMubXQxMzQyL25yOzVNQUszTEdoLjFsaTFzZjQyRUgmUg%3D%3D; __jdb=122270672.12.1595213903005116662704|123.1610955353; mba_muid=1595213903005116662704; mba_sid=16109559266537842608963232693.1"
           }}
cate_pattern = re.compile(r'navThird[1-9]: (\[.*\])')
cate_pattern1 = re.compile(r'<li data-sku="(\d+)"[\s\S]*?class="gl-item">[\s\S]*?<em>([^￥][\s\S]*?)</em>[\s\S]*?</li>')
first_pettern = re.compile(r"search000014_log:{wids:'([,\d]*?)',")
comments_pattern = re.compile(r'"comments":[\s\S]*?(\[[\s\S]*\])')
allcnt_pattern = re.compile(r'"CommentCount": \"(\d+)\",')
import json
import time
from ast import literal_eval
import json
from fake_useragent import UserAgent
ua = UserAgent()
#,proxies={"https": "https://u0:crawl@192.168.0.71:3128","http": "http://u0:crawl@192.168.0.71:3128"}
count = 0
begincout = 0
isbegin = False
import random
for i in range(10000):
    delay = random.random() + 0.5
    print(i, begincout, count, delay)
    time.sleep(delay)
    src = requests.get(**request,proxies={"http": "http://u0:crawl@192.168.0.71:3128"})
    #src = requests.get(**request)
    rsl = allcnt_pattern.findall(src.text)
    if rsl:
        count += 1
    else:
        if not isbegin:
            begincout += 1
            isbegin = True
# first_pettern = re.compile(r"search000014_log:{wids:'([,\d]*?)',")
# shopid_pettern = re.compile(r'shopId:\'(\d*)\',')
# venderid_pettern = re.compile(r'venderId:(\d*),')
# brand_pettern = re.compile(r'brand: (\d*),')
# skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
# shop_name_pettern = re.compile(r'target="_blank" title="(\S*?)" clstag="shangpin')
# ziying_pettern = re.compile(r'<div class="contact fr clearfix">[\s]*?<div class="name goodshop EDropdown">[\s]*?<em class="u-jd">[\s]*?(\S*?)[\s]*?</em>[\s]*?</div>')
# cat_pettern = re.compile(r'cat: \[([,\d]*)\],')
# phonenum=re.compile(r'<div class="locate_text">[\s]*?<div class="upper_text">(.*?) (.*?)</div>[\s]*?<div class="upper_text">手机号码: (\d.*?)</div>[\s]*?</div>')
# print(shopid_pettern.findall(src))
# print(venderid_pettern.findall(src))
# print("brand:" + brand_pettern.findall(src)[0])
# print(skuids_pettern.findall(src))
# print(shop_name_pettern.findall(src))
# print(ziying_pettern.findall(src))
# print(cat_pettern.findall(src))
# print(first_pettern.findall(src))
# print(phonenum.findall(src))


import time
# toc = time.time()
# for i in range(0, 10000, 100):
#     request = {
#         "url": "https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083&_=1597758342897".format(",".join(map(lambda x: str(x), range(i, i+100)))),
#         "headers": {
#             'Connection': 'close',
#             # "Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
#             "Referer": "https://www.jd.com",
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
#         }}
#     src = requests.get(**request).text
#     jsonr = json.loads(re.compile(r"(\[.*?\])").findall(src)[0])
#     print(i, len(jsonr))
# print(time.time() - toc)
def run():
    toc = time.time()
    for i in range(0, 10000, 100):
        request = {
            "url": "https://chat1.jd.com/api/checkChat?pidList={0}&callback=jQuery8117083&_=1597758342897".format(
                ",".join(map(lambda x: str(x), range(i, i + 100)))),
            "headers": {
                'Connection': 'keep-alive',
                # "Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
                "Referer": "https://www.jd.com",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            }}
        src = requests.get(**request).text
        jsonr = json.loads(re.compile(r"(\[.*?\])").findall(src)[0])
        #print(i, len(jsonr))
    print(time.time() - toc, len(jsonr))
import threading
class Manger:
    def __init__(self,num=10):
        self.runners = [threading.Thread(target=run) for i in range(num)]

    def run(self):
        [r.start() for r in self.runners]
        [r.join() for r in self.runners]

# m = Manger(8)
# m.run()