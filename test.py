# -*- coding: utf-8 -*-

import os
from unittest import TestLoader, TextTestRunner


TEST_DIR = './siphon/tests/'

if __name__ == '__main__':
    if not os.path.isdir(TEST_DIR):
        print('Test directory not found.')
        exit(1)
    loader = TestLoader()
    tests = loader.discover(TEST_DIR)
    runner = TextTestRunner()
    runner.run(tests)
