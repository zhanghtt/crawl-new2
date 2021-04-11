#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
from pyspark.sql.functions import udf, array
import re
from pyspark.sql.types import *
import pyspark.sql.functions as F
price_pattern = re.compile(r'^\d+\.\d\d$')


@udf(returnType=DoubleType())
def clean_price(item):
    price_tmp = []
    for key in item:
        current_value = str(key)
        str_price_list = price_pattern.findall(current_value)
        if str_price_list and str_price_list[0] != "-1.00":
            price_tmp.append(float(str_price_list[0]))
    if price_tmp:
        price = min(price_tmp)
    else:
        price = 79.90
    return price


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
        month = '202102'
        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdprice20210129$"}})
        #tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdprice20210302$$"}}))
        schema = StructType([StructField("skuid", IntegerType(), True),StructField("price", DoubleType(), True),StructField("month", StringType(), True)])
        df = spark.createDataFrame([], schema)
        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").load().filter('_status=0').select(['id','p','op','cbf','l','m','op','p','tpp','up'])
            tmp = tmp.withColumn("price", clean_price(array('p','op','cbf','l','m','op','p','tpp','up'))).withColumn('skuid',F.col('id').cast(IntegerType())).select('skuid','price').withColumn('month', F.lit(month))
            df = df.unionAll(tmp)
        df = df.groupBy(['skuid','month']).agg(F.avg('price').alias('price'))
        tmp = spark.read.format("mongo").option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment").option(
            "spark.mongodb.input.partitioner", "MongoSplitVectorPartitioner").schema(StructType(
            [StructField("skuid", IntegerType(), True), StructField("comment", StringType(), True), StructField("month", StringType(), True)])).load().filter("month={}".format(month))
        df = df.join(tmp, [df.month == tmp.month,df.skuid == tmp.skuid], 'right').select([tmp.month, tmp.skuid, tmp.comment, df.price])
        df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_comment_price").mode("append").save()#overwrite