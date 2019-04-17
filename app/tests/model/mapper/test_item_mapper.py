import unittest
from app.model.pgadapter import PgAdapter
from app.model.item import Item, ItemSearchOption
from app.model.mapper.item_mapper import ItemMapper


class TestItemMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = ItemMapper()
        self.db = PgAdapter()

    def tearDown(self):
        self.db = PgAdapter()
        query = """
            TRUNCATE TABLE items
            RESTART IDENTITY;
        """
        self.db.execute(query)
        self.db.commit()

    def test_add_ok(self):
        data = Item(None, 1, 'test', 500)
        result = self.mapper.save(data)
        self.assertTrue(result)

    def test_edit_ok(self):
        self.__init_data()
        item = Item(1, 1, 'Edit', 500)
        result = self.mapper.save(item)
        self.assertTrue(result)

    def test_delete_ok(self):
        self.__init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_find_all_items(self):
        self.__init_data()
        data = ItemSearchOption(1)
        result = self.mapper.find(data)
        self.assertEqual(len(result), 3)

    def test_find_when_empty_row(self):
        data = ItemSearchOption(1, 'No data')
        result = self.mapper.find(data)
        self.assertEqual(len(result), 0)

    def test_find_when_keyword_search(self):
        self.__init_data()
        data = ItemSearchOption(None, 'パスタ')
        result = self.mapper.find(data)
        self.assertEqual(len(result), 2)

    def test_find_when_coplex_search(self):
        self.__init_data()
        data = ItemSearchOption(3, 'パスタ')
        result = self.mapper.find(data)
        self.assertEqual(len(result), 1)

    def test_save_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.save(None)
            self.mapper.save(1)
            self.mapper.save('test')

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def __init_data(self):
        self.db.execute_proc('create_test_data_items')
        self.db.commit()
