# -*- coding: utf-8 -*-
#
# Siphon
# pypg.py
# This program wrapped psycopg2.
#
# import logging
import psycopg2
import psycopg2.extensions
import psycopg2.extras


class Pypg():
    def __init__(self, dsn=''):
        # Todo: dsn set config from config
        self.__con = None
        self.__cur = None
        self.__dsn = dsn

    def __execute(self, query, args):
        if not query:
            raise ValueError("query must be set value")
        if args is None:
            raise ValueError("args must be set value")
        self.__con = psycopg2.connect(self.__dsn)
        self.__cur = self.__con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.__cur.execute(query, args)

    def detatch(self):
        if self.__con is None:
            self.__con.close()
