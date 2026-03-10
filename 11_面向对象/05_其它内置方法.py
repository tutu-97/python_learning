"""
演示Python内置的各类魔术方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name        # 学生姓名
        self.age = age          # 学生年龄

    # __str__魔术方法
    # 控制类转换为字符串，正常输出为地址，使用之后可以得到具体值的字符串
    def __str__(self):
        return f"Student类对象，name:{self.name}, age:{self.age}"

    # __lt__魔术方法
    # 小于或大于符号的比较方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    # 小于等于或大于等于符号的比较方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    # 不实现__eq__方法，对象之间可以比较，但是是比较内存地址，也即是：不同对象==比较一定是False结果
    # 实现__eq__方法，就可以按照自己的想法来决定2个对象是否相等了
    def __eq__(self, other):
        return self.age == other.age

# __str__
stu1 = Student("周杰轮", 31)
print(stu1)
print(str(stu1))

# __lt__
stu1 = Student("周杰轮", 31)
stu2 = Student("林俊节", 36)
print(stu1 < stu2)
print(stu1 > stu2)   # 大于python会自动反向调用方法实现逻辑等价，转换成stu2<stu1

# __le__
stu1 = Student("周杰轮", 31)
stu2 = Student("林俊节", 36)
print(stu1 <= stu2)
print(stu1 >= stu2)

# __eq__
stu1 = Student("周杰轮", 31)
stu2 = Student("林俊节", 36)
print(stu1 == stu2)






