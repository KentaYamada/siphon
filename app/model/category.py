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
            super()._add_validation_error('name', 'カテゴリ名は必須入力です')
        else:
            self.__name = value


class CategorySearchOption:
    def __init__(self, q='', with_items=False, **kwargs):
        self.q = q
        self.with_items = with_items
