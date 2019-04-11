from app.model.category import Category, CategorySearchOption
from app.model.mapper.base_mapper import BaseMapper


class CategoryMapper(BaseMapper):
    MAX_ADDABLE_ROW = 10

    def __init__(self):
        super().__init__()

    def save(self, category):
        if category is None or not isinstance(category, Category):
            raise ValueError()
        try:
            data = (category.id, category.name)
            self._db.execute_proc('save_category', data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def find(self, option):
        if option is None or not isinstance(option, CategorySearchOption):
            raise ValueError()
        try:
            rows = self._db.find_proc('find_categories', (option.q,))
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        field_list = ['id', 'name']
        categories = [{f: row[f] for f in field_list} for row in rows]
        return categories

    def delete(self, id):
        if id is None:
            raise ValueError()
        if not isinstance(id, int) or id <= 0:
            raise ValueError()
        try:
            self._db.execute_proc('delete_category', (id,))
            self._db.commit()
            deleted = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            deleted = False
        return deleted

    def is_upper_limit(self):
        row_count = 0
        try:
            row_count = self._db.fetch_rowcount('categories')
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        if row_count <= self.MAX_ADDABLE_ROW:
            return True
        else:
            return False
