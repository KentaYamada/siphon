import unittest
from datetime import datetime
from app.model.pgadapter import PgAdapter
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.daily_sales import DailySalesSearchOption
from app.model.mapper.sales_mapper import SalesMapper


class TestSalesMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = SalesMapper()
        self.db = PgAdapter()

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    def test_add_ok(self):
        items = self.__get_sales_items()
        today = datetime.now().date()
        now_time = datetime.now().time()
        sales = Sales(None, today, now_time, 100, 0, 0, 0, 0, 100, items)
        result = self.mapper.add(sales)
        self.assertTrue(result)

    def test_cancel_ok(self):
        items = self.__get_sales_items()
        today = datetime.now().date()
        now_time = datetime.now().time()
        sales = Sales(None, today, now_time, 100, 0, 0, 0, 0, 100, items)
        self.mapper.add(sales)
        result = self.mapper.cancel(1)
        self.assertTrue(result)

    def test_add_ng_when_ivalid_argment(self):
        with self.assertRaises(ValueError):
            self.mapper.add(None)
            self.mapper.add('a')
            self.mapper.add(1)
            self.mapper.add(True)

    def test_cancel_ng_when_invalid_argment(self):
        with self.assertRaises(ValueError):
            self.mapper.cancel(None)
            self.mapper.cancel('a')
            self.mapper.cancel(1)
            self.mapper.cancel(True)
            self.mapper.cancel(0)

    def __get_sales_items(self):
        items = []
        for i in range(1, 11):
            item = SalesItem(None, None, i, 'test{0}'.format(i), 100, 1, 100)
            items.append(item)
        return items
