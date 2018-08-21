

class Category():
    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name

    def find_all(self):
        return [{'id': i, 'name': 'Test{}'.format(i)} for i in range(1, 11)]

    def save(self):
        return True
