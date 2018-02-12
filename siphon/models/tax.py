# -*- coding: utf-8 -*-

import psycopg2
from siphon.models.pgadapter import PgAdapter

class Tax(PgAdapter):
    def __init__(self, rate=1, tax_type='out', *args, **kwargs):
        self.rate = rate
        self.tax_type = tax_type

    def validate(self):
        return True if 1 < self.rate < 100 else False

    def save(self):
        if not self.validate():
            return False
        saved = False
        try:
            saved = self.save('save_tax(%s, %s)', (self.rate, self.tax_type))
            if saved:
                self.commit()
            else:
                self.rollback()
        except Exception as e:
            self.rollback()
        return saved

    @classmethod
    def find_tax(cls):
        return Tax().find('find_tax()')
