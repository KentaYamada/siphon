# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras


class PgAdapter():
    def __init__(self, dsn):
        self.__con = None
        self.__dsn = dsn

    def __exec(self, query, args):
        self.__con = psycopg2.connect(self.__dsn)
        cur = self.__con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.callproc(query, args)
        return cur

    @property
    def connected(self):
        return True if self.__con.closed < 1 else False

    def execute_script(self, query):
        pass

    def save(self, query, args):
        cur = self.__exec(query, args)
        print(cur.query)
        return True if cur.rowcount > 0 else False

    def remove(self, query, args):
        cur = self.__exec(query, args)
        print(cur.query)
        return True if cur.rowcount > 0 else False

    def find(self, query, args=None):
        rows = None
        try:
            cur = self.__exec(query, args)
            print(cur.query)
            rows = [row for row in cur.fetchall()]
        finally:
            self.__con.close()
        return rows

    def find_one(self, query, args):
        row = None
        try:
            cur = self.__exec(query, args)
            print(cur.query)
            row = cur.fetchone()
        finally:
            self.__con.close()
        return row

    def commit(self):
        if self.__con is not None:
            self.__con.commit()
            self.__con.close()

    def rollback(self):
        if self.__con is not None:
            self.__con.rollback()
            self.__con.close()

    @classmethod
    def read_sqlfile(cls, filename):
        pass

