import unittest
from app.model.sales_item import SalesItem


class TestSalesItemTest(unittest.TestCase):
    def test_id_validation(self):
        sales_item = SalesItem('1', 1, 1, 'test', 100, 1, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('id' in sales_item.validation_errors.keys())

    def test_sales_id_validation(self):
        sales_item = SalesItem(1, None, 1, 'test', 100, 1, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('sales_id' in sales_item.validation_errors.keys())

        sales_item.sales_id = '1'
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('sales_id' in sales_item.validation_errors.keys())

        sales_item.sales_id = 0
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('sales_id' in sales_item.validation_errors.keys())

    def test_item_no_validation(self):
        sales_item = SalesItem(1, 1, None, 'test', 100, 1, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('item_no' in sales_item.validation_errors.keys())

        sales_item.item_no = '1'
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('item_no' in sales_item.validation_errors.keys())

        sales_item.item_no = 0
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('item_no' in sales_item.validation_errors.keys())

    def test_item_name_validation(self):
        sales_item = SalesItem(1, 1, 1, '', 100, 1, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('item_name' in sales_item.validation_errors.keys())

        sales_item.item_name = None
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('item_name' in sales_item.validation_errors.keys())

    def test_unit_price_validation(self):
        sales_item = SalesItem(1, 1, 1, 'test', None, 1, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('unit_price' in sales_item.validation_errors.keys())

        sales_item.unit_price = '1'
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('unit_price' in sales_item.validation_errors.keys())

        sales_item.unit_price = 0
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('unit_price' in sales_item.validation_errors.keys())

    def test_quantity_validation(self):
        sales_item = SalesItem(1, 1, 1, 'test', 1, None, 100)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('quantity' in sales_item.validation_errors.keys())

        sales_item.quantity = '1'
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('quantity' in sales_item.validation_errors.keys())

        sales_item.quantity = 0
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('quantity' in sales_item.validation_errors.keys())

    def test_subtotal_validation(self):
        sales_item = SalesItem(1, 1, 1, 'test', 1, 1, None)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('subtotal' in sales_item.validation_errors.keys())

        sales_item.subtotal = '1'
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('subtotal' in sales_item.validation_errors.keys())

        sales_item.subtotal = 0
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('subtotal' in sales_item.validation_errors.keys())

    def test_subtotal_unmatch(self):
        sales_item = SalesItem(1, 1, 1, 'test', 100, 1, 200)
        result = sales_item.is_valid()
        self.assertFalse(result)
        self.assertTrue('subtotal' in sales_item.validation_errors.keys())
