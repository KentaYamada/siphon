import unittest
from app.model.pgadapter import PgAdapter
from app.model.user import User, UserSearchOption
from app.model.mapper.user_mapper import UserMapper


class TestUserMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = UserMapper()
        self.db = PgAdapter()

    def tearDown(self):
        query = """
            TRUNCATE TABLE users
            RESTART IDENTITY;
        """
        self.db.execute(query)
        self.db.commit()
        self.db = None

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
        self.__init_data()
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
        self.__init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_find_by_ok(self):
            self.__init_data()
            data = UserSearchOption()
            result = self.mapper.find(data)
            self.assertEqual(len(result), 3)

    def test_save_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.save(None)

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def __init_data(self):
        self.db.execute_proc('create_test_data_users')
        self.db.commit()
