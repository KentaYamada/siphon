import unittest
from app.config import get_db_config
from app.model.pgadapter import PgAdapter
from app.model.item import Item
from app.model.mapper.item_mapper import ItemMapper


class TestItemMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = ItemMapper()

    def tearDown(self):
        db = PgAdapter(get_db_config('develop'))
        query = """
            TRUNCATE TABLE items
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_add_ok(self):
        data = Item(None, 1, 'test', 500)
        result = self.mapper.add(data)
        self.assertTrue(result)

    def test_edit_ok(self):
        self.__init_data()
        item = Item(1, 1, 'Edit', 500)
        result = self.mapper.edit(item)
        self.assertTrue(result)

    def test_delete_ok(self):
        self.__init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_add_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.add(None)
            self.mapper.add(1)
            self.mapper.add('test')

    def test_edit_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.edit(None)
            self.mapper.edit(1)
            self.mapper.edit('test')

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def __init_data(self):
        for i in range(1, 3):
            for j in range(1, 31):
                item = Item(j, i, 'Item{0}'.format(j), j*100)
                self.mapper.add(item)
