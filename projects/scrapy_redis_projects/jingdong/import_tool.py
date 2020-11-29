#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
with op.DBManger() as m:
    m.insert_many_tupe(db_collect=("jingdong", "jdchaoshiskuid"),data_tupe_list=list,fields=("_id","skuid"))

