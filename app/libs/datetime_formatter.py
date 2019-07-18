from datetime import datetime


def format_date(value):
    if value is None:
        return None
    return datetime.strptime(value, '%Y-%m-%d').date()


def format_time(value):
    if value is None:
        return None
    return datetime.strptime(value, '%H:%M:%S').time()
