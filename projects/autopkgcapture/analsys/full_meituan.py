#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=open("1_Full.txt", 'rb').read()
out = open("full_result_meituan_supplierid.csv",'w',encoding='utf8')
import re
p=re.compile('"sku_id":(\d+).*?"supplier_id":(\d+)',re.S)
import json
import traceback
import requests
import gzip
import base64
import chardet
with open("C:\\Users\\admin\\Documents\\WeChat Files\\djc421798321\\FileStorage\\File\\2021-04\\美团优选北京sku&supplierid.chlsj", 'r',encoding="utf8") as readObj:
    harDirct = json.loads(readObj.read())
    count = 0
    count1 = 0
    s = set()
    import re
    p = re.compile("supplierId=(\d+)",re.S)
    for session in harDirct:
        try:
            content = base64.b64decode(
                session["response"]["body"]["encoded"])
            data = gzip.decompress(content).decode("utf-8")
            item = json.loads(data)["data"]
            #tmp = [item['skuId'],item['skuTitle']['text'],item['firstCategoryName'],item['dashPrice']['text'],item['sellPrice']['text'],p.findall(data)[0]]
            tmp = [item['skuId'],item['skuTitle']['text'],item['firstCategoryName'] if item.get('firstCategoryName') else None ,item['dashPrice']['text'],item['sellPrice']['text'],p.findall(data)[0]]
            res = ','.join([str(i) for i in tmp])+'\n'
            out.write(res)
            count = count + 1
        except:
            #traceback.print_exc()
            pass
    print(count,count1,len(s))

out1 = open("full_result_meituan_skuid.csv",'w',encoding='utf8')
with open("C:\\Users\\admin\\Documents\\WeChat Files\\djc421798321\\FileStorage\\File\\2021-04\\美团优选北京地区sku列表1.chlsj", 'r',encoding="utf8") as readObj:
    harDirct = json.loads(readObj.read())
    count = 0
    count1 = 0
    s = set()
    import re
    p = re.compile("supplierId=(\d+)",re.S)
    for session in harDirct:
        try:
            content = base64.b64decode(
                session["response"]["body"]["encoded"])
            data = gzip.decompress(content).decode("utf-8")
            for item in json.loads(data)["data"]['itemList']:
                item = item['skuItem']
                #tmp = [item['skuId'],item['skuTitle']['text'],item['sales']['text']]
                tmp = [item['skuId'],item['skuTitle']['text'],item.get('sales')['text'] if item.get('sales') else None]
                res = ','.join([str(i) for i in tmp])+'\n'
                out1.write(res)
                count = count + 1
        except:
            pass
    print(count,count1,len(s))

