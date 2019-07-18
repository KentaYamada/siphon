import json
from datetime import datetime
from app.tests.controller.base import BaseApiTestCase


class TestDailySales(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = '/api/sales/daily'

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    def test_index(self):
        self.init_data()
        sales_date = datetime.now().strftime('%Y-%m-%d')
        url = '{0}?sales_date={1}'.format(self.endpoint, sales_date)
        res = self.client.get(url, content_type=self.CONTENT_TYPE)
        body = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertNotEquals(0, len(body['daily_sales']))

    def init_data(self):
        self.db.execute_proc('create_test_data_daily_sales')
        self.db.execute_proc('create_test_data_daily_sales_items')
        self.db.commit()
