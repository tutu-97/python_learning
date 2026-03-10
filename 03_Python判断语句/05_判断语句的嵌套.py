"""
演示判断语句的嵌套使用
"""

# if int(input("你的身高是多少：")) > 120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果vip级别大于3，可以免费")
#
#     if int(input("你的vip级别是多少：")) > 3:
#         print("恭喜你，vip级别达标，可以免费")
#     else:
#         print("Sorry 你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩。")


age = 11
year = 1
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")

    else:
        print("不好意思，年龄太大了")

else:
    print("不好意思，小朋友不可以领取。")


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

