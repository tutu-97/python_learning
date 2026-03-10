
# 数据容器:一种可以存储多个元素的python数据类型
# python数据容器：list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
name_list=[1,'2',True]
print(name_list)
print(type(name_list))
# 数据容器：list(列表)
# 列表的定义：基本语法    用[]，逗号隔开元素，可以是不同的数据类型

# 字面量
# [元素1，元素2，元素3，元素4，···]

# 定义变量
# 变量名称=[元素1，元素2，元素3，元素4，···]

# 定义空列表
# 变量名称=[]
# 变量名称=list()

# 列表里面存列表：嵌套
my_list=[[1,2,3],['4',5,6]]
print(my_list)
print(type(my_list))
# 列表的下标（索引）
# 语法：列表[下标索引]
# 正向索引：0 1 2 ···（从左往右）
print(my_list[0])
print(my_list[1][2])
# 反向索引：-1 -2 -3 ···（从右往左）
print(my_list[-2])
print(my_list[1][-2])
# 错误示范：通过下标索引取数据，不要超出范围
# print(my_list[5])

# 列表的常用操作（方法）
def add1(x, y):
    return x + y
# 函数的使用：
num1=add1(1,2)
print(num1)
class Student:
    def add(self,x,y):
        return x+y
# 方法的使用
stu=Student()
num2=stu.add(1,2)
print(num2)

# 列表的查询功能
# 1 查找某元素下标：功能：查找指定元素在列表的下标，如果找不到，报错ValueError
# 语法：列表.index(元素)
my_list = ["name", "age", "time"]
print(my_list)
index = my_list.index("name")
print(f"name在列表中的下标索引值是：{index}")

# 列表的修改功能
# 修改特定位置（索引）的元素值：
# 语法：列表[下标]=值
my_list[-1] = "grade"
print(my_list)
# 正向下标
my_list = [1, 2, 3]
my_list[0] = 5
print(my_list)
# 反向下标
my_list = [1, 2, 3]
my_list[-3] = 5
print(my_list)

# 2 插入元素：
# 语法：列表.insert(下标，元素)，在指定的下标位置，插入指定的元素
my_list = [1, 2, 3]
my_list.insert(1, "good")
print(my_list)
print(my_list.index(3))

# 3 追加元素：
# 语法：列表.append(元素)，将指定元素，追加到列表的尾部
my_list.append(7)
print(my_list)
my_list.append([4, 5, 6])
print(my_list)

# 4 追加元素方式2：(追加一批)
# 语法：列表.extend(其他数据容器)，将其它数据容器的内容取出，依次追加到列表尾部
my_list.extend([8, 9, 10])
print(my_list)

# 删除元素：
# 5 语法1：del 列表[下标]
del my_list[1]
print(my_list)

# 6 语法2：列表.pop(下标)   取出返回
element=my_list.pop(1)
print(f"取出的元素是{element}")
print(my_list)

# 7 删除某元素在列表中的第一个匹配项
# 语法：列表.remove(元素)
my_list=[1,2,4,5,9,5,3,6,8]
my_list.remove(5)
print(my_list)

# 8 清空列表内容
# 语法：列表.clear()
my_list.clear()
print(my_list)

# 9 统计某元素在列表内的数量
# 语法：列表.count(元素)
my_list=[1,3,2,4,1,5,3,1,3,1,1]
print(my_list.count(1))
my_list=["Tu","Yun","Tu","Tu","Zhang","Huang"]
print(my_list.count("Tu"))

# 10 统计列表内，有多少元素
# 语法：len(列表)    可以得到一个int数字，表示列表内的元素数量
my_list=[13,3,5,6,4,7,8,6,8,5,4,23,4,3,76,77,45,34,97]
my_list_len=len(my_list)
print(my_list_len)

# 练习案例：常用功能练习
my_list=[21,25,21,23,22,20]
my_list.append(31)
my_list.extend([29,33,30])
num1=my_list[0]
print(num1)
num2=my_list[-1]
print(num2)
index=my_list.index(31)
print(index)
print(my_list)

# list(列表)的遍历
# while循环（循环条件：定义一个变量表示下标，从0开始；循环条件为 下标值<列表的元素数量）
# index=0
# while index<len(列表):
#     元素=列表[index]
#     对元素进行处理
#     index+=1
def list_while_func():

    # 使用while循环遍历列表
    # :return:None

    my_list = ["传智教育", "黑马程序员", "python"]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

list_while_func()

# for循环
# for 临时变量 in 数据容器:
#     对临时变量进行处理
def list_for_func():

    # 使用for循环遍历列表
    # :return: None

    my_list= [1,2,3,4,5]
    for x in my_list:
        print(x)

list_for_func()

# 练习案例：取出列表内的偶数
def while_two():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    index = 0
    while index<len(my_list):
        if my_list[index]%2==0:
            new_list.append(my_list[index])
        index+=1
    print(f"通过while循环，从列表：{my_list}中取出偶数，组成新列表：{new_list}")
while_two()

def for_two():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    for x in my_list:
        if x % 2 == 0:
            new_list.append(x)
    print(f"通过for循环，从列表：{my_list}中取出偶数，组成新列表：{new_list}")
for_two()

from itertools import count

# 数据容器：tuple(元组)   元组一旦定义完成，就不可修改
# 定义元组：用小括号，逗号隔开每个数据，数据可以是不同的数据类型

# 定义元组字面量
# (元素,元素, ...... ,元素)
# 定义元组变量
# 变量名称 = (元素,元素, ...... ,元素)
t1 = (1, 3.14, "name", True)  # 定义3个元素的元组
print(f"{t1}的类型是：{type(t1)}")

t4 = ('hello',)  # 定义一个元素的元组，必须带有逗号，否则不是元组类型
print(f"{t4}的类型是：{type(t4)}")

# t5=("hello")    # 定义一个元素的元组，必须带有逗号，否则不是元组类型
# print(f"{t5}的类型是：{type(t5)}")

# 定义空元组
# 变量名称 = ()     方法1
# 变量名称 = tuple()     方法2
t2 = ()
t3 = tuple()
print(f"{t2}的类型是：{type(t2)}")
print(f"{t3}的类型是：{type(t3)}")

# 元组的嵌套
t5 = ((1, 2, 3), 4, 5, (6, 7))
print(f"{t5}的类型是：{type(t5)}")

# 下标索引取出元素
print(t5[-1][0])

# 元组的操作
t6 = (3, 5, 2, 5, 6, 3, 4, 2, 5, 6)
# index查找方法
index_6 = t6.index(6)
print(index_6)
# count统计方法
count_3 = t6.count(3)
print(count_3)
# len函数统计元组元素数量
len_t6 = len(t6)
print(len_t6)

# 元组的遍历：while
index = 0
t7 = (34, 5, 64, 6, 6, "a", 23, "b", 4, 3, 4)
while index < len(t7):
    print(t7[index], end=" ")
    index += 1
print()

# 元组的遍历：for
for x in t7:
    print(x, end=" ")
print()

# 尝试修改元组内容
# t=(2,3,24,32)
# t[2]=54    错误，不可修改
t8 = (3, 2, 4, 3, [35, 56, 43], 9)  # 元组里面嵌套列表可以修改里面的列表
t8[4][2] = 99
print(t8)

# 练习案例：元组的基本操作
tt = ('周杰lun', 11, ['football', 'music'])
index_age = tt.index(11)
print(f"年龄所在的下标位置：{index_age}")
print(f"学生的姓名为：{tt[0]}")
del tt[-1][0]
tt[-1].append("coding")
print(tt)

# 字符串（数据容器）
# 通过下标获取特定位置字符
name = "python"
print(name[0])  # p
print(name[-1])  # n
my_str = "learn python learning"
elem = my_str[7]
elem2 = my_str[-14]
print(f"从字符串{my_str}取下标为1的元素值是：{elem}")
print(f"从字符串{my_str}取下标为-14的元素值是：{elem2}")
# 同元组一样，字符串是无法修改的，若要修改则得到一个新的字符串
# 字符串的常用操作

# 查找特定字符串的下标索引值
# 语法：字符串.index(字符串)
print(my_str.index("python"))

# 字符串的替换
# 语法：字符串.replace(字符串1，字符串2)
# 功能：将字符串内的全部：字符串1，替换成字符串2
# 注意：不是修改字符串本身，而是得到了一个新字符串
str1 = my_str.replace("learn", "study")
print(my_str)
print(str1)

# 字符串的分割
# 语法：字符串.split(分割符字符串)
# 功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
# 字符串本身不变，而是得到了一个列表对象
my_list = my_str.split()
print(my_list)

# 字符串的规整操作(去前后空格)
# 语法：字符串.strip()
my_str = "   learn python studying    "
print(my_str.strip())  # 不传入参数，去除首尾空格 默认
print(my_str.strip(" "))  # 传入空格

# 字符串的规整操作(去前后指定字符串)
# 语法：字符串.strip(字符串)
my_str = "23 learn python studying 4353332323"
print(my_str.strip("23"))
# 注意：传入的是"23"，其实就是："1"和"2"都会移除，是按照单个字符

# 统计字符串中某字符串的出现次数
my_str = " 25i45d"
count = my_str.count("2")
print(f"{my_str}中2的个数为：{count}")

# 统计字符串的长度
len_str = len(my_str)
print(f"{my_str}的长度为：{len_str}")

# 字符串的遍历
my_str = "黑马程序员"
for x in my_str:
    print(x, end='')
print()

index = 0
while index < len(my_str):
    print(my_str[index], end='')
    index += 1

# 练习案例：分割字符串
str_fg="itheima itcast boxuegu"
str_count=str_fg.count("it")
print(f"字符串{str_fg}中有：{str_count}个it字符")
str_replace=str_fg.replace(" ","|")
print(f"字符串itheima itcast boxuegu，被替代空格后，结果：{str_replace}")
str_split=str_fg.split("|")
print(f"字符串itheima|itcast|boxuegu，被替代空格后，结果：{str_split}")

# 数据容器（序列）的切片
# 切片操作
# 对list进行切片，从1开始，4结束，步长1
my_list=[1,24,32,5543,657,323]
result1=my_list[1:4]
print(result1)
# 对list进行切片，从3开始，到1结束，步长-1
result2=my_list[3:1:-1]
print(result2)
# 对tuple进行切片，从头开始，到最后结束，步长1
my_tuple=(24,65,634,2,45,33)
result3=my_tuple[:]
print(my_tuple)
# 对tuple进行切片，从头开始，到尾结束，步长-2
result4=my_tuple[::-2]
print(result4)
# 对str进行切片，从头开始，到最后结束，步长2
my_str="728746328271"
result5=my_str[::2]
print(result5)
# 对str进行切片，从头开始，到最后结束，步长-1
result6=my_str[::-1]    # 相当于将序列反转了
print(result6)

# 学习案例：序列的切片实践 得到“黑马程序员”
# 方法一
my_str="万过薪月，员序程马黑来，nohtyp学"
result1=my_str[::-1]
result2=result1.split("，")
result3=result2[1].replace("来","")
print(result3)

result7=my_str.split("，")[1][4::-1]
print(result7)
# 方法二
result4=my_str[::-1][9:14]
print(result4)
# 方法三
result5=my_str[9:4:-1]
print(result5)
# 方法四
result6=my_str[5:10][::-1]
print(result6)

# 集合set（数据容器）
# 集合的定义基本语法
# 定义集合自变量
# {元素,元素,……,元素}
# 定义集合变量
# 变量名称={元素,元素,……,元素}
# 定义空集合
# 变量名称=set()
my_set1={124,534,6,"sf",556,124}
my_set2=set("2gfd65646783ghf")
print(my_set1)
print(my_set2)
# 添加新元素
my_set={"hello","happy","nice","hello","good","morning"}
my_set.add("python")
my_set.add("nice")
print(my_set)
# 移除元素
my_set.remove("hello")
print(my_set)
# 从集合中随机取出元素
# 语法：集合.pop   从集合中随机取出一个元素
element=my_set.pop()
print(f"取出的元素为：{element}")
print(f"取出后集合为{my_set}")
# 清空集合，clear
my_set.clear()
print(my_set)

# 1.得到new=1中2无
# 2.改变set1=1中删2有

# 取两个集合的差集
# 取出集合1中有而集合2没有的，得到一个新集合，集合1和集合2不变
set1={1,2,3}
set2={2,4,5}
set3=set1.difference(set2)
print(set1)
print(set2)
print(set3)
# 消除两个集合的差集
#在集合1的内部删除和集合2相同的元素
set1.difference_update(set2)
print(set1)
print(set2)

# 2个集合合并 去重
set3=set1.union(set2)
print(set1)
print(set2)
print(set3)

# 统计集合元素数量(len)
set3_len=len(set3)
print(set3_len)     # 5个
# 去重
set3_len2={1,2,3,4,5,1,2,3,4,5}
print(len(set3_len2))  # 5个

# 集合的遍历
# 集合不支持下标索引，不能用while循环
# 可以使用for循环
set1={1,2,3,4,5}
for x in set3:
    print(x,end=' ')


# test:信息去重
my_list=['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
my_set=set()
for element in my_list:
    my_set.add(element)
print(f"列表的内容是：{my_list}")
print(f"通过for循环后，得到的集合对象是：{my_set}")

# 字典的定义：

# 定义字典字面量
# {key:value,key:value,······,key:value}
my_dict1={"王力宏":99,"关鹏":88,"王红":77}

# 定义字典变量
# my_dict={key:value,key:value,······,key:value}

# 定义空字典
my_dict2={}   #1
my_dict3=dict()   #2

print(f"内容：{my_dict1},类型：{type(my_dict1)}")
print(f"内容：{my_dict2},类型：{type(my_dict2)}")
print(f"内容：{my_dict3},类型：{type(my_dict3)}")

# key重复的话，保留的是最后一个
my_dict1={"关鹏":99,"关鹏":88,"王红":77}
print(f"重复key的字典内容是：{my_dict1}")

# 字典同集合一样，不可以使用下标索引，但是可以通过key值来取得对应的value
my_dict1={"王力宏":99,"关鹏":88,"王红":77}
score=my_dict1["王力宏"]
print(f"王力宏的考试分数：{score}")

# 字典的嵌套
# 字典的key和value可以是任意数据类型（key不可以为字典）
# 记录学生各科的考试信息
my_dict={"王力宏":{"语文":77,"数学":66,"英语":33},
         "周杰伦":{"语文":88,"数学":86,"英语":55},
         "林俊杰":{"语文":99,"数学":96,"英语":66}
         }
# 从嵌套字典中获取数据
print(f"林俊杰的各科成绩为：{my_dict["林俊杰"]}")
print(f"周杰伦语文成绩为：{my_dict["周杰伦"]["语文"]}")

# 字典常用操作
# 新增元素
# 语法：字典[key]=value  结果：若key不存在，则字典被修改，新增元素
my_dict1={"王力宏":99,"关鹏":88,"王红":77}
my_dict1["张三"]=83
print(my_dict1)

# 更新元素
# 语法：字典[key]=value  结果：字典被修改，元素被更新
my_dict1={"王力宏":99,"关鹏":88,"王红":77}
my_dict1["王力宏"]=92
print(my_dict1)

# 删除元素
# 语法：字典.pop(key)  结果：获得指定key的value，同时字典被修改，指定key的元素的数据被删除
my_dict1={"王力宏":99,"关鹏":88,"王红":77}
value=my_dict1.pop("王力宏")
print(value)
print(my_dict1)

# 清空元素
# 语法：字典.clear()
my_dict1.clear()
print(my_dict1)

# 获取全部的key
# 语法：字典.keys()  结果：得到字典中全部key
my_dict1={"张三":93,"关鹏":88,"王红":77}
keys=my_dict1.keys()
print(keys)

# 遍历字典
# 方式一：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict1[key]}")
# 方法二：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict1:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict1[key]}")

# 统计字典的元素数量，len函数
num=len(my_dict1)
print(f"my_dict1中的元素数量为：{num}")

# test:升职加薪
my_dict={
    "王力鸿":{"部门":"科技部","工资":3000,"级别":1},
    "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
    "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
    "张学友":{"部门":"科技部","工资":4000,"级别":1},
    "刘德华":{"部门":"市场部","工资":6000,"级别":2}
}
print("全体员工当前信息如下：")
print(my_dict)

for key in my_dict:
    if my_dict[key]["级别"]==1:
        my_dict[key]["级别"]=2
        my_dict[key]["工资"]+=1000
print("全体员工级别为1的员工完成升职加薪操作，操作后：")
print(my_dict)

# 通用排序
my_set={423,54,623,4,1,24,5,3,6}
my_list=[1,2,3,4,2,53,6,4,765,8,6,32]
print(sorted(my_list))
print(sorted(my_set))
print(sorted(my_list,reverse=True))
print(sorted(my_set,reverse=True))

# ASCII码
# 大小写英字母 数字 特殊符号（！、\、|、@、#、空格等）都有对应的ASCII值
# 字符串