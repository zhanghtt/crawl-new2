#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from multiprocess.tools import timeUtil
current_date = "20200821"
current_month = current_date[:-2]
last_1_month, last_2_month, last_3_month = timeUtil.get_month(-1, current_month),timeUtil.get_month(-2, current_month),timeUtil.get_month(-3, current_month),
comment_table = "secoComment{}".format(current_date)

with op.DBManger() as m:
   for month in [last_1_month]:
       # 合并属于一个月的List
       m.drop_db_collect(db_collect=("secoo","List{}".format(month)))
       dic = {}
       for listday in m.list_tables(dbname="secoo", filter={"name": {"$regex": r"List{}\d\d$".format(month)}}):
           print(listday,"List{}".format(month))
           for item in m.read_from(db_collect=("secoo",listday), out_field=("pid","price","self")):
               dic.update({item[0]: (item[1], item[2])})
       date_tuple_list = []
       for k, (p, s) in dic.items():
           date_tuple_list.append((k, k, p, s))
       m.insert_many_tupe(db_collect=("secoo","List{}".format(month)),data_tupe_list=date_tuple_list, fields=("_id","pid","price","self"))
       # 有销量
       pipeline1 = [
           {
               "$match": {
                   "$and": [{"_status": 0}, {"pid": {"$ne": None}}]
               }
           },
           {
               "$project": {
                   "cid": "$cid",
                   "pid_rel": "$pid_rel",
                   "pid": "$pid",
                   "user": "$user",
                   "device": "$device",
                   "price": "$price",
                   "date": "$date",
                   "month": {"$substr": ["$date", 0, 6]},
                   "self": "$self",
               }
           },
           {
               "$match": {
                   "month": "{}".format(month)
               }
           },
           {
               "$lookup": {
                   "from": "CleanListNew",
                   "localField": "pid",
                   "foreignField": "_id",
                   "as": "tableb"
               }
           },
           {
               "$group": {
                   "_id": {
                       "month": "$month",
                       "cid": "$cid",
                       "pid": "$pid",
                       "pid_rel": "$pid_rel",

                   },
                   "user": {
                       "$last": "$user",
                   },
                   "device": {
                       "$last": "$device",
                   },
                   "price": {
                       "$last": "$price",
                   },
                   "tmp_price": {
                       "$last": {
                           "$arrayElemAt": [
                               "$tableb.price",
                               0
                           ]
                       }

                   },
                   "tmp_self": {
                       "$last": {
                           "$arrayElemAt": [
                               "$tableb.self",
                               0
                           ]
                       }

                   },
               },
           },
           {
               "$project": {
                   "_id": 0,
                   "month": "$_id.month",
                   "cid": "$_id.cid",
                   "pid_rel": "$_id.pid_rel",
                   "pid": "$_id.pid",
                   "user": "$user",
                   "device": "$device",
                   "price": {
                       "$cond": {
                           "if": {"$ne": ["$tmp_price", None]}, "then": "$tmp_price",
                           "else": "$price"
                       }
                   },
                   "tmp_self": "$tmp_self",
               }
           },
           {
               "$lookup": {
                   "from": "CleanListNew",
                   "localField": "pid_rel",
                   "foreignField": "_id",
                   "as": "tablec"
               }
           },
           {
               "$project": {
                   "_id": 0,
                   "month": "$month",
                   "cid": "$cid",
                   "pid_rel": "$pid_rel",
                   "pid": "$pid",
                   "user": "$user",
                   "device": "$device",
                   "price": "$price",
                   "tmp_self": "$tmp_self",
                   "tmp_self1": {
                       "$arrayElemAt": [
                           "$tablec.self",
                           0
                       ]
                   },
               }
           },
           {
               "$project": {
                   "_id": 0,
                   "month": "$month",
                   "cid": "$cid",
                   "pid_rel": "$pid_rel",
                   "pid": "$pid",
                   "user": "$user",
                   "device": "$device",
                   "price": "$price",
                   "self": {
                       "$cond": {
                           "if": {"$ne": ["$tmp_self", None]}, "then": "$tmp_self",
                           "else": {
                               "if": {"$ne": ["$tmp_self1", None]}, "then": "$tmp_self1",
                               "else": "其他"
                           }
                       }
                   },
               }
           },
           {
               "$group": {
                   "_id": {
                       "month": "$month",
                       "cid": "$cid",
                       "pid": "$pid",
                       "price": "$price",
                   },
                   "self": {
                       "$last": "$self"
                   }
               },
           },
           {
               "$group": {
                   "_id": {
                       "month": "$_id.month",
                       "pid": "$_id.pid",
                       "price": "$_id.price",
                   },
                   "sales": {"$sum": 1},
                   "self": {"$last": "$self"},
               },
           },
           {
               "$project": {
                   "_id": 0,
                   "month": "$_id.month",
                   "pid": "$_id.pid",
                   "sales": "$sales",
                   "price": "$_id.price",
                   "self": {
                       "$cond": {
                           "if": {"$ne": ["$self", "自营"]}, "then": "0",
                           "else": "1"
                       }
                   },
               }
           },
           {
               "$out": "secoSales{}".format(month)
           }
       ]
       # 无销量
       pipeline2 = [
           {
               "$match": {
                   "$and": [{"_status": {"$ne": 0}}, {"_seed": {"$ne": None}}]
               }
           },
           {
               "$project": {
                   "pid_rel": {"$arrayElemAt": [
                       "$_seed",
                       0
                   ]
                   },
                   "price": {"$arrayElemAt": [
                       "$_seed",
                       1
                   ]
                   },
               }
           },
           {
               "$lookup": {
                   "from": "List{}".format(month),
                   "localField": "pid_rel",
                   "foreignField": "_id",
                   "as": "tableb"
               }
           },
           {
               "$project": {
                   "pid_rel": "$pid_rel",
                   "price": "$price",
                   "self": {
                       "$arrayElemAt": [
                           "$tableb.self",
                           0
                       ]
                   },
               }
           },
           {
               "$match": {
                   "self": {"$exists": True}
               }
           },
           {
               "$group": {
                   "_id": {
                       "pid_rel": "$pid_rel",
                       "price": "$price",
                   },
                   "self": {
                       "$last": "$self"
                   },
               },
           },
           {
               "$project": {
                   "_id": 0,
                   "month": "{}".format(month),
                   "pid": "$_id.pid_rel",
                   "sales": "0",
                   "price": "$_id.price",
                   "self": {
                       "$cond": {
                           "if": {"$ne": ["$self", "自营"]}, "then": "0",
                           "else": "1"
                       }
                   },
               }
           },
           {
               "$out": "secoNosales{}".format(month)
           }
       ]
       m.aggregate(db_collect=("secoo", comment_table), pipeline=pipeline1)
       m.aggregate(db_collect=("secoo", comment_table), pipeline=pipeline2)
       dic = {}
       for item in m.read_from(db_collect=("secoo", "secoNosales{}".format(month)), out_field=("pid", "price", "sales","self")):
           dic.update({item[0]: (item[1], item[2],item[3])})
       for item in m.read_from(db_collect=("secoo", "secoSales{}".format(month)),
                               out_field=("pid", "price", "sales", "self")):
           dic.update({item[0]: (item[1], item[2], item[3])})
       date_tuple_list = []
       for k, (p, s, self) in dic.items():
           date_tuple_list.append((k, k, p, s, self))
       m.drop_db_collect(db_collect=("secoo", "secoResult{}".format(month)))
       m.insert_many_tupe(db_collect=("secoo", "secoResult{}".format(month)), data_tupe_list=date_tuple_list,
                          fields=("_id", "pid", "price", "sales", "self"))