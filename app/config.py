"""
    Siphon
    config.py
    Siphon app config
    Author: Kenta Yamada

    See configration options
    Flask
        https://flask.palletsprojects.com/en/1.1.x/config/#builtin-configuration-values
    Flask-JWT-extended
        https://flask-jwt-extended.readthedocs.io/en/latest/
"""
from os import environ, path
import logging

# constants
DEBUG_LOG_KEY = 'debug_logger'
ERROR_LOG_KEY = 'error_logger'
SQL_LOG_KEY = 'sql_logger'


class BaseConfig:
    # flask options
    DEBUG = False
    ENV = ''
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    TESTING = False
    SECRET_KEY = ''

    # JWT options
    JWT_BLACKLIST_ENABLED = True
    JWT_SECRET_KEY = ''
    JWT_BACKLIST_TOKEN_CHECKS = ['identity']
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_REFRESH_TOKEN_EXPIRES = False

    # database configs
    DATABASE = {}

    def _get_logging_options(self):
        raise NotImplementedError()

    def __str__(self):
        return 'app.config.{0}'.format(type(self).__name__)


class ProductionConfig(BaseConfig):
    ENV = 'production'
    JWT_SECRET_KEY = ''


class StagingConfig(BaseConfig):
    ENV = 'production'
    JWT_SECRET_KEY = ''


class TestConfig(BaseConfig):
    ENV = 'test'
    TESTING = True
    TEST_ROOT_DIR = './app/tests'
    DATABASE = {
        'host': 'localhost',
        'dbname': 'siphon_test',
        'user': 'kenta',
        'password': 'kenta'
    }
    JWT_BLACKLIST_ENABLED = False
    JWT_SECRET_KEY = 'testing'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    DATABASE = {
        'host': 'localhost',
        'dbname': 'siphon_dev',
        'user': 'kenta',
        'password': 'kenta'
    }
    JWT_BLACKLIST_ENABLED = True
    JWT_SECRET_KEY = 'development'

    def _get_logging_options(self):
        log_dir = '{0}/log'.format(path.dirname(path.abspath(__file__)))
        options = {
            'version': 1,
            'formatters': {
                'devFormat': {
                    'format': '[%(levelname)s] %(asctime)s %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'
                }
            },
            'handlers': {
                'debug_log_file_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/debug.log'.format(log_dir),
                },
                'debug_console_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.StreamHandler',
                    'formatter': 'devFormat'
                },
                'sql_log_file_handler': {
                    'level': logging.DEBUG,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/sql.log'.format(log_dir),
                },
                'error_log_file_handler': {
                    'level': logging.ERROR,
                    'class': 'logging.FileHandler',
                    'formatter': 'devFormat',
                    'filename': '{0}/error.log'.format(log_dir),
                }
            },
            'loggers': {
                DEBUG_LOG_KEY: {
                    'level': logging.DEBUG,
                    'handlers': [
                        'debug_log_file_handler',
                        'debug_console_handler',
                    ],
                    'propagate': 0
                },
                SQL_LOG_KEY: {
                    'level': logging.DEBUG,
                    'handlers': [
                        'sql_log_file_handler'
                    ],
                    'propagate': 0
                },
                ERROR_LOG_KEY: {
                    'level': logging.ERROR,
                    'handlers': [
                        'error_log_file_handler'
                    ],
                    'propagate': 0
                }
            }
        }
        return options


def get_config():
    configs = {
        'production': ProductionConfig(),
        'test': TestConfig(),
        'development': DevelopmentConfig()}
    app_env = environ.get('APP_TYPE')
    if app_env not in configs:
        raise RuntimeError()
    return configs[app_env]
