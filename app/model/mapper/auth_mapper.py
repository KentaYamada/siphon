from datetime import datetime
from app.model.token import Token
from app.model.mapper.base_mapper import BaseMapper


class AuthMapper(BaseMapper):
    def find_logged_in_user(self, token):
        if token is None or not isinstance(token, Token):
            raise ValueError()
        try:
            user = self._db.find_one_proc('find_logged_in_user', (token,))
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            user = None
            print(e)
        return user

    def save_token(self, token):
        if token is None or not isinstance(token, Token):
            raise ValueError()
        data = (
            token.user_id,
            token.token,
            token.expired
        )
        try:
            self._db.execute_proc('save_token', data)
            self._db.commit()
            saved = True
        except Exception as e:
            print(e)
            self._db.rollback()
            saved = False
        return saved

    def dispose_token(self, token):
        if not token or not isinstance(token, str):
            raise ValueError('Invalid argument')
        try:
            self._db.execute_proc('dispose_token', (token,))
            self._db.commit()
            disposed = True
        except Exception as e:
            self._db.rollback()
            disposed = False
            print(e)
        return disposed
