from app.model.user import User, UserSearchOption
from app.model.mapper.base_mapper import BaseMapper


class UserMapper(BaseMapper):
    def save(self, user):
        if user is None or not isinstance(user, User):
            raise ValueError()
        try:
            data = (
                user.id,
                user.name,
                user.nickname,
                user.email,
                user.password
            )
            self._db.execute_proc('save_user', data)
            self._db.commit()
            saved = True
        except Exception as e:
            # todo logging
            print(e)
            self._db.rollback()
            saved = False
        return saved

    def delete(self, id):
        if id is None or not isinstance(id, int):
            raise ValueError()
        if id <= 0:
            raise ValueError('Invalid id')
        try:
            self._db.execute_proc('delete_user', (id,))
            self._db.commit()
            deleted = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            deleted = False
        return deleted

    def find(self, option):
        if option is None or not isinstance(option, UserSearchOption):
            raise ValueError()
        data = (option.q,)
        rows = []
        try:
            rows = self._db.find_proc('find_users_by', data)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        fields = ['id', 'name', 'nickname']
        users = self.format_rows(rows, fields)
        return users

    def find_auth_user(self, user):
        if user is None or not isinstance(user, User):
            raise ValueError()
        data = (user.email,)
        row = None
        try:
            row = self._db.find_one_proc('find_auth_user', data)
            self._db.commit()
        except Exception as e:
            # todo: logging
            print(e)
            self._db.rollback()
        fields = ['id', 'name', 'nickname', 'email', 'password']
        return self.format_row(row, fields) if row is not None else None
