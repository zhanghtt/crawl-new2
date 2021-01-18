#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
with op.DBManger() as m:
        skuids = set()
        for item in tqdm(m.read_from(db_collect=("jingdong", "paopaomate_skuids"))):
            skuids.add(str(item["skuid"]))
        print(len(skuids))
        for item in tqdm(m.read_from(db_collect=("jingdong", "summary_201905_202009"))):
            if item["skuid"] in skuids:
                m.insert_one_dict(db_collect=("jingdong", "paopaomate_summary"), data_dict=item)
