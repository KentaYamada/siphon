import unittest
from app.config import get_db_config
from app.model.pgadapter import PgAdapter
from app.model.category import Category
from app.model.mapper.category_mapper import CategoryMapper


class TestCategoryMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = CategoryMapper()

    def tearDown(self):
        db = PgAdapter(get_db_config('develop'))
        query = """
            TRUNCATE TABLE categories
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_add_ok(self):
        data = Category(None, 'test')
        result = self.mapper.add(data)
        self.assertTrue(result)

    def test_edit_ok(self):
        self.__init_data()
        data = Category(1, 'Edit test')
        result = self.mapper.edit(data)
        self.assertTrue(result)

    def test_delete_ok(self):
        self.__init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_is_upper_limit(self):
        self.__init_data()
        result = self.mapper.is_upper_limit()
        self.assertTrue(result)

    def test_less_than_limit(self):
        self.__init_data()
        self.mapper.delete(1)
        result = self.mapper.is_upper_limit()
        self.assertLess(result, 10)

    def test_find_all_ok(self):
        pass
        # self.__init_data()
        # result = self.mapper.find_all()
        # self.assertEqual(len(result), 10)

    def test_add_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.add(None)

    def test_edit_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.edit(None)

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def __init_data(self):
        for i in range(1, 11):
            category = Category(i, 'Test{0}'.format(i))
            self.mapper.add(category)
