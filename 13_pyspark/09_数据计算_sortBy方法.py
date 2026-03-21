"""
演示RDD的sortBy成员方法的使用
功能：对RDD数据进行排序，基于指定的排序依据
rdd.sortBy(func,ascending=False,numPartitions=1)
func:(T)->U:告知按照RDD中的哪个数据进行排序，比如lambda x:x[1] 表示按照RDD中的第二列元素进行排序
ascending True升序 False降序
numPartitions:用多少分区排序
"""
import os

from pyspark import SparkConf, SparkContext

os.environ['PYSPARK_PYTHON'] = "D:\\proApp\\Python3.10.4\\Python310\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1. 读取数据文件
rdd = sc.textFile("D:\\个人\\learning\\python\\资料\\第15章资料\\资料\\hello.txt")
# 2. 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 3. 将所有单词都转换成二元元组，单词为Key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 4. 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 5. 对结果进行排序
final_rdd = result_rdd.sortBy(lambda x: x[1], ascending=True, numPartitions=1)
print(final_rdd.collect())



