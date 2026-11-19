import pymysql
username=input()
password=input()

con=pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port=3306,
    database="jing_dong"
)
cur=con.cursor()
sql= f"select * from user where user='{username}'and pwd='{password}'"
result=cur.execute(sql)
if result:
    print("登录成功")
else:
    print("登录失败")

cur.close()
con.close()