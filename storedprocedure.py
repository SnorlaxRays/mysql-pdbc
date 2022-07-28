import pymysql

connection = pymysql.connect(host="localhost", user="root", password="root",db="marksheet")
with connection.cursor() as cursor:
    cursor.callproc("new_procedure")
    for result in cursor.fetchall():
        print(result)
    
connection.close()