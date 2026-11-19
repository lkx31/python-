
import pymysql
conn=pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    port=3306,
    database="jing_dong"
)
cur=conn.cursor()
sql='update user set user="rose"where id=15'
result=cur.execute(sql)
print(f"影响函数{result}")
conn.commit()
cur.close()
conn.close()
