from app.config import get_db_config
from app.model.pgadapter import PgAdapter


class BaseMapper:
    def __init__(self):
        # todo: read app env
        self._db = PgAdapter(get_db_config('develop'))
