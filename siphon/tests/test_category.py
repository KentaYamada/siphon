# -*- coding: utf-8 -*-

import unittest
from siphon.models.category import Category

class TestCategory(unittest.TestCase):
    # def test_save_name_is_empty(self):
    #     model = Category(None, '')
    #     saved = model.save()
    #     error = Category.error()
    #     self.assertEqual(False, saved)
    #     self.assertEqual('name', error['field'])

    #     model.name = None
    #     saved = model.save()
    #     error = Category.error()
    #     self.assertEqual(False, saved)
    #     self.assertEqual('name', error['field'])

    def test_save_ok(self):
        model = Category(None, 'Morning')
        saved = model.save()
        self.assertEqual(True, saved)
