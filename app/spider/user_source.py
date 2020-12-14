#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 10:30 下午
# @Author  : BruceLee
# @Site    : 用户系统相关的接口数据源
# @File    : user_source.py
import requests

from ..libs import helper


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
        return resp

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
            add_single_user = User.add_fake_user(number)
            get_single_user_info = User.get_user_info(number)
            res_singel_user = helper.str_to_json(add_single_user.text)
            res_single_uesr_info = helper.str_to_json(get_single_user_info.text)
            if res_singel_user['code'] == 0:
                user_list.append(res_single_uesr_info['data']['id'])
                user_list.append(res_single_uesr_info['data']['phone'])
            if len(res_single_uesr_info['data']['taobao']) > 0:
                user_list.append(res_single_uesr_info['data']['taobao'][0])
        return user_list

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
        return resp
