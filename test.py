from os import path
from unittest import TestLoader, TextTestRunner


TEST_ROOT_DIR = './app/tests'


def run():
    paths = [
        TEST_ROOT_DIR,
        path.join(TEST_ROOT_DIR, 'controller')
    ]
    loader = TestLoader()
    for p in paths:
        tests = loader.discover(p)
        runner = TextTestRunner()
        runner.run(tests)


if __name__ == '__main__':
    run()
