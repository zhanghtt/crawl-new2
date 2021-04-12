#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('JupyterPySpark').enableHiveSupport().getOrCreate()
import pyspark.sql.functions as F
# 原始数据
test = spark.createDataFrame([('2018-01','项目1',100,2), ('2018-01','项目2',200,3), ('2018-01','项目3',300,1),
                            ('2018-02','项目1',1000,5), ('2018-02','项目2',2000,6), ('2018-03','项目4',999,8),
                            ('2018-05','项目1',6000,19), ('2018-05','项目2',4000,18), ('2018-05','项目4',1999,10)
                           ], ['月份','项目','收入','天数'])

test.show()

test_pivot = test.groupBy('月份') \
        .pivot('项目', ['项目1', '项目2', '项目3', '项目4']) \
        .agg(F.sum('收入')) \
        .fillna(0)

test_pivot.show()