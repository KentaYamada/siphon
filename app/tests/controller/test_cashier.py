import json
import unittest
# from urllib.parse import urljoin
from app import startup_app


# constant
CONTENT_TYPE = 'application/json'
END_POINT = '/api/cashier/'


class TestCashierApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app = startup_app()
        cls.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.client = None

    def test_add_success(self):
        data = json.dumps({
            'total_price': 1000,
            'discount_price': 0,
            'discount_rate': 0,
            'inclusive_tax': 0,
            'exclusive_tax': 0,
            'deposit': 1000,
            'items': [
                {
                    'item_name': 'Item A',
                    'unit_price': 500,
                    'quantity': 2,
                    'subtotal': 1000
                }
            ]})
        res = TestCashierApi.client.post(
            END_POINT,
            content_type=CONTENT_TYPE,
            data=data)
        self.assertEqual(201, res.status_code)
