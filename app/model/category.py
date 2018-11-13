from app.model.base import BaseModel


class Category(BaseModel):
    MAX_ADDABLE_DATA = 10

    def __init__(self, id=None, name=''):
        super().__init__()
        self.id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        super()._clear_validation_error('id')
        if value is not None and not isinstance(value, int):
            super()._add_validation_error('id', 'IDには整数をセットしてください')
        else:
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        super()._clear_validation_error('name')
        if not value:
            super()._add_validation_error('name', 'ユーザー名は必須入力です')
        else:
            self.__name = value

    def is_valid(self):
        if not super().is_valid():
            return False

        saved_rows = Category.db.fetch_rowcount('categories')
        if self.MAX_ADDABLE_DATA <= saved_rows:
            super()._add_validation_error('maximum_row', '商品カテゴリの登録上限を超えています')
            return False
        return True

    def save(self):
        if not self.is_valid():
            return False
        saved = False
        try:
            affected = Category.db.execute_proc('save_category', (self.id, self.name))
            saved = True if affected == 1 else False
            if saved:
                Category.db.commit()
            else:
                Category.db.rollback()
        except Exception as e:
            Category.db.rollback()
            print(e)
            raise e
        return saved

    def delete(self):
        if self.id is None:
            return False
        deleted = False
        try:
            affected = Category.db.execute_proc('delete_category', (self.id,))
            deleted = True if affected == 1 else False
            if deleted:
                Category.db.commit()
            else:
                Category.db.rollback()
        except Exception as e:
            Category.db.rollback()
            print(e)
            raise e
        return deleted

    @classmethod
    def find_all(cls):
        categories = []
        try:
            rows = Category.db.find('find_categories')
            if len(rows) > 0:
                categories = [
                    {'id': row['id'], 'name': row['name']} for row in rows]
        except Exception as e:
            print(e)
            raise e
        return categories
