from app.model.item import Item
from app.model.mapper.base_mapper import BaseMapper


class ItemMapper(BaseMapper):
    MAX_ADDABLE_DATA = 30

    def __init__(self):
        super().__init__()

    def add(self, item):
        if item is None:
            raise ValueError()
        if not isinstance(item, Item):
            raise ValueError()
        query = """
            INSERT INTO items (
                category_id,
                name,
                unit_price
            ) VALUES (
                %s,
                %s,
                %s
            );
        """
        data = (
            item.category_id,
            item.name,
            item.unit_price
        )
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

    def edit(self, item):
        if item is None:
            raise ValueError()
        if not isinstance(item, Item):
            raise ValueError()
        query = """
            UPDATE items SET
                category_id = %s,
                name = %s,
                unit_price = %s
            WHERE id = %s;
        """
        data = (
            item.category_id,
            item.name,
            item.unit_price,
            item.id
        )
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
        query = 'DELETE FROM items WHERE id = %s;'
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

    def find_by_category_id(self, category_id):
        if category_id is None:
            raise ValueError()
        if not isinstance(category_id, int):
            raise ValueError()
        query = """
            SELECT
                id,
                category_id,
                name,
                unit_price
            FROM items
            WHERE category_id = %s
            ORDER BY id ASC;
        """
        rows = None
        try:
            rows = self._db.find(query)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        return rows
