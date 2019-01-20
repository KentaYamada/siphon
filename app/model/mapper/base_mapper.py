from app.model.pgadapter import PgAdapter


class BaseMapper:
    def __init__(self):
        self._db = PgAdapter()
