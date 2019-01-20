import unittest
from datetime import datetime
from app.model.pgadapter import PgAdapter
from app.model.sales import Sales
from app.model.sales_item import SalesItem
from app.model.mapper.sales_mapper import SalesMapper


class TestSalesMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = SalesMapper()

    def tearDown(self):
        db = PgAdapter()
        query = """
            TRUNCATE TABLE sales
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()
        query2 = """
            TRUNCATE TABLE sales_items
            RESTART IDENTITY;
        """
        db.execute(query2)
        db.commit()

    def test_add_ok(self):
        items = [
            SalesItem(
                None,
                None,
                i,
                'test{0}'.format(i),
                100,
                1,
                100
            )
            for i in range(1, 11)
        ]
        today = datetime.now()
        sales = Sales(None, today, 100, 0, 0, 0, 0, 100, items)
        result = self.mapper.add(sales)
        self.assertTrue(result)

    def test_cancel_ok(self):
        items = [
            SalesItem(
                None,
                None,
                i,
                'test{0}'.format(i),
                100,
                1,
                100
            )
            for i in range(1, 11)
        ]
        today = datetime.now()
        sales = Sales(None, today, 100, 0, 0, 0, 0, 100, items)
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
