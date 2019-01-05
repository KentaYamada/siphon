import unittest
from datetime import datetime
from app.model.sales import Sales


class TestSales(unittest.TestCase):
    def test_id_validation(self):
        sales = Sales('1', datetime.now(), 1000, 0, 0, 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('id' in sales.validation_errors.keys())

    def test_sales_date_validation(self):
        sales = Sales(1, None, 1000, 0, 0, 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('sales_date' in sales.validation_errors.keys())

        sales.sales_date = 'hoge'
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('sales_date' in sales.validation_errors.keys())

    def test_total_price_validation(self):
        sales = Sales(1, datetime.now(), None, 0, 0, 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('total_price' in sales.validation_errors.keys())

        sales.total_price = '1000'
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('total_price' in sales.validation_errors.keys())

        sales.total_price = 0
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('total_price' in sales.validation_errors.keys())

    def test_discount_price_validation(self):
        sales = Sales(1, datetime.now(), 1000, '0', 0, 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('discount_price' in sales.validation_errors.keys())

    def test_discount_rate_validation(self):
        sales = Sales(1, datetime.now(), 1000, 0, '0', 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('discount_rate' in sales.validation_errors.keys())

        sales.discount_rate = 100
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('discount_rate' in sales.validation_errors.keys())

    def test_deposit_validation(self):
        sales = Sales(1, datetime.now(), 1000, 0, 0, 0, 0, None, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('deposit' in sales.validation_errors.keys())

        sales.deposit = '1000'
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('deposit' in sales.validation_errors.keys())

    def test_total_price_more_than_discount_price(self):
        sales = Sales(1, datetime.now(), 1000, 1100, 0, 0, 0, 1000, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('discount_price' in sales.validation_errors.keys())

    def test_deposit_less_than_total_price(self):
        sales = Sales(1, datetime.now(), 1000, 0, 0, 0, 0, 900, [])
        result = sales.is_valid()
        self.assertFalse(result)
        self.assertTrue('deposit' in sales.validation_errors.keys())
