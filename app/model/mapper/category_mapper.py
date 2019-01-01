from app.model.category import Category
from app.model.mapper.base_mapper import BaseMapper


class CategoryMapper(BaseMapper):
    MAX_ADDABLE_ROW = 10

    def __init__(self):
        super().__init__()

    def add(self, category):
        if category is None:
            raise ValueError()
        if not isinstance(category, Category):
            raise ValueError()
        query = """
            INSERT INTO categories (
                name
            ) VALUES (
                %s
            );
        """
        data = (category.name,)
        saved = False
        try:
            self._db.execute(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def edit(self, category):
        if category is None:
            raise ValueError()
        if not isinstance(category, Category):
            raise ValueError()
        query = """
            UPDATE categories SET
                name = %s
            WHERE id = %s;
        """
        data = (category.name, category.id)
        try:
            self._db.execute(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def delete(self, id):
        if id is None:
            raise ValueError()
        if not isinstance(id, int):
            raise ValueError()
        if id <= 0:
            raise ValueError('Invalid id')
        query = """
            DELETE FROM categories WHERE id = %s
        """
        data = (id,)
        try:
            self._db.execute(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def find_all(self):
        query = """
            SELECT
                id,
                name
            FROM categories
            ORDER BY id;
        """
        rows = None
        try:
            rows = self._db.find(query)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        return rows

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
