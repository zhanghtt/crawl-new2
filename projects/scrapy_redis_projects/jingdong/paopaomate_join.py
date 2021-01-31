#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
# with op.DBManger() as m, open("paopaomate_summary","w") as f:
#     pipeline = [
#         {
#             "$lookup": {
#                 "from": "paopaomate_comment",
#                 "localField": "skuid",
#                 "foreignField": "skuid",
#                 "as": "skuid"
#             }
#         },
#         {"$out": "paopaomate_final"}
#     ]
#     m.aggregate(db_collect=("jingdong","paopaomate_summary"), pipeline=pipeline)
with op.DBManger() as m, open("paopaomate_summary","w") as f:
    tmp = {}
    for skuid, comment in m.read_from(db_collect=("jingdong","paopaomate_comment"),out_field=("skuid","comment")):
        tmp[str(skuid)] = comment

    headers = ["skuid","brand_id","price","comment_201905","comment_201906","comment_201907","comment_201908",
               "comment_201909","comment_201910","comment_201911","comment_201912","comment_202001","comment_202002",
               "comment_202003","comment_202004","comment_202005","comment_202006","comment_202007","comment_202008","comment_202009"]
    skuids = set()
    for item in tqdm(m.read_from(db_collect=("jingdong", "paopaomate_summary"))):
        f.write("\t".join([str(item[filed]) for filed in headers]) + "\t" + tmp[item["skuid"]] + "\n")
