#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:38 上午
# @Author  : BruceLee
# @Site    : APP的初始化工作
# @File    : __init__.py.py
from flask import Flask
from app.models.book import db


def create_app():
    # 实例化flask对象
    app = Flask(__name__) # template_folder指定特定的模板路径，这里是相对于app应用程序级别相对路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 把数据库对象插到核心对象板上
    db.init_app(app)
    # 第一种写法：把数据模型映射到数据库中
    # db.create_all(app=app)

    # 第二种写法，把app_context推入栈中即可
    with app.app_context():
        db.create_all()
    return app

    # 第三种写法，在实例化对象的时候，就传一个值至

def register_blueprint(app):
    """
    把蓝图注册到Flask的APP核心对象上
    :param app:
    :return:
    """
    from app.web.book import web
    app.register_blueprint(web)