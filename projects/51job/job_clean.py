#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
from tqdm import tqdm
job_table = "job_20200616"
pipeline=[
    {
        "$lookup": {
            "from": "companyALL",
            "localField": "comId",
            "foreignField": "_id",
            "as": "company"
        }
    },
    {
        "$group": {
            "_id": {
                "jobId": "$jobId",
                "comId": "$comId"
            },
            "salary": {
                "$last": "$salary"
            },
            "postdate": {
                "$last": "$postdate"
            },
            "location": {
                "$last": "$location"
            },
            "position": {
                "$last": "$position"
            },
            "backgroud": {
                "$last": "$backgroud"
            },
            "name": {
                "$last": {
                    "$arrayElemAt": [
                        "$company.name",
                        0
                    ]
                }
            },
            "industry": {
                "$last": {
                    "$arrayElemAt": [
                        "$company.industry",
                        0
                    ]
                }
            },
            "compkind": {
                "$last": {
                    "$arrayElemAt": [
                        "$company.compkind",
                        0
                    ]
                }
            },
            "size": {
                "$last": {
                    "$arrayElemAt": [
                        "$company.size",
                        0
                    ]
                }
            }
        }
    },
    {
        "$out": "{}_clean".format(job_table)
    }
]

with op.DBManger() as m:
    m.aggregate(db_collect=("51job",job_table), pipeline=pipeline)