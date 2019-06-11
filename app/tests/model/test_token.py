import unittest
from app.model.token import Token


class TestToken(unittest.TestCase):
    def test_user_id_when_user_id_is_none_value(self):
        model = Token(None, 'test')
        self.assertFalse(model.is_valid())
        self.assertTrue('user_id' in model.validation_errors)

    def test_validate_when_user_id_is_invalid_type(self):
        model = Token('1', 'test')
        self.assertFalse(model.is_valid())
        self.assertTrue('user_id' in model.validation_errors)

    def test_validate_when_token_is_empty(self):
        model = Token(1, '')
        self.assertFalse(model.is_valid())
        self.assertTrue('token' in model.validation_errors)

        model.token = None
        self.assertFalse(model.is_valid())
        self.assertTrue('token' in model.validation_errors)

    def test_validate_when_token_is_invalid_type(self):
        model = Token(1, 1)
        self.assertFalse(model.is_valid())
        self.assertTrue('token' in model.validation_errors)

        model.token = True
        self.assertFalse(model.is_valid())
        self.assertTrue('token' in model.validation_errors)
