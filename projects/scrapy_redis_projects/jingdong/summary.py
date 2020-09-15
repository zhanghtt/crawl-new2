#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import logging
logger = logging.getLogger(__name__)
import re
price_pattern = re.compile(r'^\d+\.\d\d$')
def clean_price(item):
    price = 0
    k = 0
    if 'l' in item and 'm' in item:
        if item['l'] < item['m']:
            for key in item:
                str_price_list = price_pattern.findall(item[key])
                if key != 'l' and key != 'm' and str_price_list:
                    price = price + float(str_price_list[0])
                    k = k + 1
        else:
            for key in item:
                str_price_list = price_pattern.findall(item[key])
                if key != 'l' and str_price_list:
                    price = price + float(str_price_list[0])
                    k = k + 1
    if price == 0:
        price = 79.90
        k = 1
    return round(price / k, 2)

with op.DBManger() as m:
    pipeline = [
        {
            "$match": {"_status": 0},
        }
    ]
    price_dic = {}
    last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdprice20\d\d\d\d\d\d_sep"}})
    for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdprice(20\d\d\d\d\d\d)$"}}):
        if not last_sep or table > last_sep:
            logger.info("valid table : {}".format(table))
            for item in m.read_from(db_collect=("jingdong", table), pipeline=pipeline):
                if item["id"] in price_dic:
                    price_dic[int(item["id"])]["prices"].append(clean_price(item))
                else:
                    price_dic[int(item["id"])] = {"prices": []}


    #skuids in last result
    last_month_skuids = {}
    last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
    last_month = last_result.split("_")[-1]
    for skuid, comments, price,cate_id,brand_id,ziying in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid","comment_{}".format(last_month),"price","cate_id","brand_id","ziying")):
        last_month_skuids[int(skuid)] = {"clean_price":price,"comments":comments, "cate_id":cate_id,"brand_id":brand_id,"ziying":ziying}

    skuid_sukid_dict = {}
    last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep"}})
    for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
        if not last_sep or table > last_sep:
            logger.info("valid table : {}".format(table))
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
                skuid_sukid_dict[int(skuid)]={"cate_id":cate_id,"brand_id":brand_id,"ziying":ziying}

    last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20\d\d\d\d\d\d_sep"}})
    for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20\d\d\d\d\d\d)retry\d*$"}}):
        if not last_sep or table > last_sep:
            logger.info("valid table : {}".format(table))
            pipeline = [
                {
                    "$match": {
                        "$and": [{"_status": 0}, {"comment": {"$gt": 0}}]
                    }
                },
                {
                    "$project": {
                        "skuid": "$skuid",
                        "comment": "$comment",
                    }
                },
            ]
            for skuid, comments in m.read_from(db_collect=("jingdong", table), out_field=("skuid","comment"), pipeline=pipeline):
                if int(skuid) in price_dic:
                    price_item = price_dic[int(skuid)]
                    price_item["clean_price"] = sum(price_item["prices"])/len(price_item["prices"]) if len(price_item["prices"]) > 0 else 79.90
                    price_item["comments":int(comments)]
                    price_item["type"]=0
                elif int(skuid) in last_month_skuids:
                    last_month_price_item = last_month_skuids[int(skuid)]
                    price_item = price_dic[int(skuid)]
                    price_item["clean_price"] = last_month_price_item["clean_price"]
                    price_item["comments":"comments":int(comments)]
                    price_item["type"] = 1
                else:
                    price_dic[int(skuid)] = {"clean_price":79.90,"comments":int(comments)}
                    price_item["type"] = 2


