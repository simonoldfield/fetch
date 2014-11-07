__author__ = 'u63606'

import doctest
import fetch
import fetch.auto


def load_tests(loader=None, tests=None, ignore=None):
    tests.addTests(doctest.DocTestSuite(fetch))
    tests.addTests(doctest.DocTestSuite(fetch.auto))
    return tests
