from unittest import TestCase
from app import startup_app
from app.model.pgadapter import PgAdapter


class BaseApiTestCase(TestCase):
    # constants
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.db = PgAdapter()
        self.endpoint = ''

    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def init_data(self):
        raise NotImplementedError()
