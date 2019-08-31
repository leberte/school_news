#!/user/bin/python3
# _*_ coding: utf-8 _*_
import mysql.connector
from sendmail import mailcuowu

class MysqlHelper:
    def __init__(self,host='localhost',port='3306',db='school_info',user='root',passwd='*******',charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        try:
            self.conn=mysql.connector.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
            self.cursor=self.conn.cursor()
        except Exception as e:
            mailcuowu('数据库连接错误...')
    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self,sql,params=()):
        result=None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            pass
        return result

    def get_all(self,sql,params=()):
        list1 = []
        list2 = []
        try:
            self.connect()
            self.cursor.execute(sql,params)
            list1  =self.cursor.fetchall()
            self.close()
        except Exception as e:
            mailcuowu('数据库查询错误...')
            pass
        for i in list1:
            list2.append(list(i)[0])
        return list2

    def insert(self,sql,params=()):
        return self.__edit(sql,params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self,sql,params):
        try:
            count=0
            self.connect()
            count=self.cursor.execute(sql,params)
            self.conn.commit()
            self.close()
        except Exception as e:
            mailcuowu('数据库写入错误...')
        return count
