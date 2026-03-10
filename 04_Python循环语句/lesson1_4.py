
# while循环语句 用flag=True标记更好
import random
num=random.randint(1,100)
i=2
num_1=int(input("请输入第1次猜的数字(1~100):"))
while num_1!=num:
    if num_1>num:
        print("大了！")
        num_1=int(input("请输入第%d次猜的数字(1~100):"%i))
        i+=1
    else:
        print("小了！")
        num_1 = int(input("请输入第%d次猜的数字(1~100):"%i))
        i += 1
print("恭喜你猜中了。")

# 练习案例：求1-100的和
i=1;sum=0
while i<=100:
    sum+=i
    i+=1
print("1-100的累加的和为：",sum) #这样sum前会有一个空格
print(f"1-100的累加的和为：{sum}")
print("1-100的累加的和为：%d"%sum)

# while循环的基础案例 猜数字
import random
num=random.randint(1,100)
count=0
# 通过一个bool类型变量 做循环是否继续的标记
flag=True
while flag:
    count += 1
    num_suppose=int(input("请输入第%d次猜测的数字："%count))
    if num_suppose>num:
        print("大了！")
    elif num_suppose<num:
        print("小了！")
    else :
        flag=False
        print("恭喜你猜中了！")
print(f"你总共猜测了{count}次")

# while嵌套循环
#表白100天，每一天都会送10朵花
i=1
while i<=100:
    print("今天是第%d天表白"%i)
    j=1
    while j<=10:
        print("小美，这是送你的第%d朵花"%j)
        j+=1
    print("小美，我喜欢你\n")
    i+=1
print(f"坚持到第{i-1}天，表白成功")

# 输出print 语句不换行 (在print语句中，加入end='')
print("hello")
print("world")
print("hello",end=' ')
print("world",end='')

# 制表符  \t
print("hello\tworld")
print("myself\tbest")
print("\"我\"")

# while嵌套循环案例:九九乘法表
i=1
while i<=9:
    j = 1
    while j<=i:
        print("%d*%d=%d"%(j,i,i*j),end=' ')
        j+=1
    print()
    i+=1

i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%d\t"%(j,i,i*j),end='')
        j+=1
    i+=1
    print()

# for循环
# 语法：for 临时变量 in 待处理数据集（即序列类型）
name="helloworld"
for x in name:
    print(x)

# 练习案例：数一数有几个a
count=0
name="itheima is a brand of itcast"
for x in name:
    if x=='a':
        count+=1
print(f"itheima is a brand of itcast中共含有：{count}个字母a")

# for循环的range语句
# 语法1：range(num)  从0开始，到num结束的数字序列（不包含num本身）
for x in range(5):
    print(x,end=' ')
print()
# 语法2：range(num1,num2) 从num1开始，到num2结束的数字序列（不包含num2本身）
for x in range(5,10):
    print(x, end=' ')
print()
# 语法3：range(num1,num2,step) 从num1开始，到num2结束的数字序列（不包含num2本身） step:步长（默认为1）
for x in range(5,10,2):
    print(x, end=' ')
print()
# 给小美送玫瑰花
i=1
for x in range(10):
    print("这是送你的第%d朵玫瑰花"%i)
    i+=1

# 练习案例：有几个偶数
num=100;count=0
for x in range(1,100):
    if x%2==0:
        count+=1
print(f"1到100(不含100本身)范围内，有{count}个偶数。")

# for循环变量作用域
# 临时变量，在编程规范上，作用范围（作用域），只限定在for循环内部
x=0
for x in range(5):
    print(x)
print(x)

# for循环嵌套使用
# 表白小美送花
i=0
for i in range(100):
    print(f"今天是向小美表白的第{i+1}天")
    for j in range(10):
        print("这是送你的第%d朵玫瑰花。"%(j+1))
    print(f"小美，我喜欢你！(第{i+1}天的表白结束)")
print(f"坚持表白了{i+1}次，表白成功。")

# while for搭配使用
i=1
while i<=100:
    print(f"今天是向小美表白的第{i}天")
    for j in range(10):
        print("这是送你的第%d朵玫瑰花。"%(j+1))
    print(f"小美，我喜欢你！(第{i}天的表白结束)")
    i+=1
print(f"坚持表白了{i-1}次，表白成功。")

i=0
for i in range(100):
    print(f"今天是向小美表白的第{i+1}天")
    j=1
    while j<=10:
        print("这是送你的第%d朵玫瑰花。"%j)
        j+=1
    print(f"小美，我喜欢你！(第{i+1}天的表白结束)")
print(f"坚持表白了{i+1}次，表白成功。")

# 练习案例：for循环打印九九乘法表
for i in range(1,10):
    j = 1
    for y in range(1,10):
        if j<=i:
            print("%d*%d=%d\t"%(j,i,i*j),end='')
            j+=1
    print()

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d\t" % (j, i, i * j), end='')

# continue关键字控制循环
for i in range(1,6):
    print(i)
    continue
    print("语句2")
print()
# continue嵌套应用
for i in range(1,6):
    print(f"{i}语句1")
    for j in range(1,6):
        print(f"{i}语句2")
        continue
        print("语句3")
    print(f"{i}语句4")
print()
# break关键字控制循环
for x in range(1,6):
    print("语句1")
    break
    print("语句2")
print("语句3")
print()
# break嵌套应用
for i in range(1,6):
    print(f"{i}语句1")
    for j in range(1,6):
        print(f"{i}语句2")
        break
        print("语句3")
    print(f"{i}语句4")
    print()

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
