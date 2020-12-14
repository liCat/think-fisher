#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:38 上午
# @Author  : BruceLee
# @Site    : 
# @File    : book.py
import json

from flask import jsonify, request, render_template
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YUShuBook
from . import web

# app.add_url_rule('/hello', view_func=hello, endpoint=hello)
from ..forms.book import SearchForm
from ..spider.order_source import Order
from ..spider.search_source import Search
from ..spider.user_source import User
from ..view_models.book import BookViewModel, BookCollection


@web.route("/hello")
def hello():
    return render_template('index.html')


@web.route("/book/search")
def search():
    """
        q: 普通关键字 isbn
        page: 分页
        空行：python中有意义的空行可以很好的分割代码，帮助阅读和理解
    :return:
    """
    # q = request.args["q"]
    # page = request.args["page"]
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YUShuBook()

        if isbn_or_key == "isbn":
            yushu_book.search_by_isbn(q)
            # result = YUShuBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            yushu_book.search_by_keyword(q, page)
            # result = YUShuBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        return jsonify(form.errors)


@web.route("/order/placeOrder")
def place_ok_order():
    """
    通过下单的接口返回的trace，去查订单数据
    taobao & jingdong & pinduoduo order
    :return:
    """
    userId = request.args["user_id"]
    print(userId)
    productId = request.args["product_id"]
    print(productId)
    platform = request.args["platform"]
    print(platform)
    flag = request.args["flag"]
    if flag == "ok":
        trace = Order.order_ok(userId, productId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order ok fail"}


@web.route("/order/placePresaleOrder")
def place_presale_order():
    """
    taobao & jingdong & pinduoduo presale order
    :return:
    """
    userId = request.args["user_id"]
    productId = request.args["product_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "presale":
        trace = Order.order_presale(userId, productId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order presale fail"}


@web.route("/order/placeCancelOrder")
def place_cancel_order():
    """
    taobao & jingdong & pinduoduo cancel order
    :return:
    """
    userId = request.args["user_id"]
    productId = request.args["product_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "cancel":
        trace = Order.order_cancel(userId, productId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order cancel fail"}


@web.route("/order/placeRightOrder")
def place_right_order():
    """
    taobao & jingdong & pinduoduo right order
    :return:
    """
    userId = request.args["user_id"]
    productId = request.args["product_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "right":
        trace = Order.order_right(userId, productId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order right fail"}


@web.route("/order/palceTakeoutOrder")
def place_ok_takeOutOrder():
    """
    elme & meituan & KFC ok order
    :return:
    """
    userId = request.args["user_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "ok":
        trace = Order.order_takeout_ok(userId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order-takeout ok fail"}


@web.route("/order/palceTakeoutCancelOrder")
def place_cancel_takeOutOrder():
    """
    elme & meituan & KFC ok cancel order
    :return:
    """
    userId = request.args["user_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "cancel":
        trace = Order.order_takeout_cancel(userId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order-takeout cancel fail"}


@web.route("/order/palceTakeoutRigntOrder")
def place_right_takeOutOrder():
    """
    elme & meituan & KFC ok right order
    :return:
    """
    userId = request.args["user_id"]
    platform = request.args["platform"]
    flag = request.args["flag"]
    if flag == "right":
        trace = Order.order_takeout_right(userId, platform)
        return jsonify(trace)
    else:
        return {"msg": "order-takeout cancel fail"}


@web.route("/search/searchQuery")
def search_productId_query():
    """
    taobao & pinduoduo & jingdong search productId
    :return:
    """
    userId = request.args["user_id"]
    platform = request.args["platform"]
    trace = Search.search_productId(userId, platform)
    return jsonify(trace)
