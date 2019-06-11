from app.model.token import Token
from app.model.mapper.base_mapper import BaseMapper


class AuthMapper(BaseMapper):
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

    def delete_token(self, user_id):
        if user_id is None or not isinstance(user_id, int):
            raise ValueError()
        if user_id <= 0:
            raise ValueError('Invalid value')
        try:
            self._db.execute_proc('delete_token', (user_id,))
            self._db.commit()
            deleted = True
        except Exception as e:
            self._db.rollback()
            deleted = False
        return deleted

