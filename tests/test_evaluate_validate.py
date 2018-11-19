"""
frisky_sleuth.evaluate.validate
tests.test_evaluate_validate
"""

import unittest
from unittest.mock import MagicMock, Mock
from frisky_sleuth.constants import SignatureConstants
from frisky_sleuth.evaluate import validate
from frisky_sleuth.signature import Signature
from frisky_sleuth.violation import Violation

class TestEvaluateValidate(unittest.TestCase):
    """
    Test frisky_sleuth.evaluate_validate.
    """

    def setUp(self):
        """
        Run before every test.
        """
        pass

    def tearDown(self):
        """
        Run after every test.
        """
        pass

    def test_evaluate_validate_by_part(self):
        """
        frisky_sleuth.evaluate.validate.by_part
        """

        signature = Signature({'part': ''})
        for part in SignatureConstants.Parts.VALUES:
            signature.part = part
            validate.by_part(signature)


        with self.assertRaises(ValueError):
            signature.part = 'UNKNOWN'
            validate.by_part(signature)


    def test_evaluate_validate_by_type(self):
        """
        frisky_sleuth.evaluate_validate.by_string
        """

        signature = Signature(dict(type=''))
        for kind in SignatureConstants.Types.VALUES:
            signature.type = kind
            validate.by_type(signature)

        with self.assertRaises(ValueError):
            signature.type = 'UNKNOWN'
            validate.by_type(signature)



    def test_evaluate_validate_single(self):
        """
        frisky_sleuth.evaluate_validate.contents
        """
        signature = Signature(dict(part='path', type='match'))
        validate.single(signature)

        signature.part = 'unknown'
        signature.type = 'unknown'
        validate.single(signature)


    def test_evaluate_validate_every(self):
        """
        frisky_sleuth.evaluate_validatees
        """
        signatures = [
            Signature(dict(part=SignatureConstants.Parts.CONTENTS, type=SignatureConstants.Types.MATCH)),
            Signature(dict(part='UNKNOWN', type='UNKNOWN'))
        ]
        validate.single = Mock(return_value=True)
        validate.every(signatures)
        self.assertEqual(validate.single.call_count, 2)

        # Test short-circuit "break"
        validate.single.reset_mock()
        validate.single = Mock(return_value=False)
        validate.every(signatures)
        self.assertEqual(validate.single.call_count, 1)
        validate.single.side_effect = None

    def test_evaluate_validate_throw_value_error(self):
        self.assertRaises(
            ValueError,
            validate.throw_value_error,
            'foo', 'part', SignatureConstants.Parts.VALUES
        )

