import json
import unittest
from urllib.parse import urljoin
from app import startup_app


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/items/'


class TestItemApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_index(self):
        res = TestItemApi.client.get(END_POINT)
        self.assertEqual(200, res.status_code)

    def test_add_success(self):
        data = json.dumps({
            'id': None,
            'category_id': 1,
            'name': 'Test item',
            'unit_price': 500
        })
        res = TestItemApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(201, res.status_code)

    def test_add_ng_when_no_data(self):
        res = TestItemApi.client.post(
            END_POINT,
            content_type='application/json')
        self.assertEqual(400, res.status_code)

    def test_add_ng_when_invalid_data(self):
        data = json.dumps({
            'id': None,
            'category_id': 1,
            'name': 'Test item',
            'unit_price': None
        })
        res = TestItemApi.client.post(
            END_POINT,
            content_type='application/json',
            data=data)
        self.assertEqual(400, res.status_code)

    def test_edit_ok(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'category_id': 1,
            'name': 'Test item',
            'unit_price': 500
        })
        res = TestItemApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_edit_ng(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'category_id': None,
            'name': 'Test item',
            'unit_price': 500
        })
        res = TestItemApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(409, res.status_code)

    def test_delete_ok(self):
        url = urljoin(END_POINT, '1')
        res = TestItemApi.client.delete(url)
        self.assertEqual(204, res.status_code)

    def test_delete_ng(self):
        res = TestItemApi.client.delete(END_POINT)
        self.assertEqual(405, res.status_code)
