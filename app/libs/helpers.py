"""
    helpers.py
    This module implements app helper functions
    Author: Yamaken
"""
from datetime import datetime


def format_date(value):
    if value is None:
        return None
    return datetime.strptime(value, '%Y-%m-%d').date()


def format_time(value):
    if value is None:
        return None
    return datetime.strptime(value, '%H:%M:%S').time()


def has_request_keys(request, keys):
    if request is None or keys is None:
        raise ValueError('Invalid argument')
    if not isinstance(keys, set):
        raise ValueError('Invalid data type: keys')
    return request.keys() <= keys
