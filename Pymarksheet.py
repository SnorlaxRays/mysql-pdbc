import pymysql
result = ""
connection = pymysql.connect(host="localhost" ,user ='root', password='root',db='Marksheet')
with connection.cursor() as cursor:
    sql = 'select * from marks'
    cursor.execute(sql)
    result = cursor.fetchall()

connection.close()
for d in result:
    print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4],"\t",d[5])
'''


import pymysql
connection = pymysql.connect(host="localhost" ,user ='root', password='root',db='Marksheet')
with connection.cursor() as cursor:
    sql = 'insert into marks values(7,"free", 117, 74, 93, 57)'
    cursor.execute(sql)
    connection.commit()
    print("data inserted!!")

connection.close()
'''