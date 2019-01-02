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

    def find_by(self, condition):
        users = []
        for i in range(1, 31):
            user = User(
                i,
                'User{0}'.format(i),
                'Nickname{0}'.format(i),
                'test{0}@email.com'.format(i),
                'hoge{0}fuga'.format(i)
            )
            users.append(user)
        return users

    def authoricate(self, email, password, **kwargs):
        # dummy
        if not email or not password:
            return False
        if email != 'test' and password != 'test':
            return False
        return True
        # if user is None or not isinstance(user, User):
        #     raise ValueError()
        # query = """
        #     SELECT
        #         COUNT(id) AS logged_in
        #     FROM users
        #     WHERE email = %s
        #       AND password = %s;
        # """
        # data = (user.email, user.password)
        # user = None
        # try:
        #     user = self._db.find_one(query, data)
        #     self._db.commit()
        # except Exception as e:
        #     self._db.rollback()
        #     print(e)
        # return user
