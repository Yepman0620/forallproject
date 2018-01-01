#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:52:51 2017

@author: allen
"""
# 导入MySQLdb模块
import MySQLdb

# 建立与数据库的连接
conn3 = MySQLdb.connect('localhost', 'root', 'admin', 'test123')

# 创建游标
cur3 = conn3.cursor()

# 创建表
cur3.execute('select * from table_a where user_id=988917 and month_id=201503')

# 接收一条查询结果
result1 = cur3.fetchone()
print result1

# 接收全部查询结果
result2 = cur3.fetchall()
print result2

# 返回这次execute操作影响的记录数
print cur3.rowcount

# 循环遍历结果集记录
for row in result2:
    user_id = row[0]
    month_id = row[1]
    brand_id = row[2]
    rate = row[3]
    print 'user_id=%d,month_id=%d,brand_id=%s,rate=%f' % \
          (user_id, month_id, brand_id, rate)

# 关闭游标
cur3.close()

# 断开数据库连接
conn3.close()