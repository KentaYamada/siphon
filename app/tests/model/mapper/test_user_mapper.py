# import unittest
from app.model.pgadapter import PgAdapter
from app.model.user import User, UserSearchOption
from app.model.mapper.user_mapper import UserMapper
from app.tests.model.mapper.base import BaseMapperTestCase


class TestUserMapper(BaseMapperTestCase):
    def setUp(self):
        super().setUp()
        self.mapper = UserMapper()
        # self.db = PgAdapter()
        self.teardown_query = """
            TRUNCATE TABLE users
            RESTART IDENTITY;
        """

    def test_add_ok(self):
        data = User(
            None,
            'Test user',
            'Mr. test',
            'test@email.com',
            'testtest'
        )
        result = self.mapper.save(data)
        self.assertTrue(result)

    def test_edit_ok(self):
        self.init_data()
        data = User(
            1,
            'Edit user',
            'Mr. test',
            'test@email.com',
            'testtest'
        )
        result = self.mapper.save(data)
        self.assertTrue(result)

    def test_delete_ok(self):
        self.init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_find_ok_when_no_condition(self):
        self.init_data()
        data = UserSearchOption()
        result = self.mapper.find(data)
        self.assertEqual(len(result), 3)

    def test_find_ok_when_keyword_search(self):
        self.init_data()
        data = UserSearchOption(q='太郎')
        result = self.mapper.find(data)
        self.assertEqual(len(result), 1)

    def test_find_auth_user(self):
        self.init_data()
        data = User(
            email='test.taro@email.com',
            password='tarosan'
        )
        result = self.mapper.find_auth_user(data)
        self.assertIsNotNone(result)

    def test_find_auth_user_when_no_user(self):
        self.init_data()
        data = User(
            email='whoisthis@email.com',
            password='whoisthis'
        )
        result = self.mapper.find_auth_user(data)
        self.assertIsNone(result)

    def test_save_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.save(None)

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def test_find_auth_user_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.find_auth_user(None)
            self.mapper.find_auth_user('Test')
            self.mapper.find_auth_user(1)
            self.mapper.find_auth_user(True)

    def init_data(self):
        self.db.execute_proc('create_test_data_users')
        self.db.commit()
