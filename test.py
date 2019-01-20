from os import environ, path
from unittest import TestLoader, TextTestRunner
from app.config import get_config


def run():
    # switch test config
    environ['APP_TYPE'] = 'test'
    config = get_config()

    paths = (
        config.TEST_ROOT_DIR,
    )
    loader = TestLoader()
    for p in paths:
        tests = loader.discover(p)
        runner = TextTestRunner()
        runner.run(tests)


if __name__ == '__main__':
    run()
