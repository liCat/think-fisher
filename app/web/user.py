#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 3:25 下午
# @Author  : BruceLee
# @Site    : 
# @File    : user.py
from flask import request, jsonify, render_template

from app.spider.user_source import User
from ..spider.page import Pagination
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


@web.route("/user/freeMember")
def claim__user_free_card():
    """
    开通免费3天会员
    """
    user_id = int(request.args['userId'])
    if user_id != 0 and user_id != '':
        trace = User.claim_free_card(user_id)
        return jsonify(trace)
    else:
        return {"msg": "claim free thrree member fail"}


@web.route("/user/familyMember")
def bind_user_family_relation():
    """
    绑定亲友关系, 新用户需要登录才算做绑定亲友号成功
    :return:
    """
    invit_id = int(request.args['invitedId'])
    family_user_id = int(request.args['familyId'])
    if invit_id != 0 and invit_id != '' and family_user_id != 0 and family_user_id != '':
        trace = User.bind_family_relation(invit_id, family_user_id)
        return jsonify(trace)
    else:
        return {"msg": "bind user family relation"}


@web.route("/pager")
def pager():
    li = []
    for i in range(1, 100):
        li.append(i)
    pager_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=10)
    # print(request.args)
    index_list = li[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template("index.html", index_list=index_list, html=html)


