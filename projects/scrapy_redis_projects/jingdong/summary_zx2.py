#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mongo import op
import logging
logger = logging.getLogger(__name__)
import re
price_pattern = re.compile(r'^\d+\.\d\d$')
from multiprocess.tools import timeUtil
from jingdong.Tools import format_cat_id
current_date = timeUtil.current_time()
price_pattern = re.compile(r'^\d+\.\d\d$')


def run_result():
    with op.DBManger() as m:
        skuid_sukid_dict = {}
        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20210108)retry\d*$"}})
        tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20201214)retry\d*$"}}))
        tables.extend(m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdskuid(20200821)retry\d*$"}}))
        tables.extend(m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdskuid(20200920)retry\d*$"}}))
        for table in tables:
            print("step 1: processing {}".format(table), flush=True)
            pipeline = [
                {
                    "$match": {"_status": 0}
                },
                {
                    "$project": {
                        "shopid": "$shopid",
                        "shop_name": "$shop_name",
                    }
                },
            ]
            for shopid, shop_name in m.read_from(db_collect=("jingdong", table), out_field=("shopid","shop_name"), pipeline=pipeline):
                if shop_name:
                    skuid_sukid_dict[shopid] = (shopid,shop_name)
                elif shopid:
                    skuid_sukid_dict[shopid] = (shopid, None)


        #skuids in last result
        m.date_tuple_to_db(date_tuple_list=list(skuid_sukid_dict.values()),db_collect=("jingdong","zhaixun_shop"),fields_tupe=("shopid","shop_name"))


if __name__ == "__main__":
    run_result()



