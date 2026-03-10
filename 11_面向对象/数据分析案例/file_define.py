"""
和文件相关的类定义
"""
import json

from data_define import Record


# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将它们都封装到list内返回即可"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件的路径

    # 复写（实现抽象方法）父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()     # 消除读取到的每一行数据中的\n
            data_list = line.split(",")
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path            # 定义成员变量记录文件的路径


    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


# 这段代码用于判断当前模块是否作为主程序运行。
# 当Python文件直接执行时，__name__变量等于'__main__'，条件为真，会执行后续的代码块；
# 当该文件被其他模块导入时，__name__变量等于模块名，条件为假，不会执行后续代码。这是Python中常见的入口点检查机制。
if __name__ == '__main__':
    text_file_reader = TextFileReader("D:/个人/learning/python/资料/第13章资料/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("D:/个人/learning/python/资料/第13章资料/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)