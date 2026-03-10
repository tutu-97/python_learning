
# bool True:1 False:0
# 定义变量存储布尔类型的数据
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1},类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2},类型是：{type(bool_2)}")
# 比较运算符的使用 ==,!=,>,<,>=,<=
result = 10
print(f"10的结果是：{result},类型是：{type(result)}")
result = 10 > 5
print(f"10>5的结果是：{result},类型是：{type(result)}")
result = 10 < 5
print(f"10<5的结果是：{result},类型是：{type(result)}")
result = "world" == "word"
print(f"world和word是否相等的结果是：{result},类型是：{type(result)}")
result = "world" != "word"
print(f"world和word是否不相等的结果是：{result},类型是：{type(result)}")
result = 10 >= 10
print(f"10>=10的结果是：{result},类型是：{type(result)}")
result = 12 >= 10
print(f"12>=10的结果是：{result},类型是：{type(result)}")
result = 10 <= 10
print(f"10<=10的结果是：{result},类型是：{type(result)}")
result = 12 <= 10
print(f"12<=10的结果是：{result},类型是：{type(result)}")

# 逻辑判断语句（if）
age=int(input("请输入年龄："))
if age>=18:
    print("已成年")
if age<18:
    print("未成年")
print("时间过得真快啊")
truth=input("小美是否喜欢我？（喜欢/不喜欢）：")
if truth=="喜欢":
    print("明天我一定要去表白")
if truth == "不喜欢":
    print("算了，明天我不去表白了")

# 练习案例：成年人判断
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元。")
print("祝您游玩愉快。")

#if else组合判断语句
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age=int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要买票10元。")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快。")

# 练习案例：我要买票吗
print("欢迎来到黑马动物园。")
height=int(input("请输入你的身高（cm）："))
if height>120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快。")

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

# 练习案例：猜猜心里数字
import random
num = random.randint(1, 100)
if int(input("请输入第一次猜想的数字：")) == num:
    print("恭喜你猜对了。")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜你猜对了。")
elif int(input("不对，再猜最后一次：")) == num:
    print("恭喜你猜对了。")
else:
    print("Sorry，全部猜错啦，我想的是：", num)

# 判断语句的嵌套使用
from datetime import datetime
now=datetime.now()
day=now.day
print(now)
print("欢迎来到黑马动物园。")
if day!=1:
    if int(input("你的身高是多少："))>120:
        print("很遗憾，你的身高大于120cm，不可以免费游玩。")
        print("如果你的vip级别大于3，可以免费。")
        if int(input("请告诉我你的vip级别："))>3:
            print("恭喜你，你的vip级别大于3，可以免费游玩。")
        else:
            print("Sorry,你需要补票10元。")
    else:
        print("欢迎你小朋友，可以免费游玩。")
else:
        print("今天是会员日，可以免费游玩。")

# 公司发礼物 必须是大于等于18岁小于30岁的成年人；同时入职时间需满足大于两年，或者级别大于3才可领取
age=int(input("请输入你的年龄："))
if age>=18:
    if age<30:
        print("年龄满足")
        if int(input("你的入职时间："))>2:
            print("年龄和入职时间都达标，恭喜你可以领取礼物。")
        elif int(input("你的级别是："))>3:
            print("年龄和级别都达标，恭喜你可以领取礼物。")
        else:
            print("年龄满足，但入职时间和级别不满足，不可领取礼物。")
    else:
        print("年龄过大，不可领取礼物。")
else:
    print("你未成年，不可领取礼物。")

# 猜数字的实战案例
import random

num = random.randint(1, 10)
num_1 = int(input("请输入第一次猜的数字(1~10):"))
if num_1 != num:
    if num_1 > num:
        print("大了！")
    else:
        print("小了！")
    num_2 = int(input("请输入第二次猜的数字(1~10):"))
    if num_2 != num:
        if num_2 > num:
            print("大了！")
        else:
            print("小了！")
        num_3 = int(input("请输入最后一次猜的数字(1~10):"))
        if num_3 != num:
            if num_3 > num:
                print("大了！")
            else:
                print("小了！")
            print("不好意思，游戏结束，三次都没猜中。")
        else:
            print("恭喜你最后一次猜中了！")
    else:
        print("恭喜你第二次猜中了！")
else:
    print("恭喜你第一次就猜中了！")
