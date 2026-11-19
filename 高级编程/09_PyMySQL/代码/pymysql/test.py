#导入包
import pymysql
#创建连接（基本四项主机名称，用户密码和端口号），外加指定的数据库
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
    database="jing_dong"
)
#创建游标
cur=conn.cursor()
#注入sql
sql ="select * from goods"
#启动等于python那个三角形的小绿标execute,执行代码
result=cur.execute(sql)
print(f"查询到了多少行{result}")
data1=cur.fetchone()
data2=cur.fetchall()
#抓取数据一个
print(data1)
for i in data2:
    print(i)
#关闭游标
cur.close()
#关闭连接
conn.close()