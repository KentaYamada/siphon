"""
    Siphon
    config.py
    siphon app config
    Author: Kenta Yamada
"""
from os import environ


class BaseConfig:
    # flask configs
    DEBUG = False
    TESTING = False
    JSON_AS_ASCII = False
    JSON_SORT_KEYS = True
    SECRET_KEY = ''

    # database configs
    DATABASE = {}


class ProductionConfig(BaseConfig):
    pass


class DemoConfig(BaseConfig):
    pass


class StagingConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True
    TEST_ROOT_DIR = './app/tests'
    DATABASE = {
        'host': 'localhost',
        'dbname': 'siphon_test',
        'user': 'kenta',
        'password': 'kenta'
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DATABASE = {
        'host': 'localhost',
        'dbname': 'siphon_dev',
        'user': 'kenta',
        'password': 'kenta'
    }


def get_config():
    configs = {
        'production': ProductionConfig(),
        'test': TestConfig(),
        'development': DevelopmentConfig()}
    app_env = environ.get('APP_TYPE')
    if app_env not in configs:
        raise RuntimeError()
    return configs[app_env]
