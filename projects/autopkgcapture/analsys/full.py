#!/usr/bin/env python
# -*- coding: utf-8 -*-
a=open("1_Full.txt", 'rb').read()
out = open("full_result.csv",'w')
import re
p=re.compile('"sku_id":(\d+).*?"supplier_id":(\d+)',re.S)
import json
import traceback
with open("C:\\Users\\admin\\Documents\\WeChat Files\\djc421798321\\FileStorage\\File\\2021-04\\橙心北京sku&supplierid.chlsj", 'r',encoding="utf8") as readObj:
    harDirct = json.loads(readObj.read())
    count = 0
    count1 = 0
    s = set()
    for session in harDirct:
        try:
            item = json.loads(session["response"]["body"]["text"])
            tmp = [item['data']["goods_name"],item['data']["category_name"],item['data']["supplier_id"],
                  item['data']["stock"][0]['goods_id'],item['data']["stock"][0]['line_price'],item['data']["stock"][0]['price']
            , item['data']["stock"][0]['cost_price'],item['data']["stock"][0]['sku_id'],item['data']['attribute'][0]["licenseImgs"][0]]
            s.add(item['data']["supplier_id"])
            res = ','.join([str(i) for i in tmp])+'\n'
            print(res)
            out.write(res)
            count = count + 1
        except:
            traceback.print_exc()
            pass
    print(count,count1,len(s))

