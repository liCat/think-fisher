#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 10:59 下午
# @Author  : BruceLee
# @Site    : 为满足客户端对不同页面需求数据的处理，需要设计对源数据进行裁剪和加工
# @File    : book.py


class BookViewModel:
    """
    单本数据
    """

    def __init__(self, book):
        self.title = book['title']
        self.author = '、'.join(book['author'])
        self.binding = book['binding']
        self.publisher = book['publisher']
        self.image = book['image']
        self.price = '￥' + book['price'] if book['price'] else book['price']
        self.pubdate = book['pubdate']
        self.summary = book['summary']
        self.pages = book['pages']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = None

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword


class _BookViewModel:
    """
    面向对象正确表达：
    1，描述特征【类变量、实例变量】
    2，行为（方法）
    """

    @classmethod
    def package_single(cls, data, keyword):
        """

        :param data:
        :param keyword:
        :return:
        """
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned["total"] = 1
            returned["books"] = [cls.__cut_book_data(data)]
        return returned

    @classmethod
    def package_collection(cls, data, keyword):
        """

        :param data:
        :param keyword:
        :return:
        """
        returned = {
            "books": [],
            "total": 0,
            "keyword": keyword
        }
        if data:
            returned["total"] = data["total"]
            returned["books"] = [cls.__cut_book_data(book) for book in data["books"]]
        return returned

    @classmethod
    def __cut_book_data(cls, data):
        """

        :param data:
        :return:
        """
        book = {
            "title": data['title'],
            "author": '、'.join(data['author']),
            "binding": data['binding'] or "",  # or是最简单的使用方法，超过三元运算符
            "publisher": data['publisher'],
            "image": data['image'],
            "price": '￥' + data['price'] if data['price'] else data['price'],
            "pubdate": data['pubdate'],
            "summary": data['summary'] or "",
            "pages": data['pages'] or ""
        }
        return book
