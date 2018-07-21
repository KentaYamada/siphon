from unittest import TestLoader, TextTestRunner


TEST_ROOT_DIR = './app/tests'

def run():
    loader = TestLoader()
    tests = loader.discover(TEST_ROOT_DIR)
    runner = TextTestRunner()
    runner.run(tests)


if __name__ == '__main__':
    run()
