import unittest
from app.model.user import User


class TestUser(unittest.TestCase):
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
