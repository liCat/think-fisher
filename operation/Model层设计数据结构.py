#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 4:07 下午
# @Author  : BruceLee
# @Site    : 对应项目的models层
# @File    : Model层设计数据结构.py

"""
Model层设计数据结构
"""
"""
1，了解第三方库sqlalchemy,Flask做了封装flask-SQLAlchemy
2，了解第三方库WTFORMS,Flask做了封装flask-WTFORMS，验证层
3，了解第三方库werkzeug，Flask做了封装实现了路由系统
4，学习看第三方库的API文档，或者继承第三方库从而实现自己定制的功能
5, flask连接数据库的操作：
    a.导入from flask_sqlalchemy import SQLAlchemy
    b.实例化数据库对象，也需要插到核心对象上才能使用【app下的__init__文件中】db = SQLAlchemy()
    c.把数据库对象插到核心对象板上, db.init_app(app)
    d.数据库连接，只需要写上连接地址即可【key值不可更改】,SQLALCHEMY_DATABASE_URI='mysql+pymysql://<dbUsername>:<dbPassword>@<host>/<dbname>[?<options>]'
    e.数据库驱动：pymysql需要下载
    f.把数据模型映射到数据库中,生产数据表。db.create_all(app=app)
参考数据库API文档：https://docs.sqlalchemy.org/en/13/dialects/mysql.html

6，Model层一般是写业务逻辑的，只有数据 == 数据表
7，ORM 对象关系映射 Code First, 增删改查，通过操作ORM来操作数据库

阅读源码，学习思路，入门最主要的是不仅会使用API而且还能阅读源码
"""
