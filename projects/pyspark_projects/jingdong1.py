#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark import SparkConf


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
    # 使用指定格式读取
    mg_data = spark.read.format("mongo").option("uri","mongodb://192.168.0.13:27017/jingdong.jdskuid20200821retry0").\
        option("spark.mongodb.input.partitioner","MongoSplitVectorPartitioner").filter("shop_name=='京东大药房' or shopid==10183439").load()
    mg_data.registerTempTable("tmp_table")
    dyf_df = spark.sql("select skuid, shopid from tmp_table where shopid=1000015441")
    dyf_df.show()
    dyf_df.write.format('mongo').option("uri","mongodb://192.168.0.13:27017/jingdong.dyf").mode("append").save()
    spark.stop()
