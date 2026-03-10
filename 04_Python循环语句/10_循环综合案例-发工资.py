age = int(input("请输入您的年龄："))
if age >= 18:
    if age < 30:
        print("年龄满足继续判断")
        if int(input("请输入您入职已有多少年：")) > 2:
            print("年龄符合且入职超过2年，满足条件，可以领取")
            exit()
        else:
            print("入职时间不满足继续判断")
        if int(input("请输入您的职位级别：")) > 3:
            print("年龄符合且级别超过3级，满足条件，可以领取")
        else:
            print("不好意思，您不满足领取条件")
    else:
        print("不好意思，年龄大于30岁，不满足领取条件。")
else:
    print("不好意思，年龄小于18岁，不满足领取条件。")


# 练习案例：发工资
salary = 10000
for i in range(1, 21):
    import random
    grade = random.randint(1, 10)
    if grade < 5:
        print(f"员工{i}，绩效分{grade},低于5，下一位。")
        continue
    """
        else:
        salary-=1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{salary}元。")
    if salary==0:
        print("工资发完了，下个月领取吧")
        break
    """
    if salary >= 1000:
        salary -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{salary}元。")
    else:
        print("工资发完了，下个月领取吧")
        # break结束发放
        break