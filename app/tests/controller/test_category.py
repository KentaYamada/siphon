import json
import unittest
from urllib.parse import urljoin, urlencode
from app import startup_app
from app.model.pgadapter import PgAdapter


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/categories/'


class TestCategoryApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    def tearDown(self):
        query = """
            TRUNCATE TABLE categories
            RESTART IDENTITY;
        """
        db = PgAdapter()
        db.execute(query)
        db.commit()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_index(self):
        self.__init_data()
        res = TestCategoryApi.client.get(
            END_POINT,
            content_type=CONTENT_TYPE)
        body = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertEquals(10, len(body['categories']))

    def test_index_keyword_search(self):
        self.__init_data()
        query_string = urlencode({'q': 'セット'})
        #todo: strict_slashes = false
        url = '/api/categories?{0}'.format(query_string)
        res = TestCategoryApi.client.get(
            url,
            content_type=CONTENT_TYPE)
        body = json.loads(res.data)
        self.assertEqual(200, res.status_code)
        self.assertEqual(2, len(body['categories']))

    def test_index_with_items(self):
        data = json.dumps({'with_items': True})
        res = TestCategoryApi.client.get(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_add_ok(self):
        data = json.dumps({
            'id': None,
            'name': 'Test'})
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(201, res.status_code)

    def test_add_ng_when_no_data(self):
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE)
        self.assertEqual(400, res.status_code)

    def test_add_ng_when_invalid_data(self):
        data = json.dumps({
            'id': None,
            'name': ''})
        res = TestCategoryApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(400, res.status_code)

    def test_edit_ok(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': 'Test Category'
        })
        res = TestCategoryApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(200, res.status_code)

    def test_edit_ng(self):
        url = urljoin(END_POINT, '1')
        data = json.dumps({
            'name': ''
        })
        res = TestCategoryApi.client.put(
            url,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(400, res.status_code)

    def test_delete_ok(self):
        url = urljoin(END_POINT, '1')
        res = TestCategoryApi.client.delete(url)
        self.assertEqual(204, res.status_code)

    def test_delete_ng(self):
        res = TestCategoryApi.client.delete(END_POINT)
        self.assertEqual(405, res.status_code)

    def __init_data(self):
        db = PgAdapter()
        db.execute_proc('create_test_data_categories')
        db.commit()
