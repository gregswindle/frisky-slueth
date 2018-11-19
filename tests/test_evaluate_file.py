"""
tests.frisky_sleuth.test_evaluate_load
"""

import os
import unittest
from frisky_sleuth.evaluate import file
from frisky_sleuth.signature import Signature

class TestEvaluateFile(unittest.TestCase):
    """
    Test frisky_sleuth.evaluate.file.
    """

    def setUp(self):
        """
        Run before each test.
        """

        self.fixturepath = {
            'subdir': 'tests/fixtures',
            'filename': 'contents.fixture.txt'
        }

    def tearDown(self):
        """
        Run after each test.
        """

        pass

    def test_evaluate_file_evaluate(self):
        class Expectations(object):
            COUNT = 1

        violations = file.evaluate(self.fixturepath, {'subdir': 'frisky_sleuth', 'filename': 'signatures.json'})
        self.assertIsInstance(violations, list)
        self.assertEqual(len(violations), Expectations.COUNT)


if __name__ == '__main__':
    unittest.main()
