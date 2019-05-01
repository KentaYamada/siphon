import json
from unittest import TestCase
from app import startup_app
from app.model.pgadapter import PgAdapter


class TestDashboardApi(TestCase):
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.db = PgAdapter()

    def tearDown(self):
        self.db.execute_proc('cleanup_sales')
        self.db.commit()

    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_index_status_200(self):
        self.__init_data()
        url = '/api/dashboard/{0}/{1}'.format(2019, 5)
        res = self.client.get(
            url,
            content_type=self.CONTENT_TYPE
        )
        body = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertNotEqual(0, len(body['popular_items']))

    def __init_data(self):
        self.db.execute_proc('create_test_data_popular_sales_items')
        self.db.commit()
