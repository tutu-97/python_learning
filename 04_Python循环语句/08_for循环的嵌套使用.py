"""
演示嵌套应用for循环
"""

# 坚持表白100天，每天都送10朵花
# range
i = 0
for i in range(1, 101):
    print(f"今天是向小美表白的第{i}天，加油坚持。")

    # 写内层的循环了
    for j in range(1, 11):
        print(f"给小美送的第{j}朵玫瑰花")

    print("小美我喜欢你")

print(f"第{i}天，表白成功")


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


