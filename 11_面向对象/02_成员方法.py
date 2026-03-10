"""
演示面向对象类中的成员方法定义和使用
"""

# 定义一个带有成员方法的类
# class 类名称:
class Student:
    # 类的属性 成员变量
    name = None     # 学生的姓名
    # 类的行为 函数 成员方法
    # define 方法名(self,形参1，···,形参N):
    #        方法体
    # self关键字：self关键字是成员方法定义的时候，必须填写的
    # 用来表示类对象自身的意思
    # 当我们使用类对象调用成员方法时，self会自动被python传入
    # 在方法内部，想要访问类的成员变量，必须使用self
    def say_hi(self):
        print(f"大家好呀，我是{self.name}，欢迎大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是：{self.name}，{msg}")

# 创建类对象： 对象=类名称()
stu = Student()
stu.name = "周杰轮"
stu.say_hi()
stu.say_hi2("哎哟不错哟")

stu2 = Student()
stu2.name = "林俊节"
stu2.say_hi()
stu2.say_hi2("小伙子我看好你")
