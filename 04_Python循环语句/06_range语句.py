"""
演示Python中的range()语句的基本使用
"""

# range语法1 range(num)
# 从0开始，到num结束的数字序列（不包含num本身）
# for x in range(10):
#     print(x)

# range 语法2 range(num1, num2)
# 从num1开始，到num2结束的数字序列（不包含num2本身）
# for x in range(5, 10):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔是1
#     print(x)

# range 语法3 range(num1, num2, step)
# 从num1开始，到num2结束的数字序列（不包含num2本身） step:步长（默认为1）
# for x in range(5, 10, 2):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是2
#     print(x)

for x in range(10):
    print("送玫瑰花")


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