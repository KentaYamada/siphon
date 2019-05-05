from unittest import TestCase
from app import startup_app
from app.model.pgadapter import PgAdapter


class BaseApiTestCase(TestCase):
    # constants
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.db = PgAdapter()
        self.endpoint = ''
        self.teardown_query = ''

    def tearDown(self):
        if self.teardown_query:
            self.db.execute(self.teardown_query)
            self.db.commit()
        self.db = None

    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def init_data(self):
        raise NotImplementedError()
