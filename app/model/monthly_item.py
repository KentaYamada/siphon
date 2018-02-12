# -*- coding: utf-8 -*-


class MonthlyItem():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    @classmethod
    def find_by(sales_month):
        data = [
            {'item': 'Siphon Coffee', 'quantity': 200},
            {'item': 'Gamoyon Curry', 'quantity': 150},
        ]
        return data
