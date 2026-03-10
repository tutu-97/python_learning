"""
演示面向对象：继承的基础语法
"""


class Phone:
    IMEI = None     # 序列号
    producer = "ITCAST" # 厂商


    def call_by_4g(self):
        print("4g通话")

# 演示单继承
# 语法：class 类名(父类名):
class Phone2022(Phone):
    face_id = "10001"       # 面部识别ID


    def call_by_5g(self):
        print("2022年新功能：5g通话")


phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()



class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

# 演示多继承
# 语法：class 类名(父类1, 父类2, 父类3, ...):
class MyPhone(Phone, NFCReader, RemoteControl):
    pass
# pass是占位语句，用来保证函数（方法）或类定义的完整性，表示无内容，空的意思


phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()

print(phone.producer)


# 演示多继承下，父类成员名一致的场景
# 左边优先（父类1 > 父类2 > 父类3 > ...）,先继承的优先级高于后继承
