from app.model.token import Token
from app.model.mapper.auth_mapper import AuthMapper
from app.tests.model.mapper.base import BaseMapperTestCase


class TestAuthMapper(BaseMapperTestCase):
    def setUp(self):
        super().setUp()
        self.mapper = AuthMapper()
        self.teardown_query = """
            TRUNCATE TABLE tokens
            RESTART IDENTITY;
        """

    def test_save_token(self):
        data = Token(1, 'test')
        result = self.mapper.save_token(data)
        self.assertTrue(result)
