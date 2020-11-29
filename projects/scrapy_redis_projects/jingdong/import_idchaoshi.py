#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
list = []
print("step1...",flush=True)
with open("idchaoshi_result") as f:
    for i in f:
        list.append((i.strip(),i.strip()))
buffer_size = 10000
print("step2...",flush=True)
with op.DBManger() as m:
    m.insert_many_tupe(db_collect=("jingdong", "jdchaoshiskuid"),data_tupe_list=list,fields=("_id","skuid"))

