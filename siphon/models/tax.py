# -*- coding: utf-8 -*-


class Tax():
    def __init__(self, rate=1, tax_type='out', *args, **kwargs):
        self.__rate = rate
        self.__tax_type = tax_type

    @property
    def rate(self):
        return self.__rate

    @property
    def tax_type(self):
        return self.__tax_type

    def save(self):
        return True

    @classmethod
    def find_tax(cls):
        return Tax(rate=8)
