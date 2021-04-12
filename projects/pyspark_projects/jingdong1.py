#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
from pyspark.sql.functions import udf, array
from pyspark.sql.types import DoubleType,StructType,Row
import re

price_pattern = re.compile(r'^\d+\.\d\d$')


@udf(returnType=DoubleType())
def clean_price(item):
    price_tmp = []
    for key in item:
        current_value = str(item[key])
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

    # 指定连接器对应的spark-package
    myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:3.0.0")
    # 指定mongo地址，需要每个工作节点都能访问到
    #myconf.set("spark.mongodb.input.uri","mongodb://192.168.0.13:27017/")
    # 设置要读取的dbs名和collection名
    #myconf.set("spark.mongodb.input.database","jingdong")
    #myconf.set("spark.mongodb.input.collection","jdskuid20200821retry0")
    # 指定分区方式
    #myconf.set("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner")

    spark = SparkSession.builder.config(conf=myconf).getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

    # 使用指定格式读取
    with op.DBManger() as m:
        skuid_sukid_dict = {}
        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20210108)retry\d*$"}})
        tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdskuid(20201214)retry\d*$"}}))
        tables.extend(m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdskuid(20200821)retry\d*$"}}))
        tables.extend(m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdskuid(20200920)retry\d*$"}}))
        from pyspark.sql.types import *
        schema = StructType([StructField("skuid", IntegerType(), True),StructField("shop_name", StringType(), True)])
        df = spark.createDataFrame([], schema)

        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).\
                option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(schema).load().filter("shop_name is not null and shop_name=='京东大药房'").select(['skuid','shop_name']).distinct().withColumn
            df = df.unionAll(tmp)
        df = df.distinct()
        df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.dyf_skuid").mode("overwrite").save()
        df.registerTempTable("dyf_skuid")
        dyf_df = spark.sql("select skuid from dyf_skuid where shopid=1000015441")
        dyf_df.write.format('mongo').option("uri","mongodb://192.168.0.13:27017/jingdong.dyf").mode("append").save()
        spark.stop()
