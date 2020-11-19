#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
skuids = set()
with op.DBManger() as m:
    pipeline = [
        {
            "$match": {
                "chaoshi": 1
            }
        },
    ]
    for item in tqdm(m.read_from(db_collect=("jingdong", "jdskuid20201106retry0"),pipeline=pipeline)):
        skuids.add(str(item["skuid"]))
    for item in tqdm(m.read_from(db_collect=("jingdong", "summary_201905_202009"))):
        if item["skuid"] in skuids:
            m.insert_one_dict(db_collect=("jingdong", "chaoshi"), data_dict=item)
