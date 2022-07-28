import pymysql
result = ""
connection = pymysql.connect(host="localhost", user="root", password="root",db="marksheet")

def insert():
    with connection.cursor() as cursor:
        sql = "insert into marks values(7, 'hello', 117, 73, 83, 67)"
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("data inserted!!")

def show():
    with connection.cursor() as cursor:
        sql = 'select * from marks'
        cursor.execute(sql)
        result = cursor.fetchall()
        connection.close()
    for d in result:
        print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4],"\t",d[5])
        
def delete():
    with connection.cursor() as cursor:
        sql = 'delete from marks where id=7'
        cursor.execute(sql)
        connection.commit()
        connection.close()
        
#insert()
#show()
#delete()
show()