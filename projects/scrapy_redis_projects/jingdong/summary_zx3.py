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
        for shopid, shop_name in m.read_from(db_collect=("jingdong", "zhaixun_shop"), out_field=("shopid","shop_name")):
            if shop_name:
                skuid_sukid_dict[shopid] = (shopid,shop_name)

        #skuids in last result
        m.date_tuple_to_db(date_tuple_list=list(skuid_sukid_dict.values()),db_collect=("jingdong","zhaixun_shop_1"),fields_tupe=("shopid","shop_name"))


if __name__ == "__main__":
    run_result()



