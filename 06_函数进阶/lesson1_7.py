
# 函数的多返回值
# 按照返回值的顺序，写对应顺序的多个变量接收即可
# 变量之间用逗号隔开
# 支持不同类型的数据return
def test_retrun():
    return 'a',2

x,y=test_retrun()
print(x)
print(y)

# 函数的多种传参方式
def user_info(name,age,gender):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

# 位置参数：调用函数时根据函数定义的参数位置来传递参数
# 传递的参数和定义的参数的顺序及个数必须一致
user_info("Tom",18,"男")

# 关键字参数：函数调用时通过”键=值“形式传递参数
# 作用：清晰、容易使用，消除了参数的顺序需求
# 函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序

# 关键字传参
user_info(name="Tom",age=20,gender='男')
# 可以不按照固定顺序
user_info(age=19,name="Tom",gender="男")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("小明",age=20,gender="男")

# 缺省参数：也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值
# 注意：所有位置参数必须出现在默认参数前，包括函数定义和调用
# 作用：当调用函数时没有传递参数，就会使用默认是用缺省参数对应的值
# 设置默认参数时，写在后面
def user_info(name,age,gender='男'):
    print(f"您的名字是{name},年龄是{age},性别是{gender}")

user_info('Tom',20)
user_info('Rose',18,'女')

# 不定长参数
# 不定长参数也叫可变参数，用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
# 作用：当调用函数时不确定参数个数时，可以使用不定长参数
# 不定长参数的类型：位置传递、关键字传递

# 位置传递
# 传进的所有参数都会被args变量收集，它会根据传进参数的位置合并成一个元组（tuple），args是元组类型，这就是位置传递
def user_info(*args):

    print(type(args))
    print(len(args))
    print(args)

# ('Tom',)
user_info('Tom')
# ('Tom',18)
user_info('Tom',18)

# 关键字传递
# 参数是“键=值”形式的情况下所有的“键=值”都会被kwargs接受，同时会根据“键=值”组成字典
def user_info(**kwargs):
    print(type(kwargs))
    print(kwargs)

# {'name':'Tom','age':18,'id':110}
user_info(name='Tom',age=18,id=110)


# 匿名函数

# 函数作为参数传递
# 计算逻辑的传递，而非数据的传递
# 任何逻辑都可以自行定义并作为函数传入
def test_func(compute):
    result=compute(1,2)
    print(result)

def compute(x,y):
    return x+y
# 函数compute作为参数，传入test_func函数中使用
test_func(compute)

# lambda匿名函数

# def关键字，可以定义带有名称的函数
# lambda关键字，可以定义匿名函数（无名称）
# 有名称的函数，可以基于名称重复使用
# 无名称的匿名函数，只可临时使用一次

# 定义语法：  lambda传入参数：函数体（一行代码）
# 函数体只能写一行，无法写多行代码
def test_func(compute):
    result=compute(1,2)
    print(result)
# 通过lambda关键字，传入一个一次性使用的lambda匿名函数
test_func(lambda x,y:x*y)
