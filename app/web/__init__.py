#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:38 上午
# @Author  : BruceLee
# @Site    : 管理整个web类页面的视图函数，整理数据输出给前端
# @File    : __init__.py.py
"""
1， 标记temlates的文件属性-设置-project structrue 标记为temlates
"""
from flask import Blueprint

web = Blueprint("web", __name__) # template_folder指定特定的模板路径-相对路径,这里相当于蓝图

# 导入视图函数，若放在注册蓝图之前则会报错，这样的结构会出现循环导入
from app.web import book
from app.web import user
