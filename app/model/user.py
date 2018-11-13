from app.model.pgadapter import PgAdapter
from app.config import get_db_config

class User:
    db = PgAdapter(get_db_config('develop'))

    def __init__(self, id=None, name='', nickname='', email='', password=''):
        self.__errors = {}
        self.id = id
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__clear_validation_error('id')
        if value is not None and not isinstance(value, int):
            self.__add_validation_error('id', 'IDには整数をセットしてください')
        else:
            self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__clear_validation_error('name')
        if not value:
            self.__add_validation_error('name', 'ユーザー名は必須入力です')
        else:
            self.__name = value

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self, value):
        self.__nickname = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__clear_validation_error('email')
        if not value:
            self.__add_validation_error('email', 'メールアドレスは必須入力です')
        else:
            self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__clear_validation_error('password')
        if not value:
            self.__add_validation_error('password', 'パスワードは必須入力です')
        else:
            self.__password = value

    @property
    def validation_errors(self):
        return self.__errors

    def save(self):
        if not self.is_valid():
            return False
        saved = False
        try:
            affected = User.db.execute_proc('save_user', (self.id, self.name, self.nickname, self.email, self.password))
            saved = True if affected == 1 else False
            if saved:
                User.db.commit()
            else:
                User.db.rollback()
        except Exception as e:
            User.db.rollback()
            print(e)
            raise e
        return saved

    def delete(self):
        if self.id is None:
            return False
        return True

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

    def is_valid(self):
        return True if not self.__errors else False

    def __clear_validation_error(self, field):
        if field in self.__errors.keys():
            del self.__errors[field]

    def __add_validation_error(self, field, message):
        if field in self.__errors.keys():
            self.__errors[field].append(message)
        else:
            self.__errors[field] = [message]
