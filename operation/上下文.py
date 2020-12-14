#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/11 8:24 下午
# @Author  : BruceLee
# @Site    : 
# @File    : 上下文.py

"""

"""
"""
flask的上下文：
1，应用上下文，本质是对象，主要是对核心对象Flask的封装， AppContext-核心对象的封装（路由，视图..）
2，请求上下文，本质是对象，主要是对Request【大写】，RequestContext-保存了请求信息（url，header..）
一般是通过上下文操作核心对象，具体就是LocalProxy提供了方法间接操作上下文

单元测试,离线应用的原理：不需要使用浏览器，直接自己可以推入栈中
获取请求上下文对象
ctx = app.app_context() 
推入栈中
ctx.push()
a才能指向请求上下文对象
a = current_app
d才能获取到DEBUG参数
d = current_app.config['DEBUG']
ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']
    
with应用：
    实现了上下文协议的对象使用with
    上下文管理器 AppContext
    只需要实现了__enter__ __exit__ 都可以使用上下文管理器
    上下文表达式必须要返回一个上下文管理器

with使用场景：
    链接数据库 ---> 执行sql ---> 释放资源
    文件读写 ---> 执行读写 ----> 关闭文件
    
如果是在请求中使用上下文对象，那么Flask会自动实现Push
"""