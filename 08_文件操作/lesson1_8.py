
# 文件的编码
# 常用的是UTF-8编码

# 文件的读取 操作

# open()打开函数
# 打开一个已经存在的文件,或者创建一个新文件
# open(name.mode.encoding)
# name:是要打开的目标文件名的字符串(可以包含文件所在的具体路径)
# mode:设置打开文件的模式(访问模式):只读(r),写入(w),追加(a)等
# encoding:编码格式(推荐使用UTF-8)

# read()方法
# 文件对象。read(num)
# num表示要从文件中读取的数据的长度(单位是字节)，如果没有传入num，那么就表示读取文件中所有的数据

# readlines()方法
# 可以按照行的方式把整个文件中的内容进行一次性读取，并返回的是一个列表，其中每一行的数据为一个元素

# 打开文件
f=open("D:/个人/作业 考试/test.txt","r",encoding="UTF-8")
print(type(f))

# 多次读取，会从上一次末端继续

# 读取文件-read()
print(f.read(10))
print(f.read())   # 多次调用read，下一个read会在上一个的结尾处继续读取

# 读取文件-readlines()
lines=f.readlines()   # 读取文件的全部行，封装到列表中
print(type(lines))
print(lines)

# 读取文件-readline()
line1=f.readline()
line2=f.readline()
line3=f.readline()
print(line1)
print(line2)
print(line3)

import time
from os import close, write

# for循环读取文件行
# 每一个line临时变量，就记录了文件的一行数据
f=open("D:/个人/作业 考试/test.txt","r",encoding="UTF-8")
for line in f:
    print(line)

# 关闭文件
# close()关闭文件对象
# time.sleep(500000)  # 暂停50万秒
f.close()

# with open 语法
# 通过在with open的语句中对文件进行操作
# 可以在操作完成结束后自动关闭close文件，避免忘记close
with open("D:/个人/作业 考试/test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(line)

# print(f.readlines())

# test:单词计数
f = open("D:/个人/learning/python/word.txt", "r", encoding="UTF-8")
# 方法1：读取全部内容，通过字符串count方法统计itheima数量
# content = f.read()
# count = content.count("itheima")
# print(count)
# 方法2：读取内容，一行一行读取，判断单词出现的次数并累计
count=0
for line in f:
    # 将‘\n’替换掉
    # line=line.replace('\n','')

    # 去除开头和结尾的空格以及换行符
    line=line.strip()

    words=line.split(" ")
    for word in words:
        if word=='itheima':
            count+=1
print(count)
f.close()

from os import write

# 写入操作
# ‘w’文件不存在，会创建文件，存在会清空原有内容
# close方法带有flush()方法的功能
f=open("D:/个人/learning/python/test1.txt",'w',encoding='UTF-8')
f.write("hello world!!!")
f.close()

# 运行之后是hello world!!!但在运行下面的，将变成黑马程序员（’w‘,会清空所有内容）
# f=open("D:/个人/learning/python/test1.txt",'w',encoding='UTF-8')
# f.write("黑马程序员")
# f.flush()

# 文件的追加写入操作
f=open("D:/个人/learning/python/test1.txt",'a',encoding='UTF-8')
f.write("\nhappy new year!!!")
f.flush()
f.close()

# 文件操作具体案例
# 需求:账单文件 bill.txt

# 需求分析
# 打开文件得到文件对象，准备读取
fr=open("D:/个人/learning/python/bill.txt",'r',encoding='UTF-8')
# 打开文件得到文件对象，准备写入
fw=open("D:/个人/learning/python/bill.txt.bak",'w',encoding='UTF-8')
# for循环读取文件
for line in fr:
    line=line.strip()
    # 判断内容，将满足的内容写出
    if line.split(", ")[4]=="测试":
        continue
    # 将内容写出去
    fw.write(line)
    # 由于前面对内容进行了strip()的操作，所以要手动的写出换行符
    fw.write("\n")
fr.close()
fw.close()