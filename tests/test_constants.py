"""
tests.frisky_sleuth.test_constants
"""

import unittest
from frisky_sleuth.constants import SignatureConstants

class TestConstants(unittest.TestCase):
    """
    Test frisky_sleuth.constants.SignatureConstants.
    """

    def setUp(self):
        """
        Run before each test.
        """

        pass

    def tearDown(self):
        """
        Run after each test.
        """

        pass

    def test_constants_attributes(self):
        """
        SignatureConstants.Attributes
        """
        self.assertEqual(SignatureConstants.Attributes.CAPTION, 'caption')
        self.assertEqual(SignatureConstants.Attributes.DESCRIPTION, 'description')
        self.assertEqual(SignatureConstants.Attributes.PART, 'part')
        self.assertEqual(SignatureConstants.Attributes.PATTERN, 'pattern')
        self.assertEqual(SignatureConstants.Attributes.TYPE, 'type')

    def test_constants_parts(self):
        """
        SignatureConstants.Parts
        """
        self.assertEqual(SignatureConstants.Parts.CONTENTS, 'contents')
        self.assertEqual(SignatureConstants.Parts.EXTENSION, 'extension')
        self.assertEqual(SignatureConstants.Parts.FILENAME, 'filename')
        self.assertEqual(SignatureConstants.Parts.PATH, 'path')
        self.assertEqual(SignatureConstants.Parts.VALUES, [
            'contents',
            'extension',
            'filename',
            'path'
        ])

    def test_constants_types(self):
        """
        SignatureConstants.Types
        """
        self.assertEqual(SignatureConstants.Types.MATCH, 'match')
        self.assertEqual(SignatureConstants.Types.REGEX, 'regex')
        self.assertEqual(SignatureConstants.Types.VALUES, [
            'match',
            'regex'
        ])

if __name__ == '__main__':
    unittest.main()
