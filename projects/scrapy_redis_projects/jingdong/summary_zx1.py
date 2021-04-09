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
        brandid2name={}
        for brand_id, brand_name in m.read_from(db_collect=("jingdong", "jdbrand20210108retry0"),
                                                                              out_field=("brand_id", "name")):
            if brand_id:
                brandid2name[int(brand_id)] = brand_name
        skuid_sukid_dict = {}
        #last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20\d\d\d\d\d\d_sep"}})
        #for table in m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20\d\d\d\d\d\d)retry\d*$"}}):
        last_sep = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdskuid20201214_sep"}})
        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20210108)retry\d*$"}})
        tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20201214)retry\d*$"}}))
        for table in tables:
            if not last_sep or table > last_sep:
                print("step 1: processing {}".format(table), flush=True)
                pipeline = [
                    {
                        "$match": {"_status": 0}
                    },
                    {
                        "$project": {
                            "skuid": "$skuid",
                            "cate_id": "$cate_id",
                            "brand_id": "$brand_id",
                            "shopid": "$shopid",
                            "shop_name": "$shop_name",
                            "title": "$title",
                        }
                    },
                ]
                for skuid, cate_id, brand_id, shopid, shop_name, title in m.read_from(db_collect=("jingdong", table), out_field=("skuid","cate_id","brand_id","shopid","shop_name","title"), pipeline=pipeline):
                    skuid_sukid_dict[int(skuid)]={"cate_id":cate_id,"brand_id": "0" if brand_id is None else brand_id,"shopid":shopid,"shop_name":shop_name,"title":title}

        #skuids in last result
        buffer = []
        buffer_size = 5000
        last_result = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^summary_201905_202012"}})
        print("step 2: processing {}".format(last_result), flush=True)
        count = 0
        out_table = "summary_zx_" + "202007"
        for element in m.read_from(db_collect=("jingdong", last_result)):
            count = count + 1
            skuid = element["skuid"]
            if int(skuid) not in skuid_sukid_dict:
                tmp = {"brand_name": brandid2name.get(int(brand_id))}
            else:
                item = skuid_sukid_dict[int(skuid)]
                tmp = {"brand_name": brandid2name.get(int(brand_id)), "shopid":item["shopid"],"shop_name":item["shop_name"],"title":item["title"]}
            buffer.append(tmp)
            if count % buffer_size == 0 and buffer:
                m.insert_many_dict(db_collect=("jingdong",out_table), data_dict_list=buffer)
                buffer = []
        if buffer:
            m.insert_many_dict(db_collect=("jingdong", out_table),
                               data_dict_list=buffer)


if __name__ == "__main__":
    run_result()



