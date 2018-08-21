import unittest
import app.model.response as res


class TestResponseBodyCreator(unittest.TestCase):
    def setUp(self):
        self.__res = res.ResponseBodyCreator()

    def test_added(self):
        dummy = {'id': 1, 'name': 'test'}
        body = self.__res.added(dummy)
        self.assertEqual(res.CREATED, body['status_code'])
        self.assertEquals(dummy['id'], body['id'])

    def test_add_failed(self):
        errors = [
            {'name': 'name is required'},
            {'age': 'age greator than or equal to 0'}
        ]
        body = self.__res.add_failed(errors)
        self.assertEquals(len(errors), len(body['errors']))


if __name__ == '__main__':
    unittest.main()
