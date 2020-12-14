#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/12 10:19 下午
# @Author  : BruceLee
# @Site    : 
# @File    : _getPath.py

import inspect, os, sys


# 获取脚本文件的当前路径
# 1. 获取调用该函数的脚本所在路径，跨模块跨文件可调用的函数：
def get_script_path():
    caller_file = inspect.stack()[1][1]  # caller's filename
    return os.path.abspath(os.path.dirname(caller_file))  # path


# 2. 获取该文件的所在的路径
def get_file_path():
    this_file = inspect.getfile(inspect.currentframe())
    return os.path.abspath(os.path.dirname(this_file))


# 3. 获取解释器所执行的脚本路径
def script_path():
    path = os.path.realpath(sys.path[0])
    if os.path.isfile(path):
        path = os.path.dirname(path)
    return os.path.abspath(path)
