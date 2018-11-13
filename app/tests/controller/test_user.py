import json
import unittest
from urllib.parse import urljoin
from app import startup_app


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/users/'


class TestUserApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_add_ok(self):
        data = json.dumps({
            'name': 'Test user',
            'nickname': 'nickname',
            'email': 'test@email.com',
            'password': 'test'})
        res = TestUserApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(201, res.status_code)

    def test_add_ng_when_no_data(self):
        res = TestUserApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE)
        self.assertEqual(400, res.status_code)

    def test_add_ng_when_invalid_data(self):
        data = json.dumps({
            'name': '',
            'nickname': 'nickname',
            'email': 'test@email.com',
            'password': 'test'})
        res = TestUserApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(400, res.status_code)

    def test_edit_ok(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': 'Test user',
            'nickname': 'nickname',
            'email': 'test@email.com',
            'password': 'test'})
        res = TestUserApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_edit_ng(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': '',
            'nickname': 'nickname',
            'email': 'test@email.com',
            'password': 'test'})
        res = TestUserApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(409, res.status_code)

    def test_delete_ok(self):
        url = urljoin(END_POINT, '1')
        res = TestUserApi.client.delete(url)
        self.assertEqual(204, res.status_code)

    def test_delete_ng(self):
        res = TestUserApi.client.delete(END_POINT)
        self.assertEqual(405, res.status_code)

    def test_authoricate_ok(self):
        url = urljoin(END_POINT, 'authoricate')
        data = json.dumps({
            'user_id': 'test',
            'password': 'test'
        })
        res = TestUserApi.client.post(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_authoricate_ng(self):
        url = urljoin(END_POINT, 'authoricate')
        data = json.dumps({
            'user_id': 'hoge',
            'password': 'hoge'
        })
        res = TestUserApi.client.post(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(401, res.status_code)

    def test_authoricate_when_bad_request(self):
        url = urljoin(END_POINT, 'authoricate')
        res = TestUserApi.client.post(
            url,
            content_type=CONTENT_TYPE)
        self.assertEqual(400, res.status_code)
