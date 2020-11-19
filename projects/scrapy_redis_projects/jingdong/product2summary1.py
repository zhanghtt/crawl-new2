#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from mongo import op
from tqdm import tqdm
import pandas as pd
list = []
print("step1...",flush=True)
with op.DBManger() as m:
    last_summary = m.get_lasted_collection("jingdong",filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
    for i,item in tqdm(enumerate(m.read_from_yield(db_collect=("jingdong", last_summary)))):
        list.append(item)
last_df = pd.DataFrame(list)
del list
del last_df["_id"]
del last_df["price"]
del last_df["cate_id"]
del last_df["ziying"]
this_month=[]
print("step2...",flush=True)
with op.DBManger() as m:
    for i,item in tqdm(enumerate(m.read_from_yield(db_collect=("jingdong", "month202008")))):
        this_month.append(item)
this_df = pd.DataFrame(this_month)
del this_month
this_df["skuid"]=this_df["skuid"].astype(str)
this_df = this_df.rename(columns={'comments': 'comment_{}'.format(202008),"clean_price":"price"})
del this_df["_id"]
del this_df["type"]
del this_df["month"]
print("step3...",flush=True)
new_pd = pd.merge(last_df,this_df,how="right",on=["skuid"],)
print("step4...",flush=True)
new_pd.loc[new_pd["brand_id_y"].isnull(),"brand_id_y"]=new_pd[new_pd['brand_id_y'].isnull()]["brand_id_x"]
print("step5...",flush=True)
new_pd.loc[new_pd["brand_id_y"].isnull(),"brand_id_y"]="0"
new_pd = new_pd.sort_index(axis=1)
print("step6...",flush=True)
new_pd = new_pd.fillna(method='bfill',axis=1)
del new_pd["brand_id_x"]
new_pd = new_pd.rename(columns={'brand_id_y': "brand_id"})
print("step7...",flush=True)
with op.DBManger() as m:
    m.insert_many_dict(db_collect=("jingdong","summary_201905_202008"),data_dict_list=json.loads(new_pd.T.to_json()).values())
