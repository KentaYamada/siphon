from app.model.pgadapter import PgAdapter


class BaseMapper:
    def __init__(self):
        self._db = PgAdapter()

    def format_rows(self, rows, fields):
        if rows is None or fields is None:
            raise ValueError('Invalid argument')
        if not isinstance(fields, list):
            raise ValueError('Invalid data type. arg:fields_list')
        rows = [{f: row[f] for f in fields} for row in rows]
        return rows

    def format_row(self, row, fields):
        if row is None or fields is None:
            raise ValueError('Invalid argumant')
        if not isinstance(fields, (tuple, list)):
            raise ValueError('Invalid data type')
        return {f: row[f] for f in fields}
