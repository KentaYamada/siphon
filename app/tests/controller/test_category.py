import json
import unittest
from urllib.parse import urljoin
from app import startup_app


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/categories/'


class TestCategoryApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_index(self):
        res = TestCategoryApi.client.get(
            END_POINT,
            content_type=CONTENT_TYPE)
        self.assertEqual(200, res.status_code)

    def test_add_ok(self):
        data = json.dumps({
            'id': None,
            'name': 'Test'})
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(201, res.status_code)

    def test_add_ng_when_no_data(self):
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE)
        self.assertEqual(400, res.status_code)

    def test_add_ng_when_invalid_data(self):
        data = json.dumps({
            'id': None,
            'name': ''})
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(400, res.status_code)

    def test_edit_ok(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': 'Test Category'
        })
        res = TestCategoryApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_edit_ng(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': ''
        })
        res = TestCategoryApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(409, res.status_code)

    def test_delete_ok(self):
        url = urljoin(END_POINT, '1')
        res = TestCategoryApi.client.delete(url)
        self.assertEqual(204, res.status_code)

    def test_delete_ng(self):
        res = TestCategoryApi.client.delete(END_POINT)
        self.assertEqual(405, res.status_code)
