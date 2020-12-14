#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 11:07 下午
# @Author  : BruceLee
# @Site    : 自己封装的小模块
# @File    : helper.py
import json
import requests, os
import yaml

from app.conf import _getPath

conf_dir_path = os.path.dirname(_getPath.get_file_path())


def is_isbn_or_key(word):
    """
    判断是isbn还是关键字请求
    :param word: 关键字
    :return:
    """
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit:
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = word
    return isbn_or_key


def get_token(user_id):
    """
    get token by userid
    :return:
    """
    return "Bearer 9527-{0}".format(user_id)


def get_headers(user_id):
    """
    get headers by userid
    :return:
    """
    headers = {
        "Authorization": get_token(user_id),
        "Content-Type": 'application/json; charset=utf-8'
    }
    return headers


def cms_login(self):
    """cms后台登录"""
    url = "https://betacmsapi.shmiao.net/user.Login/LoginV3"
    request_body = '{"userName": "qtt_test", "password": "123456", "app":"APP_SHIHUIMIAO_CMS"}'
    headers = {
        'x-request-id': 'e1753142a40111eab64e56df5cd3f329',
        'Content-Type': 'application/json; charset=utf-8',
    }
    resp = requests.post(url, request_body, headers=headers, verify=False)
    return resp


def update_yaml(file_name, property_value, value):
    f = open('%s/conf/%s.yml' % (conf_dir_path, file_name), 'r+', encoding='utf-8')
    conf = yaml.load(f)
    f.close()
    conf[property_value] = value
    f1 = open('%s/conf/%s.yml' % (conf_dir_path, file_name), 'w', encoding='utf-8')
    yaml.safe_dump(conf, f1)
    f1.close()


def str_to_json(str_value):
    """
    字符串转json串
    :param str_value:
    :return:
    """
    return json.loads(str_value)


def dict_to_str(dict_value):
    """
    dict 类型转成 str
    :param dict_value:
    :return:
    """
    return json.dumps(dict_value)


def fix_url(url1, url2):
    """
    拼接url1 & url2
    :param url1:
    :param url2:
    :return:
    """
    base_url = get_value("conf", url1)
    return str(base_url) + url2


def get_value(filename, key):
    f = open('%s/conf/%s.yml' % (conf_dir_path, filename), 'r', encoding='utf-8')
    x = yaml.load(f)
    f.close()
    return x[key]
