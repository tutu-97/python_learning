"""
演示使用pymysql库进行数据插入的操作
"""
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）
    port=3306,          # 端口
    user="root",        # 账户
    password="tt123456",  # 密码
    autocommit=True     # 自动提交（确认）
)

# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
# cursor.execute("create table student(id int,name char(8),age char(2),sex char(2))")
# 执行sql
cursor.execute("insert into student values(100007, '张三', 28, '男')")
# 通过commit确认 使用自动提交代替
# conn.commit()
# 关闭链接
conn.close()
