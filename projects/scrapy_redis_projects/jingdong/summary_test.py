#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import logging
logger = logging.getLogger(__name__)
import re
price_pattern = re.compile(r'^\d+\.\d\d$')
from multiprocess.tools import timeUtil
from jingdong.Tools import format_cat_id
current_date = timeUtil.current_time()
price_pattern = re.compile(r'^\d+\.\d\d$')

def clean_price(item):
    price_tmp = []
    for key in item:
        current_value = str(item[key])
        str_price_list = price_pattern.findall(current_value)
        if str_price_list and str_price_list[0] != "-1.00":
            price_tmp.append(float(str_price_list[0]))
    if price_tmp:
        price = min(price_tmp)
    else:
        price = 79.90
    return price


def run_result():
    with op.DBManger() as m:
        skuid_sukid_dict = {}
        #last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep"}})
        #for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20201214_sep"}})
        for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20201214)retry\d*$"}}):
            if not last_sep or table > last_sep:
                print("step 3: processing {}".format(table), flush=True)
                pipeline = [
                    {
                        "$match": {"_status": 0}
                    },
                    {
                        "$project": {
                            "skuid": "$skuid",
                            "cate_id": "$cate_id",
                            "brand_id": "$brand_id",
                            "ziying": "$ziying",
                        }
                    },
                ]
                for skuid, cate_id, brand_id, ziying in m.read_from(db_collect=("jingdong", table), out_field=("skuid","cate_id","brand_id","ziying"), pipeline=pipeline):
                    skuid_sukid_dict[int(skuid)]={"cate_id":cate_id,"brand_id": "0" if brand_id is None else brand_id,"ziying":ziying}

        #last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20\d\d\d\d\d\d_sep"}})
        #for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20\d\d\d\d\d\d)retry\d*$"}}):
        count = 0
        count1 = 0
        a = set()
        b = set()

        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20201218_sep"}})
        for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20201218)retry\d*$"}}):
            if not last_sep or table > last_sep:
                print("step 4: processing {}".format(table), flush=True)
                pipeline = [
                    {
                        "$match": {
                            #"$and": [{"_status": 0}, {"comment": {"$gt": 0}}]
                            "$and": [{"_status": 0}, {"comment": {"$gt": "0"}}]
                        }
                    },
                    {
                        "$project": {
                            "skuid": "$skuid",
                            "comment": "$comment",
                        }
                    },
                ]
                for skuid, comments in m.read_from_yield(db_collect=("jingdong", table), out_field=("skuid","comment"), pipeline=pipeline):
                    if int(skuid) in skuid_sukid_dict:
                        count = count + 1
                        if count < 50:
                            a.add(int(skuid))
                    else:
                        count1 = count1 + 1
                        if count1 < 50:
                            b.add(int(skuid))

        print(count,)
        for i,v in enumerate(a):
            print(v)
        print(count1,)
        for i,v in enumerate(b):
            print(v)

if __name__ == "__main__":
    #item = {"m" : "-1.00", "cbf" : "0", "_status" : 0, "p" : "-1.00", "op" : "-1.00", "id" : "58334228563" }
    #print(clean_price(item))
    run_result()



