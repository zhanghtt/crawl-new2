#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
from multiprocess.tools import timeUtil
month = "202008"
this_month={}
print("step1...",flush=True)
with op.DBManger() as m:
    for i,item in tqdm(enumerate(m.read_from_yield(db_collect=("jingdong", "month{}".format(month))))):
        if "type" in item:
            skuid = item.pop("skuid")
            item.pop("_id")
            item.pop("type")
            this_month[str(skuid)]=item

list = []
buffer_size = 10000
print("step2...",flush=True)
with op.DBManger() as m:
    last_summary = m.get_lasted_collection("jingdong",filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
    for i,item in tqdm(enumerate(m.read_from_yield(db_collect=("jingdong", last_summary)))):
        if item["skuid"] in this_month:
            this_item = this_month.pop(item["skuid"])
            item["comment_{}".format(month)] = this_item["comments"]
            item["price"] = this_item["clean_price"]
            item["ziying"] = this_item["ziying"]
            bid = this_item["brand_id"]
            if bid:
                item["brand_id"] = bid
            cate_id = this_item["cate_id"]
            if cate_id:
                item["cate_id"] = cate_id
        else:
            item["comment_{}".format(month)] = item["comment_{}".format(timeUtil.get_month(-1, current_month=month))]
        list.append(item)
        if i % buffer_size == 0:
            m.insert_many_dict(db_collect=("jingdong", "summary_201905_{}".format(month)),
                               data_dict_list=list)
            list = []
if list:
    m.insert_many_dict(db_collect=("jingdong", "summary_201905_{}".format(month)),
                       data_dict_list=list)
list=[]
print("step3...",flush=True)
for i, skuid in tqdm(enumerate(this_month)):
    this_item = this_month[skuid]
    item = {}
    item["skuid"] = skuid
    item["comment_{}".format(month)] = this_item["comments"]
    item["price"] = this_item["clean_price"]
    item["ziying"] = this_item["ziying"]
    bid = this_item["brand_id"]
    if bid:
        item["brand_id"] = bid
    else:
        item["brand_id"] = "0"
    cate_id = this_item["cate_id"]
    if cate_id:
        item["cate_id"] = cate_id
    else:
        item["cate_id"] = "0,0,0"
    count=0
    while timeUtil.get_month(count,current_month="201905") < month:
        item["comment_{}".format(timeUtil.get_month(count,current_month="201905"))]="0"
        count += 1
    list.append(item)
    if i % buffer_size == 0:
        m.insert_many_dict(db_collect=("jingdong", "summary_201905_{}".format(month)),
                           data_dict_list=list)
        list = []
if list:
    m.insert_many_dict(db_collect=("jingdong", "summary_201905_{}".format(month)),
                       data_dict_list=list)
