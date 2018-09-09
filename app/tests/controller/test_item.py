import json
import unittest
from urllib.parse import urljoin
from app import startup_app


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/items/'


class TestItem(unittest.TestCase):
    def setUp(self):
        app = startup_app()
        self.api = app.test_client()

    def tearDown(self):
        self.api = None

    def test_index(self):
        res = self.api.get(END_POINT)
        self.assertEqual(200, res.status_code)

    def test_add_success(self):
        data = json.dumps({
            'id': None,
            'category_id': 1,
            'name': 'Test item',
            'unit_price': 500
        })
        res = self.api.post(
            END_POINT,
            content_type='application/json',
            data=data)
        self.assertEqual(201, res.status_code)

    def test_add_when_empty_data(self):
        res = self.api.post(
            END_POINT,
            content_type='application/json')
        self.assertEqual(400, res.status_code)
