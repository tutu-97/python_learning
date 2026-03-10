"""
演示对函数（方法）进行类型注解
"""

# 对形参进行类型注解
# 语法：daf 函数方法名(形参:类型, 形参:类型···):
def add(x: int, y: int):
    return x + y

# 对返回值进行类型注解
# 语法：def 函数方法名(形参:类型, 形参:类型···) -> 返回值类型:
def func(data: list) -> list:
    return data

print(func(1))
