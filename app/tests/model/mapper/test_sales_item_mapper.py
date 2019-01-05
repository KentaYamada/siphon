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

    def test_find_by_sales_id_ok(self):
        pass

    def test_find_by_sales_id(self):
        with self.assertRaises(ValueError):
            self.mapper.find_by_sales_id(None)
            self.mapper.find_by_sales_id('1')
            self.mapper.cancel(-1)

    def __init_sales_items(self):
        items = []
        for i in range(1, 2):
            for j in range(1, 10):
                item = SalesItem(
                    None,
                    i,
                    j,
                    'Test item{0}'.format(j+1),
                    j*100,
                    1,
                    j*100)
                items.append(item)
        self.mapper.add_items(items)
