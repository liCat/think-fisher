#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 10:30 下午
# @Author  : BruceLee
# @Site    : 用户系统相关的接口数据源
# @File    : user_source.py
import copy
import time

import requests

from ..libs import helper
from ..models.user_struct import UserStruct


class User:
    """用户系统"""

    @classmethod
    def add_fake_user(cls, phone):
        """
        添加假用户
        :param phone:
        :return:
        """
        url = "https://betacmsapi.shmiao.net/cms/test/fakeUser"
        params = '{"user_phone":"' + str(phone) + '"}'
        request_body = params
        cms_token = helper.get_value("token", "Authorization")
        headers = {
            'X-Request-Id': '33b84429a40411ea9f1356df5cd3f329',
            'Content-Type': 'text/html; charset=utf-8',
            'Authorization': "Bearer {0}".format(cms_token)
        }
        resp = requests.post(url, request_body, headers=headers, verify=False)
        return helper.str_to_json(resp.text)

    @classmethod
    def get_user_info(cls, phone):
        """
        用户查询
        :param phone:
        :return:
        """
        url = "https://betacmsapi.shmiao.net/cms/query/userinfo"
        request_body = {"user_id": phone}
        cms_token = helper.get_value("token", "Authorization")
        headers = {
            'x-request-id': '33b84429a40411ea9f1356df5cd3f329',
            'Content-Type': 'text/html; charset=utf-8',
            'Authorization': "Bearer {0}".format(cms_token)
        }
        resp = requests.get(url, request_body, headers=headers, verify=False)
        return helper.str_to_json(resp.text)

    @classmethod
    def get_much_user_infos(cls, strat_phone, end_phone):
        """
        批量获取用户信息
        :param strat_phone: 初始phoneNumber
        :param end_phone: 结束phoneNumber
        :return:
        """
        user_list = []
        for number in range(strat_phone, end_phone + 1):
            try:
                User.add_fake_user(number)
            except Exception as e:
                print('add fake user fail')
            get_single_user_info = User.get_user_info(number)
            user_fillter = User.__fill_user(get_single_user_info)
            user_list.append(user_fillter)
        return user_list

    @classmethod
    def __fill_user(cls, user_infos):
        """
        裁剪信息
        :param user_infos:
        :return:
        """
        user_res_copy = copy.deepcopy(UserStruct.userRes)
        user_res_copy['userID'] = user_infos['data']['id']
        user_res_copy['phoneNumer'] = user_infos['data']['phone']
        if len(user_infos['data']['taobao']) > 0:
            user_res_copy['taobao'] = user_infos['data']['taobao'][0]
        if user_infos['data']['expiredTime'] > int(time.time()):
            if user_infos['data']['isHasAnnualCardPermission']:
                user_res_copy['isMember'] = True
            else:
                user_res_copy['isMember'] = True
        else:
            user_res_copy['isMember'] = False
        return user_res_copy

    @classmethod
    def bind_family_relation(cls, invit_id, family_user_id):
        """
        绑定亲友关系
        :param invit_id:
        :param family_user_id:
        :return:
        """
        url = helper.fix_url("shmiao", "/pullnew.familygroup.Default/BindFamilyGroupRelation")
        request_body = {
            "inviterUserID": invit_id,
            "familyUserID": family_user_id
        }
        token = "Bearer 9527-{0}".format(family_user_id)
        headers = {
            "Authorization": token,
            'Content-Type': 'application/json; charset=utf-8'
        }
        resp = requests.post(url, helper.dict_to_str(request_body), headers=headers, verify=False)
        return resp

    @classmethod
    def claim_free_card(cls, user_id):
        """
        领取免费3天会员
        https://betaapi.shmiao.net/membership.Default/ClaimFreeCardV2
        :param userID: 必须是用户才能领取免费会员
        :return: freeCardExpiredTime 免费3天会员过期时间
        """
        url = helper.fix_url("shmiao", "/membership.Default/ClaimFreeCardV2")
        request_body = {}
        token = "Bearer 9527-{0}".format(user_id)
        headers = {
            "Authorization": token,
            'Content-Type': 'application/json; charset=utf-8'
        }
        resp = requests.post(url, helper.dict_to_str(request_body), headers=headers, verify=False)
        return resp

    @classmethod
    def mock_open_membership(cls, user_id, package_id, order_id=None):
        """
        mock 开通会员
        redis【69】
        查询命令：LRANGE MOCK_TEST_DATA 0 -1
        遇到问题可执行：del MOCK_TEST_DATA
        :param user_id: 用户ID
        :param package_id: 会员套餐
        :param order_id: 从此单开通会员时需要传订单号，可不传
        :return:
        """
        url = "http://betaapi.shmiao.net:10935/membership.internal.default/v1/mock-open-membership"
        if order_id:
            request_body = {
                "userID": user_id,
                "packageID": package_id,
                "orderID": order_id
            }
        else:
            request_body = {
                "userID": user_id,
                "packageID": package_id,
            }
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        resp = requests.post(url, helper.dict_to_str(request_body), headers=headers, verify=False)
        return helper.str_to_json(resp.text)