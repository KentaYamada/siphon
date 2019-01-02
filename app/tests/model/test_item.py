import unittest
from app.model.item import Item


class TestItem(unittest.TestCase):
    def test_save_ng_when_invalid_value(self):
        # category_id
        item = Item(1, None, 'Test Item', 500)
        is_valid = item.is_valid()
        self.assertFalse(is_valid)

        # item name
        item = Item(1, 1, '', 500)
        is_valid = item.is_valid()
        self.assertFalse(is_valid)

        item = Item(1, 1, None, 500)
        is_valid = item.is_valid()
        self.assertFalse(is_valid)

        # unit price
        item = Item(1, 1, 'Test Item', None)
        is_valid = item.is_valid()
        self.assertFalse(is_valid)

        item = Item(1, 1, 'Test Item', 0)
        is_valid = item.is_valid()
        self.assertFalse(is_valid)

    def test_find_by(self):
        items = Item.find_by(1)
        self.assertEqual(10, len(items))
