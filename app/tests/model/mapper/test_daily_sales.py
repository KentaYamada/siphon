from datetime import datetime
from unittest import TestCase
from app.model.pgadapter import PgAdapter
from app.model.daily_sales import DailySalesSearchOption
from app.model.mapper.sales_mapper import SalesMapper


class TestDailySales(TestCase):
    def setUp(self):
        self.mapper = SalesMapper()
        self.db = PgAdapter()
        self.today = datetime.now()

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    def test_find_daily_sales(self):
        self.__init_data()
        option = DailySalesSearchOption(
            sales_date=self.today.date(),
            start_time=self.__get_time('09:00:00'),
            end_time=self.__get_time('21:00:00')
        )
        result = self.mapper.find_daily_sales(option)
        self.assertNotEqual(0, len(result))

    def test_find_daily_sales_when_set_start_time(self):
        self.__init_data()
        option = DailySalesSearchOption(
            sales_date=self.today.date(),
            start_time=self.__get_time('12:00:00'),
            end_time=None
        )
        result = self.mapper.find_daily_sales(option)
        self.assertEquals(1, len(result))

    def test_find_daily_sales_when_set_end_time(self):
        self.__init_data()
        option = DailySalesSearchOption(
            sales_date=self.today.date(),
            start_time=None,
            end_time=self.__get_time('10:00:00')
        )
        result = self.mapper.find_daily_sales(option)
        self.assertEquals(2, len(result))

    def test_find_daily_sales_when_empty_row(self):
        option = DailySalesSearchOption(
            sales_date=self.today.date(),
            start_time=self.__get_time('09:00:00'),
            end_time=self.__get_time('21:00:00')
        )
        result = self.mapper.find_daily_sales(option)
        self.assertEqual(0, len(result))

    def test_find_daily_sales_when_no_row(self):
        self.__init_data()
        option = DailySalesSearchOption(
            sales_date=self.today.date(),
            start_time=self.__get_time('13:00:00'),
            end_time=self.__get_time('21:00:00')
        )
        result = self.mapper.find_daily_sales(option)
        self.assertEqual(0, len(result))

    def test_find_daily_sales_when_invalid_args(self):
        with self.assertRaises(ValueError):
            self.mapper.find_daily_sales(None)
            self.mapper.find_daily_sales('Test')
            self.mapper.find_daily_sales(2)
            self.mapper.find_daily_sales(True)

    def __init_data(self):
        self.db.execute_proc('create_test_data_daily_sales')
        self.db.commit()

    def __get_time(self, value):
        return datetime.strptime(value, '%H:%M:%S').time()
