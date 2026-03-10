"""
演示Python pymysql库的基础操作
"""
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost",   # 主机名（IP）ip可以用127.0.0.1
    port=3306,          # 端口 MySQL数据库端口默认是3306
    user="root",        # 账户
    password="tt123456",  # 密码
    autocommit=True     # 设置自动提交
)

# print(conn.get_server_info())   # 获取数据库版本信息

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql
# cursor.execute("create table test_pymysql(id int)")
# 插入数据
cursor.execute("insert into test_pymysql values(20240005)")
# 执行查询
cursor.execute("select * from test_pymysql")
# 获取查询结果
results:tuple=cursor.fetchall()
for r in results:
    print(r)
# 关闭链接
conn.close()

