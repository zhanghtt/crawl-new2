#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import os
import glob
os.chdir("/home/u9000/secoo/secoo/tmp")
with op.DBManger() as db:

    for file in glob.glob("newmseco20????"):
        if file >= "newmseco202005":
            continue
        newfile = "secoResult{}".format(file[8:])
        print("importing file: {} to {}".format(file, newfile))
        data_list = []
        for item in open("file"):
            item = item.strip().split("\t")
            item = (item[0],item[0],item[1],item[2],item[3])
            data_list.append(item)
        db.insert_many_tupe(db_collect=("secoo",newfile),data_tupe_list=data_list,fields=("_id","pid","sales","price","self"))
