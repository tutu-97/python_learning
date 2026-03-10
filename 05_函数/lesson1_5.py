
# 函数
str1 = "hellow world"
str2 = "happy new year"
str3 = "python"
# 直接求str1的长度
count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")
# 定义函数 （已组织好的 可重复使用 针对特定功能）
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是：{count}")
# 用函数求长度
my_len(str1)
my_len(str2)
my_len(str3)


# 函数的定义:
# def 函数名(传入参数)
#     函数体
#     return 返回值

# 注意事项：
# 参数不需要，可以省略（后续章节讲解）
# 返回值如不需要，可以省略（后续章节讲解）
# 函数必须先定义后使用

def say_hi():
    print("Hi 我是黑马程序员，学python来黑马")
# 调用函数让定义的函数开始工作 ：函数名（参数）
say_hi()

# 练习案例：自动查核酸
def check_hs():
    print("欢迎来到黑马程序员！")
    print("请出示您的健康码以及72小时核酸证明！")

check_hs()

# 函数传入参数的使用 参数数量不限
# a和b是形式参数（形参）用逗号分割
def add(a,b):
    result=a+b
    print(f"{a}+{b}的结果是：{result}")
# 调用函数
# 5和6是实际参数（实参）用逗号分割
add(5,6)
add(1345612,32647826)

# 练习案例：升级版自动查核酸
def check2(temperature):
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    if temperature<=37.5:
        print("体温测量中，您的体温是：%.1f，体温正常请进！"%temperature)
    else:
        print("体温测量中，您的体温是：%.1f，需要隔离！" %temperature)
# 调用函数
import random
t = random.uniform(36, 39)
check2(t)

# 函数返回值
def add(a,b):
    result=a+b
    return result

r=add(5,7)
print(r)

# 返回值None类型,可以主动使用return返回，效果等同于不写return语句
def say_hello():
    print("Hello...")

result=say_hello()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

def say_hello2():
    print("Hello...")
    return None

result2=say_hello()
print(f"有返回值None函数，返回的内容是：{result2}")
print(f"有返回值None函数，返回的内容类型是：{type(result2)}")

# None的if判断
def check_age(age):
    if age>18:
        return "Success"
    else:
        return None

result1=check_age(16)
result2=check_age(25)
print(result1)
print(result2)
# None等同于False
# if result1(为False)则表示假
# if not result1 则为真
# if语句中，为真则执行，为假则不执行
if not result1:
    print("未成年，不可进入")
if result1:
    print("111")
if result2:
    print("已成年，可进入")

# None用于声明无初始内容的变量
name=None

# 函数的说明
# 语法：
# def func(x,y):
#     三个双引号
#     :param x:形参x的说明
#     :param y: 形参y的说明
#     :return: 返回值的说明
#     三个双引号
#     函数体
#     return 返回值
def add(x,y):
    # 三个双引号
    # add函数可以接收2个参数，进行2数相加的功能
    # :param x:形参x表示相加的其中一个数字
    # :param y:形参y表示相加的另一个数字
    # :return:返回值是2数相加的结果
    # 三个双引号
    result=x+y
    print(f"两数相加的结果是：{result}")
    return result
add(5,6)

# 函数的嵌套调用
def fun_1():
    print("---1---")
def fun_2():
    print("---2---")
    fun_1()
    print("---3---")
fun_2()

# 变量在函数中的定义域
# 局部变量（函数内部，函数调用完成即销毁）
def test_a():
    num = 100
    print(num)

# print(num)无法运行
test_a()
# 全局变量（定义在函数外部，内外都能生效）
n = 10
def test_b():
    print(n)
test_b()
print(n)

# global关键字

# num = 700
# def test_a():
#     print("a",num)
#
# def test_b():
#     num=300
#     print("b",num)
# test_a()
# test_b()
# print(num)

# 在函数内修改全局变量
num = 700
def test_a():
    print("a",num)

def test_b():
    # global关键字声明a是全局变量
    global num
    num=300
    print("b",num)
test_a()
test_b()
print(num)

# 综合案例：黑马ATM
def query(n,m):
    print("---------------查询余额---------------")
    print(f"{n}，您好，您的余额剩余：{m}元")
    menu(n, m)

def store(n, m):
    print("----------------存款----------------")
    store_money=int(input("请输入你要存的金额："))
    m= m + store_money
    print(f"{n}，您好，您存款{store_money}元成功")
    print(f"{n}，您好，您的余额剩余：{m}元")
    menu(n, m)

def withdraw(n, m):
    print("----------------取款----------------")
    get_money = int(input("请输入你要取的金额："))
    m = m - get_money
    print(f"{n}，您好，您取款{get_money}元成功")
    print(f"{n}，您好，您的余额剩余：{m}元")
    menu(n, m)

def menu(n, m):
    print("----------------主菜单----------------")
    print(f"{n}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    choice=int(input("请输入您的选择："))
    if choice==1:
        query(n,m)
    elif choice==2:
        store(n, m)
    elif choice==3:
        withdraw(n, m)
    elif choice==4:
        exit()
    else:
        print("输入错误！")
        exit()

name = input("请输入你的姓名：")
money= 5000000
menu(name,money)

money=5000000
name=input("请输入你的姓名：")
def query(show_header):
    if show_header:
        print("---------------查询余额---------------")
    print(f"{name}，您好，您的余额剩余：{money}元")

def saving():
    print("----------------存款----------------")
    store_money = int(input("请输入你要存的金额："))
    global money
    money += store_money
    print(f"{name}，您好，您存款{store_money}元成功")
    query(False)

def get_money():
    print("----------------取款----------------")
    get_money = int(input("请输入你要取的金额："))
    global money
    money = money - get_money
    print(f"{name}，您好，您取款{get_money}元成功")
    query(False)

def main():
    print("----------------主菜单----------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入您的选择："))

while True:
    choice = main()
    if choice == 1:
        query(True)
    elif choice == 2:
        saving()
    elif choice == 3:
        get_money()
    elif choice == 4:
        print("退出成功！")
        exit()
    else:
        print("输入错误！")
        exit()