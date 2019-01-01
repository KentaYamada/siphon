from app.model.base import BaseModel


class Category(BaseModel):
    def __init__(self, id=None, name='', **kwargs):
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
        else:
            return True

    @classmethod
    def find_all(cls):
        categories = []
        try:
            rows = Category.db.find('find_categories')
            Category.db.commit()
            if len(rows) > 0:
                categories = [
                    {'id': row['id'], 'name': row['name']} for row in rows]
        except Exception as e:
            print(e)
            raise e
        return categories
