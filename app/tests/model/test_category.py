import unittest
from app.model.category import Category


class TestCategory(unittest.TestCase):
    def tearDown(self):
        model = Category()
        model.db.execute('TRUNCATE TABLE categories RESTART IDENTITY;')
        model.db.commit()

    def test_add_ok(self):
        model = Category(None, 'Test')
        saved = model.save()
        self.assertTrue(saved)

    def test_add_ng_invalid_value(self):
        # id
        model = Category(1, 'test')
        model.id = 'a'
        self.assertFalse(model.is_valid())

        #name 
        model = Category(1, 'test')
        model.name = ''
        self.assertFalse(model.is_valid())

        model = Category(1, 'test')
        model.name = None 
        self.assertFalse(model.is_valid())

    def test_delete_ok(self):
        model = Category(1)
        deleted = model.delete()
        self.assertTrue(deleted)

    def test_delete_ng(self):
        model = Category(None)
        deleted = model.delete()
        self.assertFalse(deleted)

    def test_find_all(self):
        categories = []
        try:
            self._init_categories()
            categories = Category.find_all()
        except Exception as e:
            print(e)
        self.assertEqual(10, len(categories))

    def test_save_ng_when_maximum_rows(self):
        self._init_categories()
        model = Category(None, 'Invalid')
        self.assertFalse(model.is_valid())

    def _init_categories(self):
        data = ['Category{0}'.format(i) for i in range(1, 11)]
        for d in data:
            Category.db.execute(
                'INSERT INTO categories (name) VALUES (%s);',
                (d,))
        Category.db.commit()
