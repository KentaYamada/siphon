import unittest
from os import path
from app.util import init_logger


class TestLogging(unittest.TestCase):
    def tearDown(self):
        pass

    def test_output_log(self):
        filename = 'app/logging.dev.yaml'
        logger = init_logger(filename)
        logger.debug('this is debug')
        logger.info('select * from table;')
        logger.error('this is error')
        for f in ['debug.log', 'error.log', 'query.log']:
            file_path = path.abspath(path.join('log', f))
            expected = path.exists(file_path)
            self.assertTrue(expected)


if __name__ == '__main__':
    unittest.main()
