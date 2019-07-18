import unittest
from app.model.category import Category


class TestCategory(unittest.TestCase):
    def test_add_ng_invalid_value(self):
        # id
        model = Category('a', 'test')
        self.assertFalse(model.is_valid())

        # name
        model = Category(1, '')
        self.assertFalse(model.is_valid())

        model = Category(1, None)
        self.assertFalse(model.is_valid())
