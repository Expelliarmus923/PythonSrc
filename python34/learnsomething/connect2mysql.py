# -*- coding:utf-8 -*-
__author__ = 'lulizhou'

import mysql.connector

conn = mysql.connector.connect(user='root', password='121224', database='news')

cursor = conn.cursor()
cursor.execute('select * from t_news where id = %s', ['2'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()