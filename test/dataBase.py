#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 6:50 下午
# @Author  : BruceLee
# @Site    : 
# @File    : dataBase.py

from sqlalchemy import create_engine

# 数据库连接信息
HOSTNAME = '127.0.0.1'  # 本机地址
PORT = '3306'  # MySQL默认端口
DATABASE = 'TestOne'  # 数据库名
USERNAME = 'root'  # 安装数据库时设置的用户名和密码
PASSWORD = 'root1234'

# 数据库连接字符串
# dialect+driver://username:password@host:port/database
DB_URI = 'mysql+cymysql://{username}:{password}@{host}:{port}/{database}'.format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE
)

# 创建一个engine对象
engine = create_engine(DB_URI)
# 连接数据库
conn = engine.connect()
# 执行SQL语句，并返回执行结果
sel_res = conn.execute('SELECT * FROM TestOne.users;')
# 获取并打印一条查询结果
print(sel_res.fetchone())
# 关闭连接
conn.close()