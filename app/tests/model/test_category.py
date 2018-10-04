import unittest
from app.model.category import Category


class TestCategory(unittest.TestCase):
    def tearDown(self):
        model = Category()
        model.db.execute('TRUNCATE TABLE categories RESTART IDENTITY;')
        model.db.commit()

    def test_add_ok(self):
        saved = False
        category = Category(None, 'Test')
        try:
            saved = category.save()
        except Exception as e:
            print(e)
            saved = False
        self.assertTrue(saved)

    def test_add_ng_invalid_value(self):
        saved = False
        category = Category(None, '')
        try:
            saved = category.save()
        except Exception as e:
            print(e)
            saved = False
        self.assertFalse(saved)

        category = Category(None, None)
        try:
            saved = category.save()
        except Exception as e:
            print(e)
            saved = False
        self.assertFalse(saved)

    def test_delete_ok(self):
        deleted = False
        category = Category(1)
        try:
            deleted = category.delete()
        except Exception as e:
            print(e)
            deleted = False
        self.assertTrue(deleted)

    def test_delete_ng(self):
        deleted = False
        category = Category(None)
        try:
            deleted = category.delete()
        except Exception as e:
            print(e)
            deleted = False
        self.assertFalse(deleted)

    def test_find_all(self):
        categories = []
        try:
            self._init_categories()
            categories = Category.find_all()
        except Exception as e:
            print(e)
        self.assertEqual(10, len(categories))

    def _init_categories(self):
        data = ['Category{0}'.format(i) for i in range(1, 11)]
        for d in data:
            Category.db.execute(
                'INSERT INTO categories (name) VALUES (%s);',
                (d,))
        Category.db.commit()
