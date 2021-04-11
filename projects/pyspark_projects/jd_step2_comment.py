#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
import pyspark.sql.functions as F
from pyspark.sql.types import *

if __name__=='__main__':
    myconf = SparkConf()
    myconf.setAppName("test").setMaster("local[4]")
    myconf.set('spark.executor.instances','4')
    myconf.set('spark.driver.memory','6G')
    #myconf.set('spark.executor.memory','1G')
    myconf.set('spark.executor.cores','4')
    myconf.set('spark.task.cpus','4')

    # 指定连接器对应的spark-package
    myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:3.0.0")
    spark = SparkSession.builder.config(conf=myconf).getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

    # 使用指定格式读取
    with op.DBManger() as m:
        month = '202102'
        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20210316)retry\d*$"}})
        #tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20210316)retry\d*$"}}))
        df = spark.createDataFrame([], StructType([StructField("skuid", IntegerType(), True),StructField("comment", IntegerType(), True),StructField("month", StringType(), True)]))
        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).\
                option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(StructType([StructField("skuid", IntegerType(), True),StructField("comment", StringType(), True)])).load().filter("comment > '0'").select(['skuid','comment']).withColumn('comment',F.col('comment').cast(IntegerType())).withColumn('month', F.lit(month))
            df = df.unionAll(tmp)
        df = df.groupBy(['skuid','month']).agg(F.max('comment').alias('comment'))
        dyf_skuid = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.dyf_skuid").option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(StructType([StructField("skuid", IntegerType(), True)])).load().withColumn('month', F.lit(month)).distinct()
        df = df.join(dyf_skuid,[df.month==dyf_skuid.month,df.skuid==dyf_skuid.skuid],'right').select([dyf_skuid.month,dyf_skuid.skuid,df.comment])
        df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment").mode("append").save()