"""
    pgadapter.py
    PostgreSQL connection helper class.
    Author: Kenta Yamada
"""
import psycopg2
import psycopg2.extras


class PgAdapter():
    def __init__(self, config):
        self.__config = config
        self.__con = None
        self.__cur = None

    def __create_cursor(self):
        """ attach database and create cursor """
        if self.__config is None:
            raise ValueError()
        if self.__con is None or self.__con.closed:
            self.__con = psycopg2.connect(**self.__config)
        if self.__cur is None or self.__cur.closed:
            self.__cur = self.__con.cursor(
                cursor_factory=psycopg2.extras.DictCursor)

    def execute(self, command, data=None):
        """ execute plain sql query """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.execute(command, data)
        return self.__cur.rowcount

    def execute_proc(self, command, data=None):
        """ execute stored procedure """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, data)
        return self.__cur.rowcount

    def find(self, command, condition=None):
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.execute(command, condition)
        return self.__cur.fetchall()

    def find_one(self, command, condition):
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.execute(command, condition)
        return self.__cur.fetchone()

    def find_proc(self, command, condition=None):
        """ execute find rows procedure """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, condition)
        return self.__cur.fetchall()

    def find_one_proc(self, command, condition):
        """ execute find row procedure """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, condition)
        return self.__cur.fetchone()

    def fetch_rowcount(self, tablename):
        """ fetch row count by specific table """
        if not tablename:
            raise ValueError()
        query = 'SELECT COUNT(id) AS rowcount FROM {0};'.format(tablename)
        self.__create_cursor()
        self.__cur.execute(query)
        return self.__cur.fetchone()['rowcount']

    def fetch_last_row_id(self):
        """ fetch last row id """
        self.__create_cursor()
        self.__cur.execute('SELECT LASTVAL();')
        return self.__cur.fetchone()['lastval']

    def bulk_insert(self, query, values):
        """ run bulk insert values """
        if not query:
            raise ValueError()
        if values is None or len(values) < 1:
            raise ValueError()
        self.__create_cursor()
        self.__cur.executemany(query, values)
        return self.__cur.rowcount

    def commit(self):
        """ commit transaction """
        if self.__con is not None and not self.__con.closed:
            self.__con.commit()
            self.__cur.close()
            self.__con.close()

    def rollback(self):
        """ rollback transaction """
        if self.__con is not None and not self.__con.closed:
            self.__con.rollback()
            self.__cur.close()
            self.__con.close()
