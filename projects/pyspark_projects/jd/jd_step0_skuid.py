#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf
from mongo import op
from pyspark.sql.types import *
import pyspark.sql.functions as F
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

        schema = StructType([StructField("skuid", LongType(), True),StructField("cate_id", StringType(), True),
                             StructField("brand_id", StringType(), True),StructField("shopid", StringType(), True),
                             StructField("venderid", StringType(), True),StructField("shop_name", StringType(), True)
                                , StructField("title", StringType(), True), StructField("_status", IntegerType(), True)])
        df = spark.createDataFrame([], schema)

        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).\
                option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(schema).load().where("_status=0").select(schema.names)
            df = df.unionAll(tmp)
        df = df.groupby(["skuid"]).agg(F.collect_set('cate_id').alias('cate_id'),F.collect_set('brand_id').alias('brand_id')
                                       ,F.collect_set('shopid').alias('shopid'),F.collect_set('venderid').alias('venderid')
                                       ,F.collect_set('shop_name').alias('shop_name'),F.collect_set('title').alias('title'))
        df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.skuids").mode("overwrite").save()
