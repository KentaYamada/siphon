import unittest
from app.model.user import User


class TestUser(unittest.TestCase):
    def tearDown(self):
        model = User()
        model.db.execute('TRUNCATE TABLE users RESTART IDENTITY;')
        model.db.commit()

    def test_add_ok(self):
        model = User(None, 'test', 'test', 'test@email.com', 'testtest')
        saved = model.save()
        self.assertTrue(saved)

    def test_invalid_value(self):
        # id
        model = User(1, 'test', 'test', 'test@email.com', 'testtest')
        model.id = 'a'
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        # name
        model = User(1, 'test', 'test', 'test@email.com', 'testtest')
        model.name = ''
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        model = User(1, 'test', 'test', 'test@email.com', 'testtest')
        model.name = None
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        # email
        model = User(1, 'test', 'test', 'test@email.com', 'testtest')
        model.email = ''
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        model = User(1, 'test', 'test', 'test@email.com', 'testtest')
        model.email = None
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        # password
        model = User(1, 'test', 'test', 'test@password.com', 'testtest')
        model.password = ''
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

        model = User(1, 'test', 'test', 'test@password.com', 'testtest')
        model.password = None
        is_valid = model.is_valid()
        self.assertFalse(is_valid)

    def test_delete_ok(self):
        model = User(None, 'Test', 'Test', 'test@email.com', 'testtest')
        model.save()
        model = User(1)
        deleted = model.delete()
        self.assertTrue(deleted)
