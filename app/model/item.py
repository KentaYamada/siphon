from app.model.base import BaseModel


class Item(BaseModel):
    def __init__(self, id=None, category_id=None,
                 name='', unit_price=0, **kwargs):
        super().__init__()
        self.id = id
        self.category_id = category_id
        self.name = name
        self.unit_price = unit_price

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
    def category_id(self):
        return self.__category_id

    @category_id.setter
    def category_id(self, value):
        super()._clear_validation_error('category_id')
        if value is None:
            super()._add_validation_error(
                'category_id',
                '商品カテゴリIDは必須入力です'
            )
        if value is not None and not isinstance(value, int):
            super()._add_validation_error(
                'category_id',
                '商品カテゴリIDには整数をセットしてください'
            )
        else:
            self.__category_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        super()._clear_validation_error('name')
        if not value:
            super()._add_validation_error('name', '商品名は必須入力です')
        else:
            self.__name = value

    @property
    def unit_price(self):
        return self.__unit_price

    @unit_price.setter
    def unit_price(self, value):
        super()._clear_validation_error('unit_price')
        if value is None:
            super()._add_validation_error(
                'unit_price',
                '単価は必須入力です'
            )
        elif value is not None and not isinstance(value, int):
            super()._add_validation_error(
                'unit_price',
                '単価には整数をセットしてください'
            )
        elif value <= 0:
            super()._add_validation_error(
                'unit_price',
                '単価には0以上をセットしてください'
            )
        else:
            self.__unit_price = value

    @classmethod
    def find_by(cls, category_id):
        return [{
            'id': i,
            'category_id': category_id,
            'name': 'Item{}'.format(i),
            'unit_price': i * 100
        } for i in range(1, 11)]
