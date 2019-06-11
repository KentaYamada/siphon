from datetime import datetime, timedelta
from app.model.base import BaseModel


class Token(BaseModel):
    def __init__(self, user_id=None, token='', **kwargs):
        super().__init__()
        self.user_id = user_id
        self.token = token
        self.expired = (datetime.now() + timedelta(days=7)).date()

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        super()._clear_validation_error('user_id')
        if value is None:
            super()._add_validation_error('user_id', 'ユーザーIDは必須です')
        if not isinstance(value, int):
            super()._add_validation_error('user_id', 'ユーザーIDは整数をセットしてください')
        else:
            self.__user_id = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        super()._clear_validation_error('token')
        if not value:
            super()._add_validation_error('token', 'トークンは必須入力です')
        elif not isinstance(value, str):
            super()._add_validation_error('token', 'トークンのデータ型文字列です')
        else:
            self.__token = value
