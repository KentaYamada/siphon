import unittest
from datetime import datetime
from app.model.tax_rate import TaxRate


class TestTaxRate(unittest.TestCase):
    def setUp(self):
        self.model = TaxRate(10, 8, datetime.now().date(), 1)

    def tearDown(self):
        self.model = None

    def test_rate_is_none_value(self):
        self.model.rate = None
        self.assertFalse(self.model.is_valid())
        self.assertTrue('rate' in self.model.validation_errors)

    def test_rate_is_invalid_type(self):
        invalid_values = ['', '1', []]
        for value in invalid_values:
            self.model.rate = value
            self.assertFalse(self.model.is_valid())
            self.assertTrue('rate' in self.model.validation_errors)

    def test_verify_rate_range(self):
        self.model.rate = 0
        self.assertFalse(self.model.is_valid())
        self.assertTrue('rate' in self.model.validation_errors)
        self.model.rate = 1
        self.assertTrue(self.model.is_valid())

    def test_reduced_rate_is_none_value(self):
        self.model.reduced_rate = None
        self.assertFalse(self.model.is_valid())
        self.assertTrue('reduced_rate' in self.model.validation_errors)

    def test_reduced_rate_is_invalid_type(self):
        invalid_values = ['', '1', []]
        for value in invalid_values:
            self.model.reduced_rate = value
            self.assertFalse(self.model.is_valid())
            self.assertTrue('reduced_rate' in self.model.validation_errors)

    def test_verify_reduced_rate_range(self):
        self.model.reduced_rate = 0
        self.assertFalse(self.model.is_valid())
        self.assertTrue('reduced_rate' in self.model.validation_errors)
        self.model.reduced_rate = 1
        self.assertTrue(self.model.is_valid())

    def test_tax_type_is_none_value(self):
        self.model.tax_type = None
        self.assertFalse(self.model.is_valid())
        self.assertTrue('tax_type' in self.model.validation_errors)

    def test_tax_type_is_invalid_type(self):
        invalid_values = ['', '1', []]
        for value in invalid_values:
            self.model.tax_type = value
            self.assertFalse(self.model.is_valid())
            self.assertTrue('tax_type' in self.model.validation_errors)

    def test_verify_tax_type(self):
        self.model.tax_type = 1
        self.assertTrue(self.model.is_valid())
        self.model.tax_type = 2
        self.assertTrue(self.model.is_valid())
        self.model.tax_type = 3
        self.assertFalse(self.model.is_valid())
        self.assertTrue('tax_type' in self.model.validation_errors)
