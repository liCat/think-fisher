#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 9:18 下午
# @Author  : BruceLee
# @Site    : 
# @File    : 对象序列化.py

"""
构建API时，需要输出的是Json格式response，所以需要用到json序列化操作
思路：
    1， 构建一个可以序列化的函数
    2，jsonify时序列化参数的内部数据，例如：books:[]中列表如何序列化
"""