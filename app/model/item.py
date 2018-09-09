class Item():
    def __init__(self, id=None, category_id=None, name='', unit_price=0):
        self.__id = id
        self.__category_id = category_id
        self.__name = name
        self.__unit_price = unit_price
        self.__errors = []

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # ToDo: decorator化
        isValid = True
        if self.__category_id is None:
            isValid = False
            self.__set_error('category_id', '商品カテゴリIDは必須です')
        if not self.__name:
            isValid = False
            self.__set_error('name', '商品名は必須です')
        if self.__unit_price is None:
            isValid = False
            self.__set_error('unit_price', '単価は必須です')
        elif self.__unit_price <= 0:
            isValid = False
            self.__set_error('unit_price', '単価は1円以上設定してください')
        return isValid

    def save(self):
        if not self.validate():
            return False
        return True

    def delete(self):
        if self.__id is None:
            return False
        return True

    def __set_error(self, field, message):
        self.__errors.append({'name': field, 'message': message})

    @classmethod
    def find_by(cls, category_id):
        return [{
            'id': i,
            'category_id': category_id,
            'name': 'Item{}'.format(i),
            'unit_price': i * 100
        } for i in range(1, 11)]
