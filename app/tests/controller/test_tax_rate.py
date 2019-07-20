import json
from app.tests.controller.base import BaseApiTestCase


class TestTaxRate(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = '/api/tax_rates'
        self.teardown_query = """
            TRUNCATE TABLE tax_rates RESTART IDENTITY;
        """

    def test_index(self):
        self.init_data()
        result = self.client.get(
            self.endpoint,
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(result.data)
        self.assertEqual(200,  result.status_code)
        self.assertEqual(10, body['tax_rate']['rate'])

    def test_index_when_no_data(self):
        result = self.client.get(
            self.endpoint,
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(result.data)
        self.assertEqual(200,  result.status_code)
        self.assertTrue('tax_rate' in body)
        self.assertIsNone(body['tax_rate'])

    def init_data(self):
        # see: /db/tests/data/tax_rates.sql
        self.db.execute_proc('create_test_data_tax_rates')
        self.db.commit()
