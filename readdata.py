from pymysql import *

conn=Connect("127.0.0.1","root","","rider")

s="select * from students"

cr=conn.cursor()

cr.execute(s)

result=cr.fetchall()

for row in result:
    print(row[0],row[1])