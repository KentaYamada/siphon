from app.model.pgadapter import PgAdapter
from app.config import get_db_config


class Category():
    db = PgAdapter(get_db_config('develop'))

    def __init__(self, id=None, name=''):
        self.__id = id
        self.__name = name
        self.__errors = {}

    @property
    def errors(self):
        return self.__errors

    def validate(self):
        # ToDo: decorator化
        isValid = True
        if not self.__name:
            self.__set_error('name', '商品カテゴリ名は必須です')
            isValid = False
        return isValid

    def save(self):
        if not self.validate():
            return False
        saved = False
        try:
            Category.db.save('save_category', (self.__id, self.__name))
            saved = True if Category.db.affected_rows == 1 else False
            if saved:
                Category.db.commit()
            else:
                Category.db.rollback()
        except Exception as e:
            Category.db.rollback()
            print(e)
            raise e
        return saved

    def delete(self):
        if self.__id is None:
            return False
        deleted = False
        try:
            Category.db.remove('delete_category', (self.__id,))
            deleted = True if Category.db.affected_rows == 1 else False
            if deleted:
                Category.db.commit()
            else:
                Category.db.rollback()
        except Exception as e:
            Category.db.rollback()
            print(e)
            raise e
        return deleted

    @classmethod
    def find_all(cls):
        categories = []
        try:
            rows = Category.db.find('find_categories')
            if len(rows) > 0:
                categories = [
                    {'id': row['id'], 'name': row['name']} for row in rows]
        except Exception as e:
            print(e)
            raise e
        print(categories)
        return categories

    def __set_error(self, field, message):
        if field in self.__errors:
            self.__errors[field].append(message)
        else:
            self.__errors[field] = [message]
