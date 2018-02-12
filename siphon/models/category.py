# -*- coding: utf-8 -*-

from siphon.models.pgadapter import PgAdapter

class Category(PgAdapter):
    def __init__(self, id=None, name='', *args, **kwargs):
        self.id = id
        self.name = name

    @property
    def error(self):
        return self.__error

    def __validate(self):
        if not self.name:
            return False
        return True

    def save(self):
        if not self.__validate():
            return False

        saved = True
        try:
            saved = super().save("save_category(%s, %s)", (self.id, self.name))
            if saved:
                super().commit()
            else:
                super().rollback()
        except:
            super().rollback()
        return saved

    @classmethod
    def find_all_categories(cls):
        return [{'id': i, 'name': 'Category{0}'.format(i)} for i in range(1, 11)]
