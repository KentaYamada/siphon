from datetime import datetime
from app.model.tax_rate import TaxRate
from app.model.mapper.tax_rate_mapper import TaxRateMapper
from app.tests.model.mapper.base import BaseMapperTestCase


class TestTaxRateMapper(BaseMapperTestCase):
    def setUp(self):
        super().setUp()
        self.mapper = TaxRateMapper()
        self.teardown_query = """
            TRUNCATE TABLE tax_rates RESTART IDENTITY;
        """

    def test_save(self):
        data = TaxRate(10, 8, datetime.now().date(), 1)
        result = self.mapper.save(data)
        self.assertTrue(result)

    def test_save_when_pass_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.mapper.save(None)
            self.mapper.save('')
            self.mapper.save(1)
            self.mapper.save(True)
            self.mapper.save([])

    def test_find_current_tax_rate(self):
        self.init_data()
        result = self.mapper.find_current_tax_rate()
        self.assertIsNotNone(result)
        self.assertEqual(10, result['rate'])
        self.assertEqual(8, result['reduced_rate'])

    def test_find_crrent_tax_rate_when_no_data(self):
        result = self.mapper.find_current_tax_rate()
        self.assertIsNone(result)

    def init_data(self):
        # see: /db/tests/data/tax_rates.sql
        self.db.execute_proc('create_test_data_tax_rates')
        self.db.commit()
