#!/usr/bin/env python3
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

    # 指定连接器对应的spark-package
    myconf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.4.1")
    spark = SparkSession.builder.config(conf=myconf).getOrCreate()
    logger = spark._jvm.org.apache.log4j
    logger.LogManager.getRootLogger().setLevel(logger.Level.FATAL)

    # 使用指定格式读取
    with op.DBManger() as m:
        month = '202101'
        last_month = '202012'
        tables = m.list_tables(dbname="jingdong", filter={"name": {"$regex": r"^jdprice20210129$"}})
        schema = StructType([StructField("skuid", LongType(), True),StructField("price", DoubleType(), True)])
        df = spark.createDataFrame([], schema)
        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").load().filter('_status=0').select(['id','p','op','cbf','l','m','op','p','tpp','up'])
            tmp = tmp.withColumn("price", clean_price(array('p','op','cbf','l','m','op','p','tpp','up'))).withColumn('skuid',F.col('id').cast(LongType())).select('skuid','price')
            df = df.unionAll(tmp)
        df_price = df.groupBy(['skuid']).agg(F.avg('price').alias('price'))

        tables = m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20210302)retry\d*$"}})
        #tables.extend(m.list_tables(dbname="jingdong",filter={"name": {"$regex": r"^jdcomment(20210316)retry\d*$"}}))
        df = spark.createDataFrame([], StructType([StructField("skuid", LongType(), False),StructField("comment", IntegerType(), True)]))
        for table in tables:
            tmp = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.{}".format(table)).\
                option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(StructType([StructField("skuid", LongType(), False),StructField("comment", StringType(), True)])).load().withColumn('comment',F.col('comment').cast(IntegerType())).filter("comment > 0")
            df = df.unionAll(tmp)
        df_comment = df.groupBy(['skuid']).agg(F.max('comment').alias('comment'))
        df_last = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.month{}".format(last_month)).option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").schema(
            StructType([StructField("skuid", LongType(), False),StructField("comments", IntegerType(), True)
                           ,StructField("clean_price", DoubleType(), True),StructField("type", IntegerType(), True)])).load()
        df = df_comment.join(df_last, ['skuid'], 'outer').withColumn("comment_f", F.when(F.isnull(df_comment.comment),df_last.comments).otherwise(df_comment.comment)).select(['skuid',F.col('comment_f').alias('comments'),'clean_price'])
        df = df.join(df_price,['skuid'],'left').withColumn("clean_price", F.when(F.isnull(df_price.price),df.clean_price).otherwise(df_price.price)).fillna({'clean_price':79.90}).select(['skuid','comments','clean_price'])
        df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.month{}".format(month)).mode("overwrite").save()
        df.where('clean_price is null').select(["skuid"]).write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.jdprice_miss_seed").mode("overwrite").save()
        #启动jd_price_miss_1.py
        # price_miss = spark.read.format("mongo").option("uri", "mongodb://192.168.0.13:27017/jingdong.{}".format('jdprice_miss_out')).option(
        #     "spark.mongodb.input.partitioner", "MongoSplitVectorPartitioner").load().filter('_status=0').select(
        #     ['id', 'p', 'op', 'cbf', 'l', 'm', 'op', 'p', 'tpp', 'up'])
        # price_miss = price_miss.withColumn("price",
        #                      clean_price(array('p', 'op', 'cbf', 'l', 'm', 'op', 'p', 'tpp', 'up'))).withColumn('skuid',
        #                                                                                                         F.col(
        #                                                                                                             'id').cast(
        #                                                                                                             LongType())).select(
        #     'skuid', 'price')
        # df = df.join(price_miss, ['skuid'], 'left').withColumn("clean_price",
        #                                                      F.when(F.isnull(df.clean_price), price_miss.price).otherwise(
        #                                                          df.clean_price)).select(
        #     ['skuid', 'comments', 'clean_price'])
        # df.write.format('mongo').option("uri", "mongodb://192.168.0.13:27017/jingdong.month{}".format(month)).mode(
        #     "overwrite").save()



