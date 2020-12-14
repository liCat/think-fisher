#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 3:25 下午
# @Author  : BruceLee
# @Site    : 
# @File    : user.py
from flask import request, jsonify

from app.spider.user_source import User
from ..web import web


@web.route("/user/add")
def add_user_fake():
    """
    添加假用户
    :return:
    """
    user_phone = request.args['phone']
    if user_phone != 0 and user_phone != '':
        trace = User.add_fake_user(user_phone)
        return jsonify(trace)
    else:
        return {"msg": "add fake User fail"}