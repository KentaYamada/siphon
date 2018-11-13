from app.model.pgadapter import PgAdapter
from app.config import get_db_config


class BaseModel:
    db = PgAdapter(get_db_config('develop'))

    def __init__(self):
        self.__errors = {}

    @property
    def validation_errors(self):
        return self.__errors

    def is_valid(self):
        return True if not self.__errors else False

    def _clear_validation_error(self, field):
        if field in self.__errors.keys():
            del self.__errors[field]

    def _add_validation_error(self, field, message):
        if field in self.__errors.keys():
            self.__errors[field].append(message)
        else:
            self.__errors[field] = [message]
