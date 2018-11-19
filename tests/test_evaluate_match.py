"""
frisky_sleuth.evaluate.match
tests.test_evaluate_match_match
"""

import unittest
from unittest.mock import Mock, patch
from frisky_sleuth.constants import SignatureConstants
from frisky_sleuth.evaluate import match
from frisky_sleuth.signature import Signature
from frisky_sleuth.violation import Violation

class TestEvaluateMatch(unittest.TestCase):
    """
    Test frisky_sleuth.evaluate.match.
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

    def test_evaluate_match_by_regex(self):
        """
        frisky_sleuth.evaluate.match.by_regex
        """

        signature = Signature({
          'caption': 'static passwords',
          'description': 'frisky_sleuth.evaluate.match.by_regex',
          'part': SignatureConstants.Parts.CONTENTS,
          'pattern': "(password|passwd|pass|pwd)['\"]? ?[=:] ?['\"]?(?!(['\"]))",
          'type': SignatureConstants.Types.REGEX
        })
        data = 'password="OMG!LOL-puppies11"'
        self.assertEqual(match.by_regex(data, signature), data)
        data = 'account=foobar'
        self.assertNotEqual(match.by_regex(data, signature), data)


    def test_evaluate_match_by_string(self):
        """
        frisky_sleuth.evaluate.match.by_string
        """

        signature = Signature({
          'caption': 'Potential cryptographic private key',
          'description': 'frisky_sleuth.evaluate.match.by_string',
          'part': SignatureConstants.Parts.EXTENSION,
          'pattern': "pem",
          'type': SignatureConstants.Types.MATCH
        })
        data = 'pem'
        self.assertEqual(match.by_string(data, signature), data)
        data = 'pembock'
        self.assertNotEqual(match.by_string(data, signature), data)

    def test_evaluate_match_by_type(self):
        """
        frisky_sleuth.evaluate.match.by_type
        """
        try:
            signature = Signature({'type': 'UNKNOWN'})
            match.by_type('', signature)
        except ValueError:
            self.assertRaises(ValueError)

    def test_evaluate_match_contents(self):
        """
        frisky_sleuth.evaluate.match.contents
        """

        signature = Signature({
          'caption': 'static passwords',
          'description': 'frisky_sleuth.evaluate.match.contents',
          'part': SignatureConstants.Parts.CONTENTS,
          'pattern': "(password|passwd|pass|pwd)['\"]? ?[=:] ?['\"]?(?!(['\"]))",
          'type': SignatureConstants.Types.REGEX
        })
        file_contents = [
            'password="foobar"',
            '',
            'pass=another-password!1234'
        ]

        class Expectations(object):
            FIRST = 0
            SECOND = 1
            COUNT = 2

        # Positive test: violations found

        results = match.contents(file_contents, signature)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), Expectations.COUNT)
        self.assertIsInstance(results[Expectations.FIRST], Violation)
        self.assertIsInstance(results[Expectations.SECOND], Violation)

        # Negative test: no violations found
        file_contents = ['hello', 'world!']
        self.assertIsNone(match.contents(file_contents, signature))

    def test_evaluate_match_extension(self):
        data = 'pem'
        signature = Signature({
            'part': SignatureConstants.Parts.EXTENSION,
            'type': SignatureConstants.Types.MATCH,
            'pattern': 'pem',
            'caption': 'Potential cryptographic private key',
            'description': None
        })
        self.assertIsInstance(match.extension(data, signature), Violation)

        data = 'not-pem'
        self.assertIsNone(match.extension(data, signature))

    def test_evaluate_match_filename(self):
        data = '.bash_history'
        signature = Signature({
            'part': SignatureConstants.Parts.FILENAME,
            'type': SignatureConstants.Types.REGEX,
            'pattern': '\\A\\.?(bash_|zsh_|z)?history$',
            'caption': 'Shell command history file',
            'description': None
        })
        violation = match.filename(data, signature)
        self.assertIsInstance(violation, Violation)

        data = 'when-dealing-with.bash_history'
        violation = match.filename(data, signature)
        self.assertNotIsInstance(violation, Violation)

    def test_evaluate_match_matches(self):
        """
        frisky_sleuth.evaluate.match.matches
        """
        data = 'data'

        # Match by string equivalence
        signature = Signature({
            'type': SignatureConstants.Types.MATCH,
            'part': 'filename',
            'pattern': data,

        })
        self.assertIsInstance(match.matches(data, signature), Violation)

        # Match by regular expression
        signature.type = SignatureConstants.Types.REGEX
        self.assertIsInstance(match.matches(data, signature), Violation)

    def test_evaluate_match_path(self):
        filepath = '.aws/credentials'
        signature = Signature({
            'part': 'path',
            'type': 'regex',
            'pattern': '(\\.)?aws\/credentials$',
            'caption': 'AWS CLI credentials file',
            'description': None
        })
        violation = match.path(filepath, signature)
        self.assertIsInstance(violation, Violation)

        filepath = '.amazon-web-services'
        violation = match.path(filepath, signature)
        self.assertNotIsInstance(violation, Violation)