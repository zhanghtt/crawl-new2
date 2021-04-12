#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
from pyspark.sql.functions import udf, array
import re,sys
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql import Window


if __name__=='__main__':
    myconf = SparkConf()
    myconf.setAppName("test").setMaster("local[4]")
    myconf.set('spark.executor.instances','4')
    myconf.set('spark.driver.memory','6G')
    #myconf.set('spark.executor.memory','1G')
    myconf.set('spark.executor.cores','4')
    myconf.set('spark.task.cpus','4')
    myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:3.0.0")
    spark = SparkSession.builder.config(conf=myconf).getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)


    # 使用指定格式读取
    with op.DBManger() as m:
        df = spark.read.format("mongo").option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment_price_fillna").option(
            "spark.mongodb.input.partitioner", "MongoSplitVectorPartitioner").schema(StructType(
            [StructField("skuid", LongType(), True), StructField("comment", IntegerType(), True), StructField("month", StringType(), True),StructField("price", DoubleType(), True)])).load()
        comment_gmv = df.withColumn("comment_gmv", F.col('price')*(F.col('comment')-F.lag("comment").over(Window.partitionBy("skuid").orderBy(F.asc("month")))))
        comment_gmv.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment_gmv").mode("append").save()#overwrite
