import pymysql

connection = pymysql.connect(host="localhost", user="root", password="root",db="marksheet")
connection.autocommit =False
try:
    with connection.cursor() as cursor:
        sql = 'insert into marks values(%s,%s,%s,%s,%s,%s)' 
        cursor.execute(sql,(7,'person',117,84,38,95))
        cursor.execute(sql,(8,'person1',118,34,39,45))
        connection.commit()
    
   

except Exception as e:
    connection.rollback()
    print("oops something went worng!!")
finally:
    connection.close()