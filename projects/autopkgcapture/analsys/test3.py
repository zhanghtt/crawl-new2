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
    dicts = {"94e4cd02-7fd6-11eb-9cbb-64006a071f72" : "2021-03-05","acdf037e-7fd6-11eb-aed0-64006a071f72" : "2021-03-06"
        , "c217c5b4-7fd6-11eb-a070-64006a071f72": "2021-03-07","d7c69286-7fd6-11eb-8def-64006a071f72":"2021-03-08","other":"2021-03-08"}
    for item in m.read_from(db_collect=("jicheng", "autopkgcatpure"), out_field=("app_id","action_id","session_id","host","time")):
        app_id, action_id, session_id, host, time = item
        if app_id == "2":
            #print(app_id, action_id, session_id, host, time)
            date=time[0:10]
            teim = time[10:]
            current_time = timeUtil.getdate(1,current_time,format="%Y-%m-%d")
            if session_id in dicts:
                time = dicts[session_id] + teim
            else:
                time = "2021-03-08" + teim
            print(app_id, action_id, session_id, host, time)
            m.insert_one_tupe(db_collect=("jicheng", "autopkgcatpure11"),data_tupe=(app_id, action_id, session_id, host, time),fields=("app_id","action_id","session_id","host","time"))

