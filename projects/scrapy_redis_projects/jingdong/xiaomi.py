#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
skuids = set()
with op.DBManger() as m:
        for item in tqdm(m.read_from(db_collect=("jingdong", "summary_201905_202009"))):
            if item["brand_id"] in ["18374","394818"]:
                m.insert_one_dict(db_collect=("jingdong", "xiaomi"), data_dict=item)
