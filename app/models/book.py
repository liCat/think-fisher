#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 3:58 下午
# @Author  : BruceLee
# @Site    : 数据结构模型定义
# @File    : book.py

from sqlalchemy import Column, INTEGER, String
from flask_sqlalchemy import SQLAlchemy


# 实例化数据库对象，也需要插到核心对象上才能使用【app下的__init__文件中】
db = SQLAlchemy()


# 必须要继承db.Model,否则写不进数据库，切记切记额！！！
class Book(db.Model):
    """
        一些属性定义重复性比较大，元类可以解决这个问题
    """
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    _author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(INTEGER)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))
