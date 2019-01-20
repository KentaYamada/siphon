import unittest
from app.model.pgadapter import PgAdapter
from app.model.mapper.sales_item_mapper import SalesItemMapper


class TestSalesItemMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = SalesItemMapper()

    def tearDown(self):
        db = PgAdapter()
        query = """
            TRUNCATE TABLE sales_items
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_find_by_sales_ids_ok(self):
        self.__init_sales_items()
        result = self.mapper.find_by_sales_ids([1, 2])
        self.assertEqual(len(result), 20)

    def test_find_by_sales_ids_when_empty_row(self):
        result = self.mapper.find_by_sales_ids([1])
        self.assertEqual(len(result), 0)

    def test_find_by_sales_ids(self):
        with self.assertRaises(ValueError):
            self.mapper.find_by_sales_ids(None)
            self.mapper.find_by_sales_ids('1')
            self.mapper.cancel([1, 2, 3, -1])

    def __init_sales_items(self):
        query = """
            INSERT INTO sales_items (
                sales_id,
                item_no,
                item_name,
                unit_price,
                quantity,
                subtotal
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );
        """
        items = []
        for i in range(1, 3):
            for j in range(1, 11):
                item = (
                    i,
                    j,
                    'Test item{0}'.format(j+1),
                    j*100,
                    1,
                    j*100)
                items.append(item)
        self.mapper._db.bulk_insert(query, items)
        self.mapper._db.commit()
