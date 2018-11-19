"""
tests.frisky_sleuth.evaluate.test_load
"""

import unittest
from frisky_sleuth.evaluate import load
from frisky_sleuth.signature import Signature

class TestEvaluateLoad(unittest.TestCase):
    """
    Test frisky_sleuth.evaluate.load.
    """

    def setUp(self):
        """
        Run before each test.
        """

        self.params = {
            'subdir': './tests/fixtures',
            'filename': 'contents.fixture.txt'
        }

    def tearDown(self):
        """
        Run after each test.
        """

        pass

    def test_evaluate_load_signatures(self):
        """
        frisky_sleuth.evaluate.load.signatures
        """
        signatures = load.signatures()
        self.assertIsInstance(signatures, list)
        self.assertIsInstance(signatures[0], Signature)

    def test_evaluate_load_signatures_io_error(self):
        """
        frisky_sleuth.evaluate.load.signatures raises an IOError
        """
        with self.assertRaises(IOError):
            load.signatures({
                'subdir': '/i/v/a/l/i/d/p/a/t/h/',
                'filename': 'truffle-hog-signatures.json'
            })

    def test_evaluate_load_contents(self):
        """
        frisky_sleuth.evaluate.load.contents
        """
        lines = load.contents(self.params)
        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 1)

    def test_evaluate_load_contents_io_error(self):
        """
        frisky_sleuth.evaluate.load.contents raises IOError
        """
        with self.assertRaises(IOError):
            load.contents({
                'subdir': '/i/v/a/l/i/d/p/a/t/h/',
                'filename': 'ineffible-file.nowhere'
            })

    def test_evaluate_load_extension(self):
        """
        frisky_sleuth.evaluate.load.extension
        """
        ext = load.extension(self.params)
        self.assertEqual(ext, 'txt')

    def test_evaluate_load_filename(self):
        """
        frisky_sleuth.evaluate.load.filename
        """
        name = load.filename(self.params)
        self.assertEqual(name, self.params.get('filename'))

    def test_evaluate_load_path(self):
        """
        frisky_sleuth.evaluate.load.path
        """
        path = load.path(self.params)
        self.assertEqual(path, f"{self.params.get('subdir')}/{self.params.get('filename')}")

    def test_evaluate_load_data(self):
        """
        frisky_sleuth.evaluate.load.data
        """
        pass

if __name__ == '__main__':
    unittest.main()
