

class User():
    def __init__(self, id, name='', nickname='', email='', password=''):
        self.__id = id
        self.__name = name
        self.__nickname = nickname
        self.__email = email
        self.__password = password
        self.__errors = []

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # ToDo: decorator化
        isValid = True
        if not self.__name:
            isValid = False
            self.__set_error('name', 'ユーザー名は必須です')
        if not self.__email:
            isValid = False
            self.__set_error('name', 'EMailは必須です')
        if not self.__password:
            isValid = False
            self.__set_error('name', 'パスワードは必須です')
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
    def authoricate(self, user_id, password):
        return True if user_id == 'test' and password == 'test' else False

    @classmethod
    def find_by(cls, keyword):
        users = []
        for i in range(1, 11):
            users.append({
                'id': i,
                'name': 'User {}'.format(i),
                'nickname': 'User nickname {}'.format(i),
                'email': 'user{}@email.com'.format(i),
                'password': 'test'
            })
        return users
