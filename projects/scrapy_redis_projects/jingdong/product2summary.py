#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
skuids = set()
with open("idchaoshi_result") as f:
    for id in f:
        skuids.add(id.strip())
with op.DBManger() as m:
    import time
    pipeline = [
        {
            "$project": {
                "skuid": "$skuid",
                "cate_id": "$cate_id",
                "comments": "$comments",
                "clean_price": "$clean_price",
                "brand_id": "$brand_id"
            }
        },
    ]
    last_summary = m.get_lasted_collection("jingdong",filter={"name": {"$regex": r"^summary_201905_20\d\d\d\d$"}})
    for item in m.read_from_yield(db_collect=("jingdong", last_summary)):
        if item[1]:
            if int(item[1].split(",")[0]) in cate1s:
                oit.write("\t".join([str(i) for i in item]) + "\n")
