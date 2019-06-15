import json
from datetime import datetime
from app.tests.controller.base import BaseApiTestCase


class TestDashboardApi(BaseApiTestCase):
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        super().setUp()
        self.endpoint = '/api/dashboard'

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    def test_index(self):
        self.init_data()
        today = datetime.now().date()
        url = '/api/dashboard/{0}/{1}'.format(today.year, today.month)
        res = self.client.get(
            url,
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertNotEqual(0, len(body['popular_items']))

    def init_data(self):
        self.db.execute_proc('create_test_data_popular_sales_items')
        self.db.commit()
