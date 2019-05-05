from unittest import TestCase
from app.model.pgadapter import PgAdapter


class BaseMapperTestCase(TestCase):
    def setUp(self):
        self.db = PgAdapter()
        self.mapper = None
        self.teardown_query = ''

    def tearDown(self):
        if self.teardown_query:
            self.db.execute(self.teardown_query)
            self.db.commit()
            self.db = None

    def init_data(self):
        raise NotImplementedError()
