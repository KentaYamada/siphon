import unittest
from app.config import get_db_config
from app.model.sales_item import SalesItem
from app.model.pgadapter import PgAdapter
from app.model.mapper.sales_item_mapper import SalesItemMapper


class TestSalesItemMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = SalesItemMapper()

    def tearDown(self):
        db = PgAdapter(get_db_config('develop'))
        query = """
            TRUNCATE TABLE sales_items
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_add_items_ok(self):
        items = [SalesItem(
            None,
            1,
            i,
            'Test item{0}'.format(i+1),
            (1)*100,
            1,
            (1)*100)
            for i in range(1, 11)]
        result = self.mapper.add_items(items)
        self.assertTrue(result)

    def test_cancel_ok(self):
        self.__init_sales_items()
        result = self.mapper.cancel(3, 1)
        self.assertTrue(result)

    def test_find_by_sales_id_ok(self):
        pass

    def test_add_items_ng_when_empty_item(self):
        result = self.mapper.add_items([])
        self.assertFalse(result)

    def test_add_items_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.add_items(None)
            self.mapper.add_items('invalid')
            self.mapper.add_items(100)

    def test_cancel_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.cancel(None, None)
            self.mapper.cancel('invalid', 1)
            self.mapper.cancel(1, 'invalid')
            self.mapper.cancel('1', 1)
            self.mapper.cancel(1, '1')
            self.mapper.cancel(-1, 1)
            self.mapper.cancel(1, -1)

    def test_find_by_sales_id(self):
        with self.assertRaises(ValueError):
            self.mapper.find_by_sales_id(None)
            self.mapper.find_by_sales_id('1')
            self.mapper.cancel(-1)

    def __init_sales_items(self):
        items = []
        for i in range(1, 2):
            for j in range(1, 10):
                items.append(
                        SalesItem(
                            None, i, j, 'Test item{0}'.format(j+1),
                            (j)*100, 1, (j)*100))
        self.mapper.add_items(items)
