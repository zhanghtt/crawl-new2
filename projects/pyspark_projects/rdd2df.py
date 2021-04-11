#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from pyspark.sql import Row
from pyspark.sql import SparkSession
def rowwise_function(row):
    # convert row to dict:
  row_dict = row.asDict()
    # Add a new key in the dictionary with the new column name and value.
  row_dict['Newcol'] = math.exp(row_dict['rating'])
    # convert dict to row:
  newrow = Row(**row_dict)
    # return new row
  return newrow

# convert ratings dataframe to RDD
ratings_rdd = ratings.rdd
# apply our function to RDD

ratings_rdd_new = ratings_rdd.map(lambda row: rowwise_function(row))

# Convert RDD Back to DataFrame
spark = SparkSession.builder.config(conf=myconf).getOrCreate()
ratings_new_df = sqlContext.createDataFrame(ratings_rdd_new)
ratings_new_df.show()