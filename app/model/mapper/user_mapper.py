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

    def add(self, user):
        if user is None:
            raise ValueError()
        if not isinstance(user, User):
            raise ValueError()
        query = """
            INSERT INTO users (
                name,
                nickname,
                email,
                password
            ) VALUES (
                %s,
                %s,
                %s,
                %s
            );
        """
        data = (
            user.name,
            user.nickname,
            user.email,
            user.password
        )
        saved = False
        try:
            self._db.execute(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def edit(self, user):
        if user is None:
            raise ValueError()
        if not isinstance(user, User):
            raise ValueError()
        query = """
            UPDATE users SET
                name = %s,
                nickname = %s,
                email = %s,
                password = %s
            WHERE id = %s;
        """
        data = (
            user.name,
            user.nickname,
            user.email,
            user.password,
            user.id
        )
        try:
            self._db.execute(query, data)
            self._db.commit()
            saved = True
        except Exception as e:
            self._db.rollback()
            # todo: logging
            print(e)
            saved = False
        return saved

    def delete(self, id):
        if id is None or not isinstance(id, int):
            raise ValueError()
        if id <= 0:
            raise ValueError('Invalid id')
        query = 'DELETE FROM users WHERE id = %s;'
        try:
            self._db.execute(query, (id,))
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
        try:
            rows = self._db.find_proc('find_users_by', (option.q,))
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
        field_list = ['id', 'name', 'nickname']
        users = [{f: row[f] for f in field_list} for row in rows]
        return users
