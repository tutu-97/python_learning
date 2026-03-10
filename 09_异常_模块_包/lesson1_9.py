
# 异常的概念
# 程序运行过程中出现了错误 异常 BUG

# 异常处理（捕获异常）
# 当程序遇到了BUG，那么会有两种情况
# ①整个程序因为一个BUG停止运行     一般是这种情况
# ②对BUG进行提醒，整个程序继续运行     希望达到这种情况（则需要用到捕获异常）
# 捕获异常的作用:提前假设某处会出现异常，做好提前准备，当真的出现异常的时候，可以有后续手段

# 基本语法：
# try:
#   可能发生错误的代码
# except:
#   如果出现异常执行的代码

# 基本捕获语法
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
# 捕获多个异常
except:
    print("出现异常了，因为文件不存在，我将open的模式，改为模式去打开")
    f=open("D:/abc.txt","w",encoding="UTF-8")

from errno import ENAMETOOLONG

# 捕获指定异常
# 基本语法：
# try:
#   print(name)
# except NameError as e:    e:别名
#   print("name变量名称未定义错误")

# 注意事项
# ①如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。
# ②一般try下方只放一行尝试执行的代码。

try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常:可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
# try:
#   print(1/0)
# except (NameError,ZeroDivisionError):
#   print("'ZeroDivision'错误...")
try:
    print(name)
    # 1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未命名 或者 除以0的异常错误")
    print(e)

try:
    # print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print("出现了变量未命名 或者 除以0的异常错误")
    print(e)

# 捕获所有异常：基本捕获 或者 类型Exception
# ① except:
# ② except Exception:

try:
    1/0
except Exception as e:
    print("出现异常了")
    print(e)

# 异常else else表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("我是else，是没有异常的时候执行的代码")

# 异常的finally  finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f=open("D:/abc.txt","r",encoding="UTF-8")
except Exception as e:
    f=open("D:/abc.txt","w",encoding="UTF-8")
else:
    print("没有异常")
finally:
    f.close()

# 异常的传递、
# 异常是具有传递性的
# 当函数fun01中发生异常，并且没有捕获处理这个异常的时候，异常会传递到函数fun02
# 当函数fun02也没有捕获处理这个异常的时候，main函数会捕获这个异常，这就是异常的传递性
def fun01():
    print("这里是fun01开始")
    num=1/0
    print("这里是fun01结束")

def fun02():
    print("这里是fun02开始")
    fun01()
    print("这里是fun02结束")

def main():
    try:
        fun02()
    except Exception as e:
        print(e)
    # fun02()
main()
# 提示：当所有函数都没有捕获异常的时候，程序就会报错

# python模块：模块的导入、自定义模块

# 什么是模块：python模块是一个python文件，以.py结尾
# 模块能定义函数，类和变量，模块里面也能包含可执行的代码
# 模块的作用：python中有很多各种不同的模块，每一个模块都可以帮助我们快速地实现一些功能，比如实现和时间相关的功能就可以使用time模块
#           我们可以认为一个模块就是一个工具包，每一个工具包中都有各种不同的工具供我们使用进而实现各种不同的功能
# 通俗说：模块就是一个python文件，里面有类、函数、变量等，我们可以拿过来用（导入模块去使用）

# 模块的导入方式
# 模块在使用前需要先导入 导入语法如下：（中括号在语法中表示可选）
# [from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]

# 常用组合形式如：
# import 模块名
# from 模块名 import 类、变量、方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

# import模块名
# 基本语法:
# import 模块名
# import模块名1,模块名2
# 模块名.功能名()
# 案例:导入time模块
import time   # 导入python内置的time模块(time.py这个代码文件)
print("开始")
# 让程序睡眠1秒(阻塞)
time.sleep(1)
print("结束")

# from 模块名 import 功能名
# 功能名()
# 案例:导出time模块中的sleep方法
from time import sleep
print("开始")
# 让程序睡眠1秒(阻塞)
sleep(1)
print("结束")

# 使用 * 导入time模块的全部功能
from time import *   # *表示全部的意思
print("开始")
# 让程序睡眠1秒(阻塞)
# 与import time:(time.sleep)的区别是调用方法不一样
sleep(1)
print("结束")

# as定义别名
# 基本语法：

# 模块定义别名
# import 模块名 as 别名
# 案例：
import time as tt
tt.sleep(2)
print("hello")

# 功能定义别名
# from 模块名 import 功能 as 别名
from time import sleep as sl
sl(2)
print("good")

# 自定义模块
# 制作自定义模块
# python中已经帮我们实现了很多的模块，不过有些时候我们需要一些个性化的模块，这里就可以通过自定义模块实现，自己制作一个模块
# 案例：新建一个python文件，命名为my_module.py，并定义test函数
# import my_module1
from my_module1 import test
test(10,20)
# 每个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必须要符合标识符命名规则

# 注意事项:当导入多个模块的时候，且模块内有同名功能。当调用这个同名功能的时候，调用到的是后面导入的模板的功能
# 模块1的代码
# def test(a,b):
#     print(a+b)

# 模块2的代码
# def test(a,b):
#     print(a-b)

# 导入模块和调用功能代码
from my_module1 import test
from my_module2 import test

# test函数是模块2中的函数
test(14,64)

# 测试模块：在py文件中添加一些测试信息，eg：在my_module1.py文件中添加测试代码test(1,1)
# def test(a,b):
#     print(a+b)
# test(51, 12)

# __main__变量
# if __main__=="__main__"表示，只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
from my_module1 import test

# __all__变量
# 如果一个模块文件中有‘__all__’变量，当使用‘from xxx import *’导入时，只能导入这个列表中的元素

# 这里all是test_A，所以导入所有(*)时只能导入test_A，也只能使用A不能调用B*     (my_module3)
# __all__=['test_A']
#
# def test_A():
#     print('testA')
#
# def test_B():
#     print('testB')

# from my_module3 import *
#
# test_A()


# python包：自定义包、安装第三方包
# python包：有__init__.py是package包，没有就是文件夹
# 物理上：包是一个文件夹，在该文件下包含了一个__init__.py文件，该文件夹可用于包含多个模块文件
# 逻辑上：包的本质依然是模块
# 作用：当我们的模块文件越来越多时，包可以帮助我们管理这些模块，但包的本质依然是模块

# 步骤如下：
# ①新建包‘my_package’
# ②新建包内模块：‘my_module1’和‘my_module2’
# ③模块内代码如下：
# my_module1模块中
# print(1)
#
# def info_print1():
#     print('my_module1')

# my_module2模块中
# print(2)
#
# def info_print2():
#     print('my_module2')

# 导入包

# 方法一：
# import 包名.模块名
# 包名.模块名.目标
# 包中的my_module1模块的info_print1()方法
# import my_package.module1
# import my_package.module2
# my_package.module1.info_print1()
# my_package.module2.info_print2()

# from my_package import module1
# from my_package import module2
# module1.info_print1()
# module2.info_print2()

# from my_package.module1 import info_print1
# from my_package.module2 import info_print2
# info_print1()
# info_print2()

# 方法二：
# 注意：必须在‘__init__.py’文件中添加‘__all__=[]'，控制允许导入的模板列表
# from 包名 import *
# 模块名.目标
# __all__控制的是import *
from my_package import *
module2.info_print2()
# module1.info_print1()     报错：模块1没有被导入，__init__.py文件中没有添加模块1
from my_package.module1 import *
info_print1()


# 安装第三方包
# 在Python程序的生态中，有许多非常多的第三方包(非Python官方)，可以极大的帮助我们提高开发效率，如:
# 科学计算中常用的:numpy包
# 数据分析中常用的:pandas包
# 大数据计算中常用的:pyspark、apache-flink包
# 图形可视化常用的:matplotlib、pyecharts
# 人工智能常用的:tensorflow等

# 安装第三方包-pip
# 安装easy，只需要使用python内置的pip程序即可
# 打开命令提示符程序：Ctrl+R
# 输入pip install 包名称
# eg：pip install numpy
# 即可通过网络快速安装第三方包

# pip的网络优化
# 由于pip是连接的国外的网站进行包的下载，所以有的时候会速度很慢
# 解决办法：通过如下命令，让其连接国内的网站进行包的安装：
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

# 安装第三方包-pycharm
# 解释器设置里面手动添加包（右下角）


# python异常、模块、包：综合案例
# 练习案例：自定义工具包
# 创建一个名为my_utils的包，里面包含两个模块：str_util.py(字符串相关工具)和file_util.py(文件处理相关工具)
# str_util.py模块中定义如下功能：
# 函数：str_reverse(s)，功能：将字符串s进行反转
# 函数：substr(s,x,y),按照下标x和y，对字符串进行切片
# str_util.py模块中定义如下功能：函数：
# 函数：print_file_info(file_name)，接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
# 函数：append_tofile(file_name，data)，接收文件路径以及传入数据，将数据追加写入到文件中
import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("abcdefg"))
print(my_utils.str_util.substr("abcdefg", 1, 4))

file_util.print_file_info("D:/个人/learning/python/bill.txt")
file_util.append_tofile("D:/个人/learning/python/bill.txt", "黑马程序员")