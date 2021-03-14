#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import re
fatt = re.compile("\d+\.\d+\.\d+\.\d+")
with op.DBManger() as m:
    # 创建临时表本月任务的分界线
    skuid = {}
    hosts = {}
    for item in m.read_from(db_collect=("jicheng", "autopkgcatpure"), out_field=("app_id","session_id","host","time")):
        app_id, session_id, host, date = item
        day = date[:10]
        if not fatt.findall(host):
            if app_id not in skuid:
                s = set()
                s.add(session_id)
                s1 = set()
                s1.add(day)
                skuid[app_id] = [s,s1]
            else:
                skuid[app_id][0].add(session_id)
                skuid[app_id][1].add(day)

            #多少天
            if host not in hosts:
                s1 = set()
                s1.add(day)
                s2 = set()
                s2.add(app_id)
                hosts[host] = [0,s1,s2]
            else:
                hosts[host][0] = hosts[host][0] + 1
                hosts[host][1].add(day)
                hosts[host][2].add(app_id)

    for app_id in skuid:
        print(app_id, len(skuid[app_id][1]),len(skuid[app_id][0]))

    for host in hosts:
        print(host, len(hosts[host][1]),hosts[host][0],hosts[host][2].pop())
