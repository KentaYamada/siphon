from app.model.item import Item, ItemSearchOption
from app.model.mapper.base_mapper import BaseMapper


class ItemMapper(BaseMapper):
    MAX_ADDABLE_DATA = 30

    def __init__(self):
        super().__init__()

    def save(self, item):
        if item is None or not isinstance(item, Item):
            raise ValueError()
        try:
            data = (
                item.id,
                item.category_id,
                item.name,
                item.unit_price
            )
            self._db.execute_proc('save_item', data)
            self._db.commit()
            saved = True
        except Exception as e:
            print(e)
            self._db.rollback()
            saved = False
        return saved

    def delete(self, id):
        if id is None:
            raise ValueError()
        if not isinstance(id, int) or id <= 0:
            raise ValueError()
        has_row = self._db.has_row('items', id)
        if not has_row:
            return False
        try:
            self._db.execute_proc('delete_item', (id,))
            self._db.commit()
            deleted = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            deleted = False
        return deleted

    def find(self, option):
        if option is None or not isinstance(option, ItemSearchOption):
            raise ValueError()
        data = (option.category_id, option.q)
        rows = []
        try:
            rows = self._db.find_proc('find_items', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        fields = ['id', 'category_id', 'name', 'unit_price']
        items = self.format_rows(rows, fields)
        return items

    def find_by_category_ids(self, option):
        if option is None or not isinstance(option, ItemSearchOption):
            raise ValueError()
        if option.category_ids is None:
            raise ValueError()
        if len(option.category_ids) < 1:
            return []
        data = (option.category_ids,)
        rows = []
        try:
            rows = self._db.find_proc('find_items_by_category_ids', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
        field_list = ['id', 'category_id', 'name', 'unit_price']
        items = self.format_rows(rows, field_list)
        return items
