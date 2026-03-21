"""
演示将RDD输出到文件中
saveAsTextFile()  将RDD的数据写入文本文件中
当文件较少时，调用少个大核，处理速度快，反之调用多核
"""

import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = 'D:\\proApp\\Python3.10.4\\Python310\\python.exe'
# os.environ['HADOOP_HOME'] = "D:\\proApp\\hadoop3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# 方法1，SparkConf对象设置属性全局并行度为1
# conf.set("spark.default.parallelism", "1")

sc = SparkContext(conf=conf)

# 方法2，创建RDD的时候设置（parallelize方法传入numSlices参数为1）
# 准备RDD1
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)

# 准备RDD2
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)], 1)

# 准备RDD3
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]], 1)

# 输出到文件中
rdd1.saveAsTextFile("D:\\个人\\learning\\python\\资料\\第15章资料\\资料\\output1")
rdd2.saveAsTextFile("D:\\个人\\learning\\python\\资料\\第15章资料\\资料\\output2")
rdd3.saveAsTextFile("D:\\个人\\learning\\python\\资料\\第15章资料\\资料\\output3")
