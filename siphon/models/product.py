# -*- coding: utf-8 -*-


class Product():
    def __init__(self, id, category_id, name='', price=0, *args, **kwargs):
        self.__id = id
        self.__category_id = category_id
        self.__name = name
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def category_id(self):
        return self.__category_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    def save(self):
        return True

    @classmethod
    def find_by_products(cls, category_id):
        products = []
        product_id = 1
        for i in range(1, 11):
            for j in range(1, 31):
                product = {
                    'id': product_id,
                    'category_id': i,
                    'name': 'Product{0}'.format(product_id),
                    'price': j * 100
                }
                products.append(product)
                product_id += 1
        if category_id < 1 and category_id > 10:
            return []
        return [row for row in products if row['category_id'] == category_id]
