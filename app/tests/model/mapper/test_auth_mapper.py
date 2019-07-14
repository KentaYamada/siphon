from app.model.token import Token
from app.model.mapper.auth_mapper import AuthMapper
from app.tests.model.mapper.base import BaseMapperTestCase


class TestAuthMapper(BaseMapperTestCase):
    def setUp(self):
        super().setUp()
        self.mapper = AuthMapper()

    def tearDown(self):
        queries = [
            'TRUNCATE TABLE tokens RESTART IDENTITY;',
            'TRUNCATE TABLE black_lists RESTART IDENTITY;'
        ]
        for query in queries:
            self.db.execute(query)
        self.db.commit()

    def test_save_token(self):
        data = Token(1, 'test')
        result = self.mapper.save_token(data)
        self.assertTrue(result)

    def test_save_token_when_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.mapper.save_token(None)
            self.mapper.save_token('')
            self.mapper.save_token(True)

    def test_dispose_token(self):
        self.init_data()
        result = self.mapper.dispose_token('hoge')
        self.assertTrue(result)

    # todo
    # def test_dispose_token_when_target_has_no_record(self):
    #     self.init_data()
    #     result = self.mapper.dispose_token('no token')
    #     self.assertFalse(result)

    def test_dispose_token_when_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.mapper.dispose_token('')
            self.mapper.dispose_token(None)
            self.mapper.dispose_token(1)
            self.mapper.dispose_token(False)

    def test_has_blacklist(self):
        self.db.execute_proc('create_test_data_black_lists')
        self.db.commit()
        result = self.mapper.has_blacklist('hoge')
        self.assertTrue(result)

    def test_has_blacklist_when_no_record(self):
        self.db.execute_proc('create_test_data_black_lists')
        self.db.commit()
        result = self.mapper.has_blacklist('white')
        self.assertFalse(result)

    def test_has_blacklist_when_invalid_argument(self):
        with self.assertRaises(ValueError):
            self.mapper.has_blacklist(None)
            self.mapper.has_blacklist('')
            self.mapper.has_blacklist('1')
            self.mapper.has_blacklist(1)
            self.mapper.has_blacklist(True)

    def init_data(self):
        # see /db/test/data/token.sql
        self.db.execute_proc('create_test_data_tokens')
        self.db.commit()
