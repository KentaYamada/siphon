import unittest
from app.model.category import Category


class TestCategory(unittest.TestCase):
    def test_add_ok(self):
        category = Category(None, 'Test')
        saved = category.save()
        self.assertTrue(saved)

    def test_add_ng_invalid_value(self):
        category = Category(None, '')
        saved = category.save()
        self.assertFalse(saved)
        category = Category(None, None)
        saved = category.save()
        self.assertFalse(saved)

    def test_delete_ok(self):
        category = Category(1)
        deleted = category.delete()
        self.assertTrue(deleted)

    def test_delete_ng(self):
        category = Category(None)
        deleted = category.delete()
        self.assertFalse(deleted)

    def test_find_all(self):
        categories = Category.find_all()
        self.assertEqual(10, len(categories))
