"""
演示RDD的reduceByKey成员方法的使用
功能：针对KV型RDD，自动按照key分组，然后根据自己提供的聚合逻辑，完成组内数据（value）的聚合操作
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:\\proApp\\Python3.10.4\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('男', 99), ('男', 88), ('男', 77), ('女', 99), ('女', 66)])
# 求男生和女生两个组的成绩之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())
# 结果：[('男', 187), ('女', 165)]
