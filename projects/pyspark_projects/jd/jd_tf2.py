#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow
from pyspark.sql.functions import split
from pyspark.ml.fpm import FPGrowth
from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.functions import udf, array
import re
from pyspark.sql.types import *
import pyspark.sql.functions as F
price_pattern = re.compile(r'^\d+\.\d\d$')
myconf = SparkConf()
myconf.setAppName("test").setMaster("local[40]")
myconf.set('spark.executor.instances','40')
myconf.set('spark.driver.memory','6G')
#myconf.set('spark.executor.memory','1G')
myconf.set('spark.executor.cores','40')
myconf.set('spark.task.cpus','40')

# 指定连接器对应的spark-package
myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.4.1")
spark = SparkSession.builder.config(conf=myconf).getOrCreate()
logger = spark._jvm.org.apache.log4j
logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

filter_hosts=["vivo","google.com","google.cn","oppomobile","baidu.com","hicloud"]
@udf(returnType=BooleanType())
def filter_host(item):
    for i in filter_hosts:
        if item.find(i) != -1:
            return False
    return True

contains_hosts=["jd.com"]
@udf(returnType=BooleanType())
def contains_host(item):
    for i in contains_hosts:
        if item.find(i) != -1:
            return True
    return False

df=spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jicheng.autopkgcatpure20210420").option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").load()
df=df.filter(filter_host('host')).select(['app_id','host','session_id'])

hosts=df.select(['host']).distinct().rdd.map(lambda r : r['host']).collect()
hosts.sort()

df1=df.groupBy('app_id','session_id') \
        .pivot('host', hosts) \
        .agg(F.count('host')).fillna(0)
df2=df1.toPandas()
df2.to_csv("tf22.csv")