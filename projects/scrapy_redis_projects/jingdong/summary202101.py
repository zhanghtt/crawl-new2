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
        pipeline = [
            {
                "$match": {"_status": 0},
            }
        ]
        price_dic = {}
        #last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdprice20\d\d\d\d\d\d_sep"}})
        #for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdprice(20\d\d\d\d\d\d)$"}}):
        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdprice20201209_sep"}})
        for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdprice(20210129)$"}}):
            if not last_sep or table > last_sep:
                print("step 1: processing {}".format(table), flush=True)
                for item in m.read_from(db_collect=("jingdong", table), pipeline=pipeline):
                    if int(item["id"]) in price_dic:
                        tmp = price_dic[int(item["id"])]
                        tmp["prices"] = (tmp["prices"][0]+1, tmp["prices"][1]+clean_price(item))
                    else:
                        price_dic[int(item["id"])] = {"prices": (1, clean_price(item))}
        for skuid in price_dic:
            tmp = price_dic[int(skuid)]
            tmp["clean_price"] = round(tmp["prices"][1]/tmp["prices"][0], 2)
            tmp.pop("prices")
        result_dic = price_dic

        #skuids in last result
        last_month_skuids = {}
        last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^month20\d\d\d\d$"}})
        print("step 2: processing {}".format(last_result), flush=True)
        last_month = last_result[-6:]
        for skuid, comments, price,cate_id,brand_id,ziying in m.read_from(db_collect=("jingdong", last_result), out_field=("skuid","comments","clean_price","cate_id","brand_id","ziying")):
            if cate_id:
                last_month_skuids[int(skuid)] = {"clean_price":price,"comments":comments, "cate_id":format_cat_id(cate_id),"brand_id":brand_id,"ziying":ziying}

        skuid_sukid_dict = {}
        #last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep"}})
        #for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20201214_sep"}})
        for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20210108)retry\d*$"}}):
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
        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20201218_sep"}})
        for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20210302)retry\d*$"}}):
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
                        if int(skuid) in price_dic:
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = price_dic[int(skuid)]["clean_price"]
                            price_item["comments"]=int(comments)
                            price_item["type"]=0
                        elif int(skuid) in last_month_skuids:
                            last_month_price_item = last_month_skuids[int(skuid)]
                            if int(skuid) not in result_dic:
                                result_dic[int(skuid)] = {}
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = last_month_price_item["clean_price"]
                            price_item["comments"]=int(comments)
                            price_item["type"] = 1
                        else:
                            result_dic[int(skuid)] = {}
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = 79.90
                            price_item["comments"]=int(comments)
                            price_item["type"] = 2
                        skuid_sukid_item = skuid_sukid_dict[int(skuid)]
                        price_item["cate_id"] = skuid_sukid_item["cate_id"]
                        price_item["brand_id"] = skuid_sukid_item["brand_id"]
                        price_item["ziying"] = skuid_sukid_item["ziying"]
                    elif int(skuid) in last_month_skuids:
                        if int(skuid) in price_dic:
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = price_dic[int(skuid)]["clean_price"]
                            price_item["comments"]=int(comments)
                            price_item["type"] = 3
                        elif int(skuid) in last_month_skuids:
                            last_month_price_item = last_month_skuids[int(skuid)]
                            if int(skuid) not in result_dic:
                                result_dic[int(skuid)] = {}
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = last_month_price_item["clean_price"]
                            price_item["comments"]=int(comments)
                            price_item["type"] = 4
                        else:
                            result_dic[int(skuid)] = {}
                            price_item = result_dic[int(skuid)]
                            price_item["clean_price"] = 79.90
                            price_item["comments"]=int(comments)
                            price_item["type"] = 5
                        last_month_skuids_item = last_month_skuids[int(skuid)]
                        price_item["cate_id"] = last_month_skuids_item["cate_id"]
                        price_item["brand_id"] = last_month_skuids_item["brand_id"]
                        price_item["ziying"] = last_month_skuids_item["ziying"]
                    else:
                        result_dic[int(skuid)] = {}
                        price_item = result_dic[int(skuid)]
                        price_item["clean_price"] = 79.90
                        price_item["comments"]=int(comments)
                        price_item["cate_id"] = "0,0,0"
                        price_item["brand_id"] = "0"
                        price_item["ziying"] = "-1"
                        price_item["type"] = 6
        print("step 5: processing skuid in last_month_skuids but not in result_dic", flush=True)
        for skuid in last_month_skuids:
            if int(skuid) not in result_dic:
                result_dic[int(skuid)] = {}
                price_item = result_dic[int(skuid)]
                price_item["clean_price"] = last_month_skuids[skuid]["clean_price"]
                price_item["comments"] = last_month_skuids[skuid]["comments"]
                price_item["cate_id"] = "0,0,0"
                price_item["brand_id"] = "0"
                price_item["ziying"] = "-1"
                price_item["type"] = 7
            else:
                price_item = result_dic[int(skuid)]
                if 'type' not in price_item:
                    price_item["clean_price"] = last_month_skuids[skuid]["clean_price"]
                    price_item["comments"] = last_month_skuids[skuid]["comments"]
                    price_item["cate_id"] = last_month_skuids[skuid]["cate_id"]
                    price_item["brand_id"] = last_month_skuids[skuid]["brand_id"]
                    price_item["ziying"] = last_month_skuids[skuid]["ziying"]
                    price_item["type"] = 8

        this_month = timeUtil.get_month(deltamonth=1,current_month=last_month)
        out_table = "month" + this_month
        print("step 6: processing writing result to {}".format(out_table), flush=True)
        buffer = []
        buffer_size = 5000
        print("result_dic:{}".format(len(result_dic)),  flush=True)
        for i, k in enumerate(result_dic):
            result_dic[k]["skuid"] = k
            if "prices" in result_dic[k]:
                result_dic[k].pop("prices")
            result_dic[k]["month"] = this_month
            if "cate_id" in result_dic[k]:
                buffer.append(result_dic[k])
            else:
                print(result_dic[k])
            if i % buffer_size == 0 and buffer:
                m.insert_many_dict(db_collect=("jingdong",out_table), data_dict_list=buffer)
                buffer = []
        if buffer:
            m.insert_many_dict(db_collect=("jingdong", out_table),
                               data_dict_list=buffer)
        m.create_db_collection(db_collection=("jingdong", "jdprice{0}_sep".format(current_date)))


if __name__ == "__main__":
    #item = {"m" : "-1.00", "cbf" : "0", "_status" : 0, "p" : "-1.00", "op" : "-1.00", "id" : "58334228563" }
    #print(clean_price(item))
    run_result()



