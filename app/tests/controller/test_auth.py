import json
from app.tests.controller.base import BaseApiTestCase


class TestAuth(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = 'api/auth'
        self.teardown_query = """
            TRUNCATE TABLE users RESTART IDENTITY;
        """

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
        self.assertEqual(200, res.status_code)

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
        self.assertEqual(403, res.status_code)

    def init_data(self):
        self.db.execute_proc('create_test_data_users')
        self.db.commit()
