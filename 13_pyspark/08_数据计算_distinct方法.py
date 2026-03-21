"""
演示RDD的distinct成员方法的使用
功能：对RDD数据进行去重，返回新RDD
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:\\proApp\\Python3.10.4\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 1, 3, 3, 5, 5, 7, 8, 8, 9, 10])
# 对RDD的数据进行去重
rdd2 = rdd.distinct()

print(rdd2.collect())

