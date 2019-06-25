from app.model.token import Token
from app.model.mapper.base_mapper import BaseMapper


class AuthMapper(BaseMapper):
    def find_logged_in_user(self, token):
        if token is None or not isinstance(token, str):
            raise ValueError()
        try:
            user = self._db.find_one_proc('find_logged_in_user', (token,))
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            user = None
            print(e)
        return user

    def find_logged_in_user_token(self, user_id):
        if user_id is None or not isinstance(user_id, int):
            raise ValueError()
        try:
            row = self._db.find_one_proc(
                'find_logged_in_user_token',
                (user_id,)
            )
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            row = None
        return row['token'] if row is not None else ''

    def get_is_blacklist(self, token):
        if token is None or not isinstance(token, str):
            raise ValueError()
        is_blacklist = False
        try:
            row = self._db.find_one_proc('find_blacklist', (token,))
            self._db.commit()
            is_blacklist = True if row['hits'] > 0 else False
        except Exception as e:
            self._db.rollback()
            raise e
        return is_blacklist

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
