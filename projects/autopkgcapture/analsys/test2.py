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
    dicts = {"ee80e6de-7fd6-11eb-ab8e-64006a071f72" : "2021-03-05","05f113e4-7fd7-11eb-be41-64006a071f72" : "2021-03-06"
        , "1c2966a6-7fd7-11eb-9327-64006a071f72": "2021-03-07","343cceec-7fd7-11eb-a01c-64006a071f72":"2021-03-08","other":"2021-03-08"}
    for item in m.read_from(db_collect=("jicheng", "autopkgcatpure"), out_field=("app_id","action_id","session_id","host","time")):
        app_id, action_id, session_id, host, time = item
        if app_id == "1":
            date=time[0:10]
            teim = time[10:]
            current_time = timeUtil.getdate(1,current_time,format="%Y-%m-%d")
            if session_id in dicts:
                time = dicts[session_id] + teim
            else:
                time = "2021-03-08" + teim
            print(app_id, action_id, session_id, host, time)
            m.insert_one_tupe(db_collect=("jicheng", "autopkgcatpure11"),data_tupe=(app_id, action_id, session_id, host, time),fields=("app_id","action_id","session_id","host","time"))

