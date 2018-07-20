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
        """
            attach database and create session
        """
        if self.__config is None:
            raise ValueError()
        if self.__con is None or self.__con.closed:
            self.__con = psycopg2.connect(**self.__config)
        self.__cur = self.__con.cursor(cursor_factory=psycopg2.extras.DictCursor)


    def save(self, command, data):
        """
            run save or change procedure
        """
        if not command or data is None:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, data)

    def remove(self, command, data=None):
        """
            run remove procedure
        """
        self.save(command, data)

    def find(self, command, condition=None):
        """
            run find rows procedure
        """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, condition)
        return self.__cur.fetchall()

    def find_one(self, command, condition):
        """
            run find row procedure
        """
        if not command:
            raise ValueError()
        self.__create_cursor()
        self.__cur.callproc(command, condition)
        return self.__cur.fetchone()

    def execute(self, query, data=None):
        """
            run sql command
        """
        if not query:
            raise ValueError()
        self.__create_cursor()
        self.__cur.execute(query, data)

    def fetch_rowcount(self, tablename):
        """
            fetch row count by specific table
        """
        if not tablename:
            raise ValueError()
        query = 'SELECT COUNT(id) AS rowcount FROM {0};'.format(tablename)
        self.__create_cursor()
        self.__cur.execute(query)
        return self.__cur.fetchone()['rowcount']

    def fetch_last_row_id(self):
        """
            fetch last row id
        """
        self.__create_cursor()
        self.__cur.execute('SELECT LASTVAL();')
        return self.__cur.fetchone()['lastval']

    def bulk_insert(self, query, values):
        """
            run bulk insert values 
        """
        if not query:
            raise ValueError()
        if values is None or len(values) < 1:
            raise ValueError()
        self.__create_cursor()
        self.__cur.executemany(query, values)
        return len(values) == self.__cur.rowcount

    def commit(self):
        """
            commit transaction
        """
        if self.__con is not None and not self.__con.closed:
            self.__con.commit()
            self.__cur.close()
            self.__con.close()
            self.__con = None

    def rollback(self):
        """
            rollback transaction
        """
        if self.__con is not None and not self.__con.closed:
            self.__con.rollback()
            self.__cur.close()
            self.__con.close()
            self.__con = None
