"""
演示RDD的flatMap成员方法的使用
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:\\proApp\\Python3.10.4\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["itheima itcast 666", "itheima itheima itcast", "python itheima"])

# 需求，将RDD数据里面的一个个单词提取出来 flatMap比map多解除一层嵌套
# rdd2 = rdd.map(lambda x: x.split(" "))
rdd2 = rdd.flatMap(lambda x: x.split(" "))
print(rdd2.collect())
