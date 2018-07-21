import unittest
import psycopg2
from app.config import get_db_config
from app.model.pgadapter import PgAdapter


class TestPgAdapterTest(unittest.TestCase):
    def setUp(self):
        config = get_db_config('pgadapter')
        self.__db = PgAdapter(config)

    def tearDown(self):
        self.__db.execute('TRUNCATE TABLE cars RESTART IDENTITY;')
        self.__db.execute('TRUNCATE TABLE car_makers RESTART IDENTITY;')
        self.__db.commit()

    def test_add_success(self):
        data = (None, 'alfa romeo')
        expected = False
        try:
            self.__db.save('save_car_maker', data)
            self.__db.commit()
            expected = True
        except Exception as e:
            self.__db.rollback()
            expected = False
        self.assertEqual(True, expected)

    def test_edit_success(self):
        self.init_test_data()
        try:
            self.__db.save('save_car_maker', (1, 'Toyota'))
            self.__db.commit()
            expected = True
        except Exception as e:
            self.__db.rollback()
            expected = False
        row = self.__db.find_one('find_car_makers_by', ('Toyota',))
        self.__db.commit()
        self.assertEqual(True, expected)
        self.assertEqual('Toyota', row['name'])

    def test_fetch_last_row_id(self):
        data = (None, 'test')
        last_id = 0
        try:
            self.init_test_data()
            self.__db.save('save_car_maker', data)
            last_id = self.__db.fetch_last_row_id()
            self.__db.commit()
        except psycopg2.DatabaseError as e:
            self.__db.rollback()
        self.assertEqual(4, last_id)

    def test_find_success(self):
        self.init_test_data()
        rows = self.__db.find('find_car_makers_by', ('toyota',))
        self.__db.commit()
        self.assertEqual(1, len(rows))
        self.assertEqual('toyota', rows[0]['name'])

    def test_fetch_rowcount(self):
        self.init_test_data()

        # check car makers row count
        expected = self.__db.fetch_rowcount('car_makers')
        self.__db.commit()
        self.assertEqual(3, expected)

        # check cars row count
        expected = self.__db.fetch_rowcount('cars')
        self.__db.commit()
        self.assertEqual(9, expected)

    def test_command_is_empty(self):
        with self.assertRaises(ValueError):
            self.__db.save('', ('test',))
            self.__db.save(None, ('test',))
            self.__db.remove('', ('test',))
            self.__db.remove(None, ('test',))
            self.__db.find('', ('test',))
            self.__db.find(None, ('test',))
            self.__db.find_one('', ('test',))
            self.__db.find_one(None, ('test',))
            self.__db.execute('', ('test',))
            self.__db.execute(None, ('test',))
            self.__db.fetch_rowcount('')
            self.__db.fetch_rowcount(None)
            self.__db.bulk_insert('', [])
            self.__db.bulk_insert(None, [])
            self.__db.bulk_insert('test', None)
            self.__db.bulk_insert('test', [])

    def test_config_is_empty(self):
        db = PgAdapter(None)
        with self.assertRaises(ValueError):
            db.save('save_car_maker', ('FIAT',))

    def test_run_invalid_command(self):
        with self.assertRaises(psycopg2.ProgrammingError):
            self.__db.save('invalid command', (None, 'test'))
            self.__db.remove('invalid command', (None,))
            self.__db.find('invalid command', (None,))
            self.__db.find_one('invalid command', (None,))
            self.__db.execute('invalid command')
            self.__db.bulk_insert('invalid command',([]))
            self.__db.fetch_rowcount('invalid table name')
        self.__db.rollback()

    def init_test_data(self):
        car_makers = [
            ('toyota',),
            ('nissan',),
            ('honda',)
        ]
        cars = [
            (1, 'カローラ'),
            (1, 'クレスタ'),
            (1, '86'),
            (2, 'スカイライン'),
            (2, 'フェアレディZ'),
            (2, 'マーチ'),
            (3, 'Civic'),
            (3, 'S2000'),
            (3, 'フリード')
        ]
        query1 = 'INSERT INTO car_makers (name) VALUES (%s);'
        query2 = 'INSERT INTO cars (maker_id, name) VALUES (%s, %s);'

        try:
            self.__db.bulk_insert(query1, car_makers)
            self.__db.bulk_insert(query2, cars)
            self.__db.commit()
        except Exception as e:
            print(e)
            self.__db.rollback()
