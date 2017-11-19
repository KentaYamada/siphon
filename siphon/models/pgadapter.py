# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras


class PgAdapter():
    def __init__(self, dsn):
        self.__con = None
        self.__dsn = dsn

    def __build_find_command(self, query):
        return "SELECT * FROM {0};".format(query)

    def __build_exec_command(self, query):
        return "SELECT {0};".format(query)

    def __exec(self, query, args):
        self.__con = psycopg2.connect(self.__dsn)
        cur = self.__con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute(query, args)
        print(cur.query)
        return cur

    @property
    def connected(self):
        return True if self.__con.closed < 1 else False

    def execute_script(self, query):
        self.__exec(cmd, None)

    def save(self, query, args):
        cmd = self.__build_exec_command(query)
        cur = self.__exec(cmd, args)
        return True if cur.rowcount > 0 else False

    def remove(self, query, args):
        return self.save(query, args)

    def find(self, query, args=None):
        rows = None
        cmd = self.__build_find_command(query)
        try:
            cur = self.__exec(cmd, args)
            rows = [row for row in cur.fetchall()]
        finally:
            self.__con.close()
        return rows

    def find_one(self, query, args):
        row = None
        cmd = self.__build_find_command(query)
        try:
            cur = self.__exec(cmd, args)
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
