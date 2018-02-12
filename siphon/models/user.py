# -*- coding: utf-8 -*-
import hashlib

class User():
    def __init__(self, email, password, *args, **kwargs):
        self.__email = email
        self.__password = password

    def __toHash(self, text):
        return hashlib.md5(password.encode("utf-8")).hexdigest()

    def save(self):
        self.__password = self.__toHash(self.__password.encode("utf-8"))
        return True

    def authentication(self):
        self.__password = self.__toHash(self.__password.encode("utf-8"))
        return True

    @classmethod
    def find_users_by(cls):
        return [{'id': i, 'name': 'User{0}'.format(i), 'email': 'hoge@email.com', 'password': '****'} for i in range(1, 11)]
