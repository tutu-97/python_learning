"""
演示RDD的filter成员方法的使用
接收一个处理函数，可用lambda快速编写
函数对rdd数据逐个处理，得到true的保留至返回值的RDD中
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:\\proApp\\Python3.10.4\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 对RDD的数据进行过滤
rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())

