import json
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper
from app.tests.controller.base import BaseApiTestCase


class TestAuth(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = '/api/auth'
        self.logout_url = '/api/auth/logout'
        self.reflesh_url = '/api/auth/reflesh'

    def tearDown(self):
        queries = [
            'TRUNCATE TABLE users RESTART IDENTITY;',
            'TRUNCATE TABLE tokens RESTART IDENTITY;',
            'TRUNCATE TABLE black_lists RESTART IDENTITY;'
        ]
        for query in queries:
            self.db.execute(query)
        self.db.commit()

    def test_login(self):
        self.init_data()
        data = json.dumps({
            'email': 'test.taro@email.com',
            'password': 'tarosan'
        })
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        data = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertTrue(data['logged_in'])

    def test_login_when_empty_request_data(self):
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(400, res.status_code)

    def test_login_when_invalid_request_data(self):
        data = json.dumps({
            'hoge': 'hoge',
            'password': 'test'
        })
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(400, res.status_code)

    def test_login_when_invalid_account(self):
        self.init_data()
        data = json.dumps({
            'email': 'who.is.this@email.com',
            'password': 'whoisthis'
        })
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(401, res.status_code)

    def test_login_when_invalid_password(self):
        self.init_data()
        data = json.dumps({
            'email': 'test.taro@email.com',
            'password': 'invalid'
        })
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(401, res.status_code)

    def test_logout(self):
        self.init_data()
        # login and get access token
        data = json.dumps({
            'email': 'test.taro@email.com',
            'password': 'tarosan'
        })
        res = self.client.post(
            self.endpoint,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        response_data = json.loads(res.data)
        token = response_data['auth_token']
        # logout request
        logout_data = json.dumps({'token': token})
        res = self.client.post(
            self.logout_url,
            content_type=self.CONTENT_TYPE,
            data=logout_data
        )
        logout_response = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertTrue(logout_response['logged_out'])

    def test_logout_when_empty_request_data(self):
        res = self.client.post(
            self.logout_url,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(400, res.status_code)

    def test_logout_when_invalid_request_data(self):
        data = json.dumps({'hoge': 'hoge'})
        res = self.client.post(
            self.logout_url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(400, res.status_code)

    def test_reflesh(self):
        pass

    def test_reflesh_when_empty_request_data(self):
        res = self.client.post(
            self.reflesh_url,
            content_type=self.CONTENT_TYPE
        )
        self.assertEqual(400, res.status_code)

    def test_reflesh_when_invalid_request_data(self):
        data = json.dumps({'hoge': 'hoge'})
        res = self.client.post(
            self.reflesh_url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(400, res.status_code)

    def test_reflesh_when_request_invalid_access_token(self):
        data = json.dumps({'token': 'invalid'})
        res = self.client.post(
            self.reflesh_url,
            content_type=self.CONTENT_TYPE,
            data=data
        )
        self.assertEqual(400, res.status_code)

    def init_data(self):
        user = User(
            name='Test taro',
            nickname='tarosan',
            email='test.taro@email.com',
            password='tarosan'
        )
        mapper = UserMapper()
        mapper.save(user)
