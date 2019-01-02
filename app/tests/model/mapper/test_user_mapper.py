import unittest
from app.config import get_db_config
from app.model.pgadapter import PgAdapter
from app.model.user import User
from app.model.mapper.user_mapper import UserMapper


class TestUserMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = UserMapper()

    def tearDown(self):
        db = PgAdapter(get_db_config('develop'))
        query = """
            TRUNCATE TABLE users
            RESTART IDENTITY;
        """
        db.execute(query)
        db.commit()

    def test_add_ok(self):
        data = User(
            None,
            'Test user',
            'Mr. test',
            'test@email.com',
            'testtest'
        )
        result = self.mapper.add(data)
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
        result = self.mapper.add(data)
        self.assertTrue(result)

    def test_delete_ok(self):
        self.__init_data()
        result = self.mapper.delete(1)
        self.assertTrue(result)

    def test_add_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.add(None)

    def test_edit_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.edit(None)

    def test_delete_ng_when_invalid_value(self):
        with self.assertRaises(ValueError):
            self.mapper.delete(None)
            self.mapper.delete('1')
            self.mapper.delete(0)
            self.mapper.delete(-1)

    def __init_data(self):
        for i in range(1, 11):
            user = User(
                i,
                'Test user{0}'.format(i),
                'Mr. test{0}'.format(i),
                'test{0}@email.com'.format(i),
                'test{0}test'.format(i)
            )
            self.mapper.add(user)
