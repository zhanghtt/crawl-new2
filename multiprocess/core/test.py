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
request = {"url": "https://chat1.jd.com/api/checkChat?pidList=100000002686,2,100013116298,1999899692,72276507174,19999997645,1999899692,100000002015,100000002686,200134637813&callback=jQuery8117083",
           "headers": {
               'Connection': 'close',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer":"https://www.jd.com",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}

request = {"url": "https://haoma.baidu.com/phoneSearch?search=13963063094",
           "headers": {
               'Connection': 'close',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer":"https://www.secoo.com",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}

src=requests.get(**request).text
print(src)
first_pettern = re.compile(r"search000014_log:{wids:'([,\d]*?)',")
shopid_pettern = re.compile(r'shopId:\'(\d*)\',')
venderid_pettern = re.compile(r'venderId:(\d*),')
brand_pettern = re.compile(r'brand: (\d*),')
skuids_pettern = re.compile(r'{.*?"skuId":(\d+).*?}')
shop_name_pettern = re.compile(r'target="_blank" title="(\S*?)" clstag="shangpin')
ziying_pettern = re.compile(r'<div class="contact fr clearfix">[\s]*?<div class="name goodshop EDropdown">[\s]*?<em class="u-jd">[\s]*?(\S*?)[\s]*?</em>[\s]*?</div>')
cat_pettern = re.compile(r'cat: \[([,\d]*)\],')
phonenum=re.compile(r'<div class="locate_text">[\s]*?<div class="upper_text">(.*?) (.*?)</div>[\s]*?<div class="upper_text">手机号码: (\d.*?)</div>[\s]*?</div>')
print(shopid_pettern.findall(src))
print(venderid_pettern.findall(src))
print(brand_pettern.findall(src))
print(skuids_pettern.findall(src))
print(shop_name_pettern.findall(src))
print(ziying_pettern.findall(src))
print(cat_pettern.findall(src))
print(first_pettern.findall(src))
print(phonenum.findall(src))


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