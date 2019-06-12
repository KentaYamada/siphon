from werkzeug.security import generate_password_hash, check_password_hash
from app.model.base import BaseModel


class User(BaseModel):
    def __init__(self, id=None, name='', nickname='',
                 email='', password='', **kwargs):
        super().__init__()
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
        super()._clear_validation_error('email')
        if not value:
            super()._add_validation_error('email', 'メールアドレスは必須入力です')
        else:
            self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        super()._clear_validation_error('password')
        if not value:
            super()._add_validation_error('password', 'パスワードは必須入力です')
        else:
            self.__password = generate_password_hash(value)

    @classmethod
    def verify_password(cls, request_password, user_password):
        return check_password_hash(user_password, request_password)


class UserSearchOption:
    def __init__(self, q='', **kwargs):
        self.q = q
