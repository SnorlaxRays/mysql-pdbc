import pymysql
import MarksheetBean
from MarksheetBean import *


class MarksheetDao:
    
    connection = pymysql.connect(host="localhost", user="root", password="root",db="marksheet")
    result =""
    
    def nextPk(self,mb):
        pk = 0
        with MarksheetDao.connection.cursor() as cursor:
            sql = 'select max(rollnum) from marks'
            cursor.execute(sql)
            MarksheetDao.result = cursor.fetchall()
            MarksheetDao.connection.close()
                
        for d in MarksheetDao.result:
            pk = d[0]
        return pk + 1
                

    def add(self,mb):
        pk = MarksheetDao.nextPk(mb)
        with MarksheetDao.connection.cursor() as cursor:
            
            sql = 'insert into marks values(%s,%s,%s,%s,%s,%s)'
            data = mb.getId(),mb.getName(),pk,mb.getPhysics(),mb.getChemistry(),mb.getMaths()
            cursor.execute(sql, args = data)
            MarksheetDao.connection.commit()
            MarksheetDao.connection.close()
            
    def update(self,mb):
        with MarksheetDao.connection.cursor() as cursor:
            
            sql = 'update marks set phy=%s where id = %s'
            data = mb.getPhysics()
            cursor.execute(sql, args =data)
            MarksheetDao.connection.commit()
            MarksheetDao.connection.close()
            
    def delete(self,mb):
        with MarksheetDao.connection.cursor() as cursor:
            sql = 'delete from marks where id=%s'
            data = mb.getId()
            cursor.execute(sql,data)
            MarksheetDao.connection.commit()
            MarksheetDao.connection.close()
            
    def search(self,mb):
        with MarksheetDao.connection.cursor() as cursor:
            sql = 'select * from marks'
            cursor.execute(sql)
            MarksheetDao.result = cursor.fetchall()
            MarksheetDao.connection.close()
        
        for d in MarksheetDao.result:
            print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4],"\t",d[5])
        
    def getRollNum(self,mb):
        with MarksheetDao.connection.cursor() as cursor:
            sql = 'select * from marks where rollnum = %s'
            data = mb.getRollNumber()
            cursor.execute(sql,data)
            MarksheetDao.result = cursor.fetchall()
            MarksheetDao.connection.close()
        
        for d in MarksheetDao.result:
            print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4],"\t",d[5])
       
    def getMeritList(self,mb):
        with MarksheetDao.connection.cursor() as cursor:
            sql = 'select id,name,rollnum,phy,chem,maths,(phy+chem+maths) as total from marks where phy >33 and chem >33 and maths>33 order by total desc limit 5'
            cursor.execute(sql)
            MarksheetDao.result = cursor.fetchall()
            MarksheetDao.connection.close()
           
        for d in MarksheetDao.result:
            print(d[0]," ",d[1],"\t",d[2],"\t",d[3],"\t",d[4],"\t",d[5],"\t",d[6])
        
                
    
        
            
        
