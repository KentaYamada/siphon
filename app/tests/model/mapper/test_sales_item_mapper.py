from calendar import monthrange
from datetime import datetime, timedelta
from unittest import TestCase
from app.model.pgadapter import PgAdapter
from app.model.sales_item import PopularSalesItemSearchOption
from app.model.mapper.sales_item_mapper import SalesItemMapper


class TestSalesItemMapper(TestCase):
    def setUp(self):
        self.mapper = SalesItemMapper()
        self.db = PgAdapter()

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    def test_find_daily_sales_items(self):
        self.__init_daily_sales_data()
        rows = self.mapper.find_daily_sales_items([1, 3])
        self.assertNotEquals(0, len(rows))

    def test_find_daily_sales_items_when_empty_row(self):
        rows = self.mapper.find_daily_sales_items([4])
        self.assertEquals(0, len(rows))

    def test_find_daily_sales_items_when_invalid_arg(self):
        with self.assertRaises(ValueError):
            self.mapper.find_daily_sales_items(None)
            self.mapper.find_daily_sales_items('')
            self.mapper.find_daily_sales_items(1)
            self.mapper.find_daily_sales_items(True)

    def test_find_popular_items(self):
        self.__init_popular_sales_items()
        today = datetime.today().date()
        _, last = monthrange(today.year, today.month)
        start_date = datetime(today.year, today.month, 1).date()
        end_date = datetime(today.year, today.month, last).date()
        option = PopularSalesItemSearchOption(start_date, end_date)
        result = self.mapper.find_popular_items(option)
        self.assertNotEquals(0, len(result))

    def test_find_popular_items_when_no_data(self):
        today = datetime.today().date()
        option = PopularSalesItemSearchOption(today, today)
        result = self.mapper.find_popular_items(option)
        self.assertEquals(0, len(result))

    def test_find_popular_items_when_empty_row(self):
        self.__init_popular_sales_items()
        # todo: 未登録な日付
        today = datetime.today().date() - timedelta(days=1)
        option = PopularSalesItemSearchOption(today, today)
        result = self.mapper.find_popular_items(option)
        self.assertEquals(0, len(result))

    def test_find_popular_items_when_invalid_arg(self):
        with self.assertRaises(ValueError):
            self.mapper.find_popular_items(None)
            self.mapper.find_popular_items('')
            self.mapper.find_popular_items(1)
            self.mapper.find_popular_items(True)

    def __init_daily_sales_data(self):
        self.db.execute_proc('create_test_data_daily_sales_items')
        self.db.commit()

    def __init_popular_sales_items(self):
        self.db.execute_proc('create_test_data_popular_sales_items')
        self.db.commit()
