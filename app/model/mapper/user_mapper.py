from app.model.user import User
from app.model.mapper.base_mapper import BaseMapper


class UserMapper(BaseMapper):
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

    def find_by(self, user):
        if user is not None and not isinstance(user, User):
            raise ValueError()
        query = """
            SELECT
                id,
                name,
                nickname,
                email,
                password
            FROM users
            ORDER BY id ASC;
        """
        users = None
        try:
            users = self._db.find(query)
            self._db.commit()
        except Exception as e:
            self._db.rollback()
            print(e)
            users = None
        return users
