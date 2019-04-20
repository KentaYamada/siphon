from app.model.pgadapter import PgAdapter


class BaseMapper:
    def __init__(self):
        self._db = PgAdapter()

    def format_rows(self, rows, field_list):
        if rows is None or field_list is None:
            raise ValueError('Invalid argument')
        if not isinstance(field_list, list):
            raise ValueError('Invalid data type. arg:fields_list')
        rows = [{f: row[f] for f in field_list} for row in rows]
        return rows
