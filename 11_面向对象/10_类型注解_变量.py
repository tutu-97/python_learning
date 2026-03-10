"""
演示变量的类型注解
"""

# 基础数据类型注解
# 语法：变量:类型
import json
import random
# 自动导包：Alt+Enter

# var_1: int = 10
# var_2: str = "itheima"
# var_3: bool = True


# 类对象类型注解
# 语法：对象名:类名
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"itheima": 666}


# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "itheima", True)
my_dict: dict[str, int] = {"itheima": 666}


# 在注释中进行类型注解：函数的形参和返回值的类型注释
# 语法：# type:类型
var_1 = random.randint(1, 10)   # type: int
var_2 = json.loads('{"name": "zhangsan"}')  # type: dict[str, str]
def func():
    return 10
var_3 = func()  # type: int

# 类型注解的限制
var_4: int = "itheima"
var_5: str = 123

# 为变量设置注释，显示的变量定义，一般无需注释
# 一般，无法直接看出变量类型时会添加变量的类型注释
# 类型注释主要功能在于帮助第三方IDE工具对代码进行类型推断，协助做代码提示；帮助开发者自身对变量进行类型注释（备注），并不会报错