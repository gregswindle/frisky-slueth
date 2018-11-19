"""
tests.frisky_sleuth.test_violation
"""

import unittest
from frisky_sleuth.signature import Signature
from frisky_sleuth.violation import Violation

class TestViolation(unittest.TestCase):
    """
    Test frisky_sleuth.violation.Violation.
    """

    def setUp(self):
        """
        Run before each test.
        """

        self.violation_info = {
            'data': 'data',
            'signature': Signature({}),
            'line': None
        }

    def tearDown(self):
        """
        Run after each test.
        """

        self.violation_info = None

    def test_violation_constructor(self):
        """
        Constructor
        """
        violation = Violation(self.violation_info)
        self.assertEqual(violation.data, 'data')
        self.assertIsInstance(violation.signature, Signature)
        self.assertIsNone(violation.line)

        self.violation_info['line'] = 300
        violation = Violation(self.violation_info)
        self.assertEqual(violation.line, 300)

    def test_violation___str__(self):
        """
        __str__ override.
        """
        violation = Violation(self.violation_info)
        expected = '{"data": "data", "signature": {"caption": null, "description": null, "part": null, "pattern": null, "type": null}, "line": null}'

        self.assertEqual(str(violation), expected)

if __name__ == '__main__':
    unittest.main()
