# -*- coding:utf-8 -*-
__author__ = 'lulizhou'

import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd='121224',
    db='test',
    charset='utf8'
)
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
users = cursor.fetchall()
for user in users:
    print("Id=%d,name=%s,passwd=%s" % user)
try:
    sql_insert = "insert into user(username,passwd) value('kkz','1231')"
    sql_update = "update user set username='lulizhou' where id=9"
    sql_delete = 'delete from user where id=3'
    cursor.execute(sql_update)
    cursor.execute(sql_insert)
    cursor.execute(sql_delete)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()
# print(user)
cursor.close()
conn.close()