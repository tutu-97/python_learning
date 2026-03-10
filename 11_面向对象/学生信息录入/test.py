class Student:
    def __init__(self):
        for i in range(1, 10):
            print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
            self.name=input("请输入学生姓名：")
            self.age=input("请输入学生年龄：")
            self.address=input("请输入学生地址：")
            print(f"学生{i}信息录入完成，信息为：【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】")

stu=Student()