import unittest
from app.model.sales_item import SalesItem


class TestSalesItemTest(unittest.TestCase):
    def test_save_ng_when_invalid_value(self):
        pass
    #    # sales_id
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('sales_id', errors[0]['name'])

    #    # item_no
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    model = SalesItem(
    #            None, sales_id=1, sales_date='2018/01/01 10:00:00',
    #            item_no=None, item_name='Test', unit_price=500,
    #            quantity=1, subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('item_no', errors[0]['name'])

    #    # item_name
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('item_name', errors[0]['name'])

    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('item_name', errors[0]['name'])

    #    # unit_price
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    model = SalesItem(
    #            None, sales_id=1, sales_date='2018/01/01 10:00:00',
    #            item_no=1, item_name='Test', unit_price=None,
    #            quantity=1, subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('unit_price', errors[0]['name'])

    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('unit_price', errors[0]['name'])

    #    # quantity
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('quantity', errors[0]['name'])

    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('quantity', errors[0]['name'])

    #    # subtotal
    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('subtotal', errors[0]['name'])

    #    model = SalesItem(None, sales_id=1, item_no=1,
    #                      item_name='Test', unit_price=500, quantity=1,
    #                      subtotal=500)
    #    saved = model.save()
    #    errors = model.errors
    #    self.assertFalse(saved)
    #    self.assertEqual('subtotal', errors[0]['name'])
