"""
演示面向对象的多态特性以及抽象类（接口）的使用
"""
# 多态常作用在继承关系上
# 以父类做定义声明，以子类做实际工作，用以获得同一行为，不同状态

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    """制造点噪音，需要传入Animal对象"""
    animal.speak()


# 演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 抽象设计的意义：父类用来确定有哪些方法，具体的方法实现，由子类自行决定，这种写法就叫做抽象类（接口）
# 抽象类：含有抽象方法的类叫抽象类；
# 抽象方法：方法体是空实现的（pass）称之为抽象方法
# 演示抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()


make_cool(midea_ac)
make_cool(gree_ac)
