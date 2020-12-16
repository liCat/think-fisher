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


@web.route("/user/list")
def add_user_lists():
    """
    添加假用户列表
    :return:
    """
    strat_phone = int(request.args['startPhone'])
    end_phone = int(request.args['endPhone'])
    if strat_phone != 0 and strat_phone != '' and end_phone != 0 and end_phone != '':
        trace = User.get_much_user_infos(strat_phone, end_phone)
        return jsonify(trace)
    else:
        return {"msg": "add fake User list fail"}


@web.route("/user/openMember")
def open_user_member():
    """
    开通银符60 && 开通金符64
    :return:
    """
    user_id = int(request.args['userId'])
    package_id = int(request.args['packageId'])
    if user_id != 0 and user_id != '' and package_id != 0 and package_id != '':
        trace = User.mock_open_membership(user_id, package_id)
        return jsonify(trace)
    else:
        return {"msg": "mock pay member fail"}

