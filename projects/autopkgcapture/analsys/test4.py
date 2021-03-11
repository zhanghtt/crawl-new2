#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import re
from multiprocess.tools import timeUtil
fatt = re.compile("\d+\.\d+\.\d+\.\d+")
with op.DBManger() as m:
    # 创建临时表本月任务的分界线
    skuid = {}
    hosts = {}
    last_time = ""
    current_time = "2021-03-05"
    last_session_id = ""
    for item in m.read_from(db_collect=("jicheng", "autopkgcatpure_bak"), out_field=("app_id","action_id","session_id","host","time")):
        app_id, action_id, session_id, host, time = item
        m.insert_one_tupe(db_collect=("jicheng", "autopkgcatpure"),data_tupe=(app_id, action_id, session_id, host, time),fields=("app_id","action_id","session_id","host","time"))

