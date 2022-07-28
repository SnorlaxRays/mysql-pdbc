import pymysql

class User:
    


    def authenticate(self, login,password):
        result = ""
        connection = pymysql.connect(host="localhost", user="root", password="root",db="django_user")
        
        with connection.cursor() as cursor:
            sql = 'select * from sos_user where emailAddress = %s && password =%s'
            data = (login, password)
            cursor.execute(sql, data)
            result = cursor.fetchall()
            if(not result):
                print("Invalid user!!")
            else:
                print("Verified!!!")
                connection.close()
                for d in result:
                    print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4])
                    
def testAuthenticate():
    login = "sand@gmail.com"
    password = "pass123"
    
    md = User()
    md.authenticate(login,password)
    
testAuthenticate()
    