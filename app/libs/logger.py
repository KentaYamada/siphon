import logging
from app.config import (
    DEBUG_LOG_KEY,
    ERROR_LOG_KEY,
    SQL_LOG_KEY
)


class Logger:
    sql_logger = None
    debug_logger = None
    error_logger = None

    @classmethod
    def print_debug(cls, data):
        if data is None:
            raise ValueError()
        if cls.debug_logger is None:
            cls.debug_logger = logging.getLogger(DEBUG_LOG_KEY)
        cls.debug_logger.debug(data)

    @classmethod
    def print_error(cls, error):
        if error is None or not issubclass(error, Exception):
            raise ValueError()
        if cls.error_logger is None:
            cls.error_logger = logging.getLogger(ERROR_LOG_KEY)
        cls.error_logger.error(error)

    @classmethod
    def print_sql(cls, sql):
        if not sql:
            raise ValueError()
        if cls.sql_logger is None:
            cls.sql_logger = logging.getLogger(SQL_LOG_KEY)
        cls.sql_logger.debug(sql)
