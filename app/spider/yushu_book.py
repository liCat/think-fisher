#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 8:02 上午
# @Author  : BruceLee
# @Site    : 数据源层
# @File    : yushu_book.py
from app.libs.httper import HTTP
from flask import current_app


class YUShuBook:
    """
    M-模型层
    """
    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        """
        数据只需要裁剪，不需要返回
        :param isbn:
        :return:
        """
        # self可以取到类变量，self在方法中查找不到变量，会继续在类中查找
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def search_by_keyword(self, keyword, page=1):
        """
        数据只需要裁剪，不需要返回
        :param keyword:
        :param page:
        :return:
        """
        url = self.keyword_url.format(keyword, current_app.config["PER_PAGE"], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def calculate_start(self, page):
        return (page - 1) * current_app.config["PER_PAGE"]

    def __fill_single(self, data):
        """
        双下划线开头，私有方法
        :param data:
        :return:
        """
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        """
        双下划线开头，私有方法
        :param data:
        :return:
        """
        # self.total = data['total']
        self.books = data['books']
