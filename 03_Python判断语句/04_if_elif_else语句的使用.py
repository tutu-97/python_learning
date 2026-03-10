"""
演示if elif else 多条件判断语句的使用
"""

# 通过if判断，可以使用多条件判断的语法
# 第一个条件就是if
if int(input("请输入你的身高（cm）：")) < 120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级（1-5）：")) > 3:
    print("vip级别大于3，可以免费。")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天是1号免费日，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元。")

# if elif else语句进行多条件判断
# 从datetime模块导入datetime类
from datetime import datetime
now = datetime.now()
day = now.day
print(now)
print("欢迎来到黑马动物园。")
height=int(input("请输入你的身高（cm）："))
if height<120:
    print("您的身高小于120cm，可以免费游玩。")
elif day==7:
    print("今天是7号免费日，可以免费游玩。")
else:
    vip_level=int(input("请输入你的vip级别（1~5):"))
    if vip_level==3:
        print("您的vip级别等于3，可以享受半价。")
    elif vip_level>3:
        print("您的vip级别大于3，可以免费游玩。")
    else:
        print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快。")

