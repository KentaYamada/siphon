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
from os import environ


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


def get_config():
    configs = {
        'production': ProductionConfig(),
        'test': TestConfig(),
        'development': DevelopmentConfig()}
    app_env = environ.get('APP_TYPE')
    if app_env not in configs:
        raise RuntimeError()
    return configs[app_env]
