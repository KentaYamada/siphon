import unittest
from app.model.item import Item


class TestItem(unittest.TestCase):
    def test_save_ok(self):
        item = Item(1, 1, 'Test Item', 500)
        saved = item.save()
        self.assertTrue(saved)

    def test_save_ng_when_invalid_value(self):
        # category_id
        item = Item(1, None, 'Test Item', 500)
        saved = item.save()
        errors = item.errors
        self.assertFalse(saved)
        self.assertEqual(errors[0]['name'], 'category_id')

        # item name
        item = Item(1, 1, '', 500)
        saved = item.save()
        errors = item.errors
        self.assertFalse(saved)
        self.assertEqual(errors[0]['name'], 'name')

        item = Item(1, 1, None, 500)
        saved = item.save()
        errors = item.errors
        self.assertFalse(saved)
        self.assertEqual(errors[0]['name'], 'name')

        # unit price
        item = Item(1, 1, 'Test Item', None)
        saved = item.save()
        errors = item.errors
        self.assertFalse(saved)
        self.assertEqual(errors[0]['name'], 'unit_price')

        item = Item(1, 1, 'Test Item', 0)
        saved = item.save()
        errors = item.errors
        self.assertFalse(saved)
        self.assertEqual(errors[0]['name'], 'unit_price')

    def test_delete_ok(self):
        item = Item(1)
        deleted = item.delete()
        self.assertTrue(deleted)

    def test_delete_ng(self):
        item = Item(None)
        deleted = item.delete()
        self.assertFalse(deleted)

    def test_find_by(self):
        items = Item.find_by(1)
        self.assertEqual(10, len(items))
