from datetime import datetime
from unittest import TestCase
from app.model.pgadapter import PgAdapter
from app.model.mapper.sales_mapper import SalesMapper


class TestMonthlySales(TestCase):
    def setUp(self):
        self.mapper = SalesMapper()
        self.today = datetime.today()

    def tearDown(self):
        db = PgAdapter()
        query = """
            TRUNCATE TABLE sales
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_find_monthly_sales(self):
        data = [[self.today, 100, 0, 0, 0, 0, 100] for i in range(0, 3)]
        self.__init_data(data)

        year = self.today.year
        month = self.today.month
        result = self.mapper.find_monthly_sales(year, month)
        self.assertNotEqual(len(result), 0)
        self.assertEqual(result[1].proceeds, 300)

    def test_find_monthly_sales_when_include_discount_price(self):
        data = (
            [self.today, 500, 100, 0, 0, 0, 500],
            [self.today, 800, 0, 0, 0, 0, 1000],
            [self.today, 450, 50, 0, 0, 0, 500])
        expected = 0
        for d in data:
            expected += (d[1] - d[2])
        self.__init_data(data)

        year = self.today.year
        month = self.today.month
        result = self.mapper.find_monthly_sales(year, month)
        self.assertNotEqual(len(result), 0)
        self.assertEqual(result[0].proceeds, expected)

    def test_find_monthly_sales_when_include_discount_rate(self):
        data = (
            [self.today, 500, 0, 10, 0, 0, 500],
            [self.today, 800, 0, 15, 0, 0, 1000],
            [self.today, 450, 0, 0, 0, 0, 500])
        expected = 0
        for d in data:
            expected += (d[1] * (1 - d[3] / 100))
        self.__init_data(data)

        year = self.today.year
        month = self.today.month
        result = self.mapper.find_monthly_sales(year, month)
        self.assertNotEqual(len(result), 0)
        self.assertEqual(result[0].proceeds, expected)

    def test_find_monthly_sales_when_invalid_arguments(self):
        year = self.today.year
        month = self.today.month
        with self.assertRaises(ValueError):
            self.mapper.find_monthly_sales(None, month)
            self.mapper.find_monthly_sales(year, None)
            self.mapper.find_monthly_sales('2000', month)
            self.mapper.find_monthly_sales(year, '999')
            self.mapper.find_monthly_sales(year, 0)
            self.mapper.find_monthly_sales(year, 13)

    def __init_data(self, data):
        query = """
            INSERT INTO sales (
                sales_date,
                total_price,
                discount_price,
                discount_rate,
                inclusive_tax,
                exclusive_tax,
                deposit
            ) VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            );

        """
        db = PgAdapter()
        db.bulk_insert(query, data)
        db.commit()
