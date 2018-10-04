"""
    config.py
    siphon app config
    Author: Kenta Yamada
"""

DATABASES = {
    'pgadapter': {
        'host': 'localhost',
        'dbname': 'pgadapter_test',
        'user': 'kenta',
        'password': 'kenta'
    },
    'develop': {
        'host': 'localhost',
        'dbname': 'siphon_dev',
        'user': 'kenta',
        'password': 'kenta'
    }
}


def get_db_config(key):
    if not key:
        raise ValueError('key should be set value.')
    if key not in DATABASES:
        raise Exception('Missing dabase config.')
    return DATABASES[key]
