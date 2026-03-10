from my_module3 import *

# 模块3中__all__=['test_A']，所以导入所有(*)时只能导入test_A，也只能使用A不能调用B
test_A()
# test_B()



from my_package import *
# 包中的module1模块的info_print1()方法
# module1.info_print1()
# module1不可调用，因为__all__ = ['module2']，包中__init__.py文件中module1没有添加__all__变量

# 包中的module2模块的info_print2()方法
module2.info_print2()