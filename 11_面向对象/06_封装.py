"""
演示面向对象封装思想中私有成员的使用
"""

# 定义一个类，内含私有成员变量和私有成员方法
# 私有成员变量：变量名以__开头(2个下划线)
# 私有成员方法：方法名以__开头(2个下划线)
class Phone:
    __current_voltage = 0.5        # 当前手机运行电压


    def __keep_single_core(self):
        print("让CPU以单核模式运行")


    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电。")

# 私有方法无法直接被类对象使用
# 私有变量无法赋值，也无法获取值
phone = Phone()
phone.call_by_5g()

