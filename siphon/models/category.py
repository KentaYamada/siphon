# -*- coding: utf-8 -*-


class Category():
    def __init__(self, id=None, name='', *args, **kwargs):
        self.__id = id
        self.__name = name
        self.__products = None

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def save(self):
        return True

    @classmethod
    def find_all_categories(cls):
        return [{'id': i, 'name': 'Category{0}'.format(i)} for i in range(1, 11)]
