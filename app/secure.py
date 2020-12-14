#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 3:25 下午
# @Author  : BruceLee
# @Site    : 用户的机密信息，不能上传至git上
# @File    : secure.py

# # 调试模式
DEBUG = True
# 数据库连接，只需要写上连接地址即可【key值不可更改】
# 单数据库，分布式数据库
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root1234@127.0.0.1:3306/TestOne'

# 数据库连接信息
HOSTNAME = '127.0.0.1'  # 本机地址
PORT = '3306'  # MySQL默认端口
DATABASE = 'sys'  # 数据库名
USERNAME = 'root'  # 安装数据库时设置的用户名和密码
PASSWORD = 'root1234'

# 数据库连接字符串
# dialect+driver://username:password@host:port/database
DB_URI = 'mysql+cymysql://{username}:{password}@{host}:{port}/{database}'.format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, database=DATABASE
)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
