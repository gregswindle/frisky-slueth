"""
tests.frisky_sleuth.test_signature
"""

import unittest
from frisky_sleuth.constants import SignatureConstants
from frisky_sleuth.signature import Signature
from frisky_sleuth.violation import Violation

class TestSignature(unittest.TestCase):
    """
    Test frisky_sleuth.signature.Signature.
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

    def test_signature_null_constructor(self):
        """
        NullConstructor
        """
        signature = Signature({})
        self.assertIsNone(signature.caption)
        self.assertIsNone(signature.description)
        self.assertIsNone(signature.part)
        self.assertIsNone(signature.pattern)
        self.assertIsNone(signature.type)

    def test_signature_constructor(self):
        """
        Constructor
        """
        signature = Signature({
            'caption': 'a',
            'description': 'b',
            'part': SignatureConstants.Parts.FILENAME,
            'pattern': 'test_file.py',
            'type': SignatureConstants.Types.MATCH
        })
        self.assertIsInstance(signature, Signature)
        self.assertEqual(signature.description, 'b')

    def test_signature_evaluate(self):

        data = None
        signature = Signature({
            'caption': 'a',
            'description': 'b',
            'part': SignatureConstants.Parts.EXTENSION,
            'pattern': 'pem',
            'type': SignatureConstants.Types.MATCH
        })
        options = {
            'filename': 'putin-potomic.pem'
        }

        self.assertIsInstance(signature.evaluate(data, options), Violation)

    def test_signature___str__(self):
        """
        JSON encoded output.
        """
        expected = '{"caption": null, "description": null, "part": null, "pattern": null, "type": null}'
        self.assertEqual(str(Signature({})), expected)

if __name__ == '__main__':
    unittest.main()
