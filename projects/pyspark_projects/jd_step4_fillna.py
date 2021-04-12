#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql import Window
from pyspark.sql.functions import last,first,ntile,lag,udf, array
import sys,re


if __name__=='__main__':
    myconf = SparkConf()
    myconf.setAppName("test").setMaster("local[4]")
    myconf.set('spark.executor.instances','4')
    myconf.set('spark.driver.memory','6G')
    #myconf.set('spark.executor.memory','1G')
    myconf.set('spark.executor.cores','4')
    myconf.set('spark.task.cpus','4')
    myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.4.1")
    spark = SparkSession.builder.config(conf=myconf).getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)


    # 使用指定格式读取
    with op.DBManger() as m:
        df = spark.read.format("mongo").option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment_price").option("spark.mongodb.input.partitioner", "MongoSplitVectorPartitioner").schema(StructType(
            [StructField("month", StringType(), True), StructField("skuid", LongType(), True), StructField("comment", IntegerType(), True), StructField("price", DoubleType(), True)])).load()
        df = df.fillna({'price': 79.90})
        # 开窗函数，以id做分组，指定排序方式，设置窗口大小
        # last函数，返回分组中的最后一个值。ignorenulls为True表示只对null值应用
        ffill = df.withColumn("comment", last("comment", ignorenulls=True).over(Window.partitionBy("skuid").orderBy(F.asc("month")).rowsBetween(-sys.maxsize, 0)))
        bfill = ffill.withColumn("comment", first("comment", ignorenulls=True).over(Window.partitionBy("skuid").orderBy(F.asc("month")).rowsBetween(0,sys.maxsize)))
        bfill.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment_price_fillna").mode("overwrite").save()#overwrite
