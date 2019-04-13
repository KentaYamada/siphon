import unittest
from datetime import datetime
from app.model.sales import Sales


class TestSales(unittest.TestCase):
    def setUp(self):
        self.sales = Sales(
            1,
            datetime.now(),
            datetime.now().time(),
            1000,
            0,
            0,
            0,
            0,
            1000,
            []
        )

    def test_id_validation(self):
        self.sales.id = '1'
        is_valid = self.sales.is_valid()
        has_error = 'id' in self.sales.validation_errors.keys()
        self.assertFalse(is_valid)
        self.assertTrue(has_error)

    def test_sales_date_validation(self):
        invalid_values = (None, 'hoge')
        for v in invalid_values:
            self.sales.sales_date = v
            is_valid = self.sales.is_valid()
            has_error = 'sales_date' in self.sales.validation_errors.keys()
            self.assertFalse(is_valid)
            self.assertTrue(has_error)

    def test_sales_time_validation(self):
        invalid_values = (None, 'hoge')
        for v in invalid_values:
            self.sales.sales_time = v
            is_valid = self.sales.is_valid()
            has_error = 'sales_time' in self.sales.validation_errors.keys()
            self.assertFalse(is_valid)
            self.assertTrue(has_error)

    def test_total_price_validation(self):
        invalid_values = (None, '1000', 0)
        for v in invalid_values:
            self.sales.total_price = v
            is_valid = self.sales.is_valid()
            has_error = 'total_price' in self.sales.validation_errors.keys()
            self.assertFalse(is_valid)
            self.assertTrue(has_error)

    def test_discount_price_validation(self):
        self.sales.discount_price = '0'
        is_valid = self.sales.is_valid()
        has_error = 'discount_price' in self.sales.validation_errors.keys()
        self.assertFalse(is_valid)
        self.assertTrue(has_error)

    def test_discount_rate_validation(self):
        invalid_values = ('0', 100)
        for v in invalid_values:
            self.sales.discount_rate = v
            is_valid = self.sales.is_valid()
            has_error = 'discount_rate' in self.sales.validation_errors.keys()
            self.assertFalse(is_valid)
            self.assertTrue(has_error)

    def test_deposit_validation(self):
        invalid_values = (None, '1000')
        for v in invalid_values:
            self.sales.deposit = v
            is_valid = self.sales.is_valid()
            has_error = 'deposit' in self.sales.validation_errors.keys()
            print(has_error)
            self.assertFalse(is_valid, 'error: {}'.format(v))
            self.assertTrue(has_error)

    def test_total_price_more_than_discount_price(self):
        self.sales.total_price = 1000
        self.sales.discount_price = 1100
        self.sales.deposit = 1000
        is_valid = self.sales.is_valid()
        has_error = 'discount_price' in self.sales.validation_errors.keys()
        self.assertFalse(is_valid)
        self.assertTrue(has_error)

    def test_deposit_less_than_total_price(self):
        self.sales.total_price = 1000
        self.sales.deposit = 900
        is_valid = self.sales.is_valid()
        has_error = 'deposit' in self.sales.validation_errors.keys()
        self.assertFalse(is_valid)
        self.assertTrue(has_error)
