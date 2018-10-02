class Category():
    def __init__(self, id=None, name=''):
        self.__id = id
        self.__name = name
        self.__errors = []

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # ToDo: decorator化
        isValid = True
        if not self.__name:
            self.__set_error('name', '商品カテゴリ名は必須です')
            isValid = False
        return isValid

    def save(self):
        if not self.validate():
            return False
        return True

    def delete(self):
        if self.__id is None:
            return False
        return True

    @classmethod
    def find_all(cls):
        return [
            {'id': i, 'name': 'Category{}'.format(i)}
            for i in range(1, 10)]

    def __set_error(self, field, message):
        self.__errors.append({'name': field, 'message': message})
