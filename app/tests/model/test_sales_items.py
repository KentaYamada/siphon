import unittest
from app.model.sales_item import SalesItem


class TestSalesItemTest(unittest.TestCase):
    def test_save_ok(self):
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        self.assertTrue(saved)

    def test_save_ng_when_invalid_value(self):
        # sales_id
        model = SalesItem(
                None, sales_id=None, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('sales_id', errors[0]['name'])

        # sales_date
        model = SalesItem(
                None, sales_id=1, sales_date=None,
                item_no=1, item_name='Test', unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('sales_date', errors[0]['name'])

        # item_no
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=None, item_name='Test', unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('item_no', errors[0]['name'])

        # item_name
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='', unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('item_name', errors[0]['name'])

        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name=None, unit_price=500,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('item_name', errors[0]['name'])

        # unit_price
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=None,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('unit_price', errors[0]['name'])

        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=0,
                quantity=1, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('unit_price', errors[0]['name'])

        # quantity
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=None, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('quantity', errors[0]['name'])

        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=0, subtotal=500)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('quantity', errors[0]['name'])

        # subtotal
        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=1, subtotal=None)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('subtotal', errors[0]['name'])

        model = SalesItem(
                None, sales_id=1, sales_date='2018/01/01 10:00:00',
                item_no=1, item_name='Test', unit_price=500,
                quantity=1, subtotal=0)
        saved = model.save()
        errors = model.errors
        self.assertFalse(saved)
        self.assertEqual('subtotal', errors[0]['name'])

    def test_delete_ok(self):
        model = SalesItem(1)
        deleted = model.delete()
        self.assertTrue(deleted)

    def test_delete_ng(self):
        model = SalesItem()
        deleted = model.delete()
        self.assertFalse(deleted)

    def test_monthly_sales_items_by(self):
        rows = SalesItem.find_monthly_sales_items_by('YYYY-mm')
        self.assertEqual(10, len(rows))
