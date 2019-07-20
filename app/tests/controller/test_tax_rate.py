import json
from datetime import datetime
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
        body = result.get_json()
        self.assertEqual(200,  result.status_code)
        self.assertEqual(10, body['tax_rate']['rate'])

    def test_index_when_no_data(self):
        result = self.client.get(
            self.endpoint,
            content_type=self.CONTENT_TYPE
        )
        body = result.get_json()
        self.assertEqual(200,  result.status_code)
        self.assertTrue('tax_rate' in body)
        self.assertIsNone(body['tax_rate'])

    def test_add(self):
        data = json.dumps({
            'rate': 10,
            'reduced_rate': 8,
            'start_date': datetime.now().strftime('%Y-%m-%d'),
            'tax_type': 1
        })
        result = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(200, result.status_code)

    def test_add_when_no_request_data(self):
        result = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(400, result.status_code)

    def test_add_when_responced_validation_error(self):
        data = json.dumps({
            'rate': None,
            'reduced_rate': None,
            'start_date': None,
            'tax_type': None
        })
        result = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(400, result.status_code)

    def test_add_when_conflict_data(self):
        self.init_data()
        data = json.dumps({
            'rate': 10,
            'reduced_rate': 8,
            'start_date': datetime.now().strftime('%Y-%m-%d'),
            'tax_type': 1
        })
        result = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        body = result.get_json()
        self.assertEqual(409, result.status_code)
        self.assertTrue('データが重複しています' in body['message'])

    def init_data(self):
        # see: /db/tests/data/tax_rates.sql
        self.db.execute_proc('create_test_data_tax_rates')
        self.db.commit()
