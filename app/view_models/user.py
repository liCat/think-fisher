#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/13 11:40 上午
# @Author  : BruceLee
# @Site    : 用户系统
# @File    : user.py


class UserViewModel:
    """ 单个非会员用户数据"""
    """
    {code: 0, msg: "成功", data: {code: 0, msg: "添加成功", data: "10013803900"}}
    {code: 1, msg: "添加假用户失败", data: {error_msg: "添加假用户失败"}}
    """

    def __init__(self, user_info, oi=1):
        self.id = ++oi
        self.user_id = user_info['id']
        self.phone = user_info['phone']
        self.taobao = user_info['taobao']


class MemberViewModel:
    """
    会员用户信息
    """

    def __init__(self, member_info):
        self.ismember = member_info['isHasAnnualCardPermission']
