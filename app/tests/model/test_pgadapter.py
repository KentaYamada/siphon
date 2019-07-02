import psycopg2
from unittest import TestCase
from app.model.pgadapter import PgAdapter


class TestPgAdapterTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = PgAdapter()

    @classmethod
    def tearDownClass(cls):
        cls.db = None

    def tearDown(self):
        self.db.execute_proc('cleanup_pgadapter')
        self.db.commit()
        self.db = None

    def test_add(self):
        data = (None, 'alfa romeo')
        result = self.db.execute_proc('save_car_maker', data)
        self.db.commit()
        self.assertEqual(1, result)

    def test_edit(self):
        self.init_data()
        data = (1, 'Toyota autmobile')
        result = self.db.execute_proc('save_car_maker', data)
        self.db.commit()
        self.assertEqual(1, result)
        row = self.db.find_one_proc('find_car_makers_by', ('Toyota',))
        self.db.commit()
        self.assertEqual('Toyota autmobile', row['name'])

    def test_delete(self):
        self.init_data()
        data = (1,)
        result = self.db.execute_proc('delete_car_maker', data)
        self.db.commit()
        self.assertEqual(1, result)

    def test_find_proc_success(self):
        self.init_data()
        rows = self.db.find_proc('find_car_makers_by', ('toyota',))
        self.db.commit()
        self.assertEqual(1, len(rows))
        self.assertEqual('toyota', rows[0]['name'])

    def test_fetch_rowcount(self):
        self.init_data()
        result = self.db.fetch_rowcount('car_makers')
        self.db.commit()
        self.assertEqual(3, result)

    def test_fetch_last_row_id(self):
        self.db.execute_proc('save_car_maker', (None, 'test'))
        result = self.db.fetch_last_row_id()
        self.db.commit()
        self.assertEqual(1, result)

    def test_has_row(self):
        self.init_data()
        data = (1,)
        result = self.db.has_row('car_makers', data)
        self.db.commit()
        self.assertTrue(result)

    def test_has_no_row(self):
        self.init_data()
        data = (999,)
        result = self.db.has_row('car_makers', data)
        self.db.commit()
        self.assertFalse(result)

    def test_invalid_command(self):
        with self.assertRaises(psycopg2.ProgrammingError):
            self.db.execute_proc('invalid command', (None, 'test'))
            self.db.find('invalid command', (None,))
            self.db.find_one('invalid command', (None,))
            self.db.execute('invalid command')
            self.db.bulk_insert('invalid command', ([]))
            self.db.fetch_rowcount('invalid table name')
        self.db.rollback()

    def test_empty_command(self):
        with self.assertRaises(ValueError):
            self.db.execute_proc('', ('test',))
            self.db.execute_proc(None, ('test',))
            self.db.find('', ('test',))
            self.db.find(None, ('test',))
            self.db.find_one('', ('test',))
            self.db.find_one(None, ('test',))
            self.db.execute('', ('test',))
            self.db.execute(None, ('test',))
            self.db.fetch_rowcount('')
            self.db.fetch_rowcount(None)
            self.db.bulk_insert('', [])
            self.db.bulk_insert(None, [])
            self.db.bulk_insert('test', None)
            self.db.bulk_insert('test', [])
        self.db.rollback()

    def init_data(self):
        self.db.execute_proc('create_test_data_pgadapter')
        self.db.commit()
