#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pycurl
import chardet
from  io import BytesIO
import re
from fake_useragent import UserAgent
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
request = {"url": "https://wq.jd.com/commodity/comment/getcommentlist?callback=fetchJSON_comment98&pagesize=10&sceneval=2&skucomment=1&score=0&sku=57160888695&sorttype=6&page=0",
           "headers": {
               'Connection': 'keep-alive',
               #"Referer":"https://list.jd.com/list.html?cat=4938%2C11760%2C12282&ev=exbrand_7575&page=1&s=1&psort=4&click=1",
               "Referer": "https://item.m.jd.com/100000006005.html",
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           }}
request = {"url": "https://wq.jd.com/commodity/comment/getcommentlist?callback=skuJDEvalB&version=v2&pagesize=10&sceneval=2&skucomment=1&score=0&sku=51963222491&sorttype=6&page=1&t=0.5156075450518778",
           "headers": {
               'Connection': 'keep-alive',
               'Host':'wq.jd.com',
               "Referer": "https://item.m.jd.com/ware/view.action?wareId=51963222491&sid=null",
               'User-Agent': 'Mozilla/5.0 (Linux; Android 10; HRY-AL00a; HMSCore 5.1.1.303) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.7.303 Mobile Safari/537.36',
               #"cookie":"__jdc=122270672; mba_muid=16087105855231456793479; shshshfpa=b86c237d-b506-9cc9-730d-39db2f5ea48c-1608710586; shshshfpb=aW2xjA0PZevBiTvJrQ6rk4A%3D%3D; retina=1; webp=1; visitkey=31140776387466944; sbx_hot_h=null; deviceVersion=83.0.4103.106; deviceOS=android; deviceOSVersion=10; deviceName=Chrome; rurl=https%3A%2F%2Fwqs.jd.com%2Ffaqs%2Findex.html%3Fsceneval%3D2%26ptag%3D7001.1.124%26productId%3D12991458%26ispg%3D%26_fd%3Djdm%26jxsid%3D16109541564584400343; equipmentId=A75Q6PQS36IHI62HBEUGC44IVLERE7257UWVYTGEXPMR6NOKARSVVF2Q6EBPSVGNR537LK6GQN3ENW47JREOEXNAVI; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1614224630058; sc_width=360; shshshfp=c6774e911e47825ddd51cefc23f9b157; wxa_level=1; cid=9; jxsid=16145705280303310338; __jda=122270672.16087105855231456793479.1608710585.1614224630.1614570529.10; wq_ug=14; fingerprint=794164a430090764096f40466260c718; mt_xid=V2_52007VwMVU1ReUlsbQB1YBmUDF1ZaXlpYGk8RbFVuBEBVWV9RRkhIGw4ZYlcRWkFQWwlIVR5aAjAAR1BZX1tZHnkaXQZnHxNQQVlSSx9JElgFbAEbYl9oUmoXSB5dDWYKE1BZXlNeF08cVQNvMxJbWV8%3D; wq_logid=1614571192.282863947; wqmnx1=MDEyNjM5M3AuL3d3MiY2NjQ1eGQtTTFBaSBsby8zd3IzZTUyNy00UkghKQ%3D%3D; __jdb=122270672.9.16087105855231456793479|10.1614570529; mba_sid=16145705290954323095988279117.9; __wga=1614571199267.1614570547761.1614225998734.1610954174749.5.6; PPRD_P=UUID.16087105855231456793479-LOGID.1614571199300.300139660; jxsid_s_t=1614571199496; jxsid_s_u=https%3A//item.m.jd.com/ware/view.action; sk_history=70241615154%2C101609%2C615036%2C54761686610%2C1399903%2C10024515889185%2C10381689654%2C12991458%2C100010062010%2C58070892025%2C100007627009%2C; shshshsID=e45b3b58ca53b7ab42489de6ebc02d6b_5_1614571200418"
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
ua = UserAgent()
for i in range(10000):
    #delay = random.random()
    delay = 2.5
    print(i, begincout, count, delay)
    time.sleep(delay)
    #request['headers']['User-Agent'] = ua.chrome
    src = requests.get(**request,proxies={"https": "https://u2:crawl@192.168.0.76:3128","http": "http://u2:crawl@192.168.0.76:3128"})
    #src = requests.get(**request)
    rsl = allcnt_pattern.findall(src.text)
    print(rsl)
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