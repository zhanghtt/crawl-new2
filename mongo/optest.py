#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
pipeline = [
    {
        "$lookup": {
            "from": "companyALL_2",
            "localField": "formdata.ecompIds",
            "foreignField": "_id",
            "as": "company"
        }
    },
    {
        "$unwind": "$data.list"
    },
    {
        "$project": {
            "_id": 0,
            "ecompIds": "$formdata.ecompIds",
            "name": {
                "$arrayElemAt": [
                    "$company.name",
                    0
                ]
            },
            "dq": {
                "$arrayElemAt": [
                    "$company.dq",
                    0
                ]
            },
            "industry": {
                "$arrayElemAt": [
                    "$company.industry",
                    0
                ]
            },
            "e_kind": {
                "$arrayElemAt": [
                    "$company.e_kind",
                    0
                ]
            },
            "salary": "$data.list.salary",
            "city": "$data.list.city",
            "title": "$data.list.title",
            "refreshTime": "$data.list.refreshTime",
            "ejobId": "$data.list.ejobId",
            "dept": "$data.list.dept",
            "hot": "$data.list.hot",
            "citySEOUrl": "$data.list.citySEOUrl",
            "time": "$data.list.time",
            "workYear": "$data.list.workYear",
            "feedbackPeriod": "$data.list.feedbackPeriod",
            "eduLevel": "$data.list.eduLevel"
        }
    },
    {
        "$group": {
            "_id": {
                "ecompIds": "$ecompIds",
                "ejobId": "$ejobId"
            },
            "name": {
                "$first": "$name"
            },
            "dq": {
                "$first": "$dq"
            },
            "industry": {
                "$first": "$industry"
            },
            "e_kind": {
                "$first": "$e_kind"
            },
            "salary": {
                "$first": "$salary"
            },
            "city": {
                "$first": "$city"
            },
            "title": {
                "$first": "$title"
            },
            "refreshTime": {
                "$first": "$refreshTime"
            },
            "dept": {
                "$first": "$dept"
            },
            "hot": {
                "$first": "$hot"
            },
            "citySEOUrl": {
                "$first": "$citySEOUrl"
            },
            "time": {
                "$first": "$time"
            },
            "workYear": {
                "$first": "$workYear"
            },
            "feedbackPeriod": {
                "$first": "$feedbackPeriod"
            },
            "eduLevel": {
                "$first": "$eduLevel"
            }
        }
    },
    {
        "$out": "job_20200602_clean"
    }
]

with op.DBManger() as m:
    # last = m.get_lasted_collection("jingdong", filter={"name": {"$regex": r"^jdcomment20\d\d\d\d\d\d$"}})
    # for table in m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdcomment(20\d\d\d\d\d\d)retry\d*$"}}):
    #     if not last or table > last:
    #         print(table)
    import time

    pipeline = [ {
        "$project": {
            "_id": 0,
            "cate_id": "$cate_id",
        }
    },]
    s1 = set()
    for i in m.read_from_yield(db_collect=("jingdong", "jdbrand20200920retry0"),out_field=("cate_id",), pipeline=pipeline):
        s1.add(i[0])

    s2 = set()
    for i in m.read_from_yield(db_collect=("jingdong", "newCateName"),out_field=("cate_id",), pipeline=pipeline):
        s2.add(i[0])
    s3 = s2 - s1
    print(len(s3))
    for i in s3:
        print(i)

