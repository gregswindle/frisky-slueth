"""
frisky_sleuth.violation
Data-leakage value object.
"""

import json

class Violation:
    """
    Constructor for generating a data-leakage result.
    """

    def __init__(self, params):
        """
        Constructor.
          :param self: Reference to signature instance.
          :param params: A dictionary of "data", "signature", and "line" number.
        """
        self.data = params.get('data')
        self.signature = params.get('signature')
        self.line = params.get('line')

    def __str__(self):
        """
        Default to JSON.
        """
        info = {
            'data': self.data,
            'signature': json.loads(str(self.signature)),
            'line': self.line
        }
        return json.dumps(info)

    @staticmethod
    def factory(data, signature, line=None):
        """
        Convenience method for creating a Violation.
            :param data: The offending secret.
            :param signature: The definition of the secret.
            :param line: The line number on which a potential secret was found.
            :returns: Violation
        """
        return Violation({
            'data': data,
            'signature': signature,
            'line': line
        })