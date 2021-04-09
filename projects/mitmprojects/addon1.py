#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mitmproxy import ctx
import mitmproxy
import re
pattern1 = re.compile("/api/c/poi/\d+/sku/(\d+)/detail/v6")

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.method == "GET" and flow.request.host == 'bi-mall.meituan.com' and pattern1.findall(flow.request.path):
            old_skuid = pattern1.findall(flow.request.path)[0]
            newpath = flow.request.path.replace(old_skuid,'100056103480311')
            oldpath = flow.request.path
            print(oldpath)
            print(newpath)
            flow.request.path = newpath
            flow.request.query.set_all('skuId',['100056103480311'])

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.method == "GET" and flow.request.host == 'bi-mall.meituan.com' and pattern1.findall(flow.request.path):
            print(flow.response.text)



addons=[Counter()]