class Item():
    def __init__(self, id, category_id, name, unit_price):
        self.__id = id
        self.__category_id = category_id
        self.__name = name
        self.unit_price = unit_price

    @classmethod
    def find_by(cls, category_id):
        return [{
            'id': i,
            'category_id': category_id,
            'name': 'Item{}'.format(i),
            'unit_price': i * 100
        } for i in range(1, 11)]
