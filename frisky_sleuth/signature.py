"""
frisky_sleuth.signature
"""

import json
from .constants import SignatureConstants
from .evaluate import load, match

class Signature():
    """
    Signature
    """

    def __init__(self, signature):
        """
        Constructor.
        """

        self.caption = signature.get(SignatureConstants.Attributes.CAPTION)
        self.description = signature.get(SignatureConstants.Attributes.DESCRIPTION)
        self.part = signature.get(SignatureConstants.Attributes.PART)
        self.pattern = signature.get(SignatureConstants.Attributes.PATTERN)
        self.type = signature.get(SignatureConstants.Attributes.TYPE)

    def evaluate(self, data, options=SignatureConstants.Files.PATH_PARAMS):
        """
        Inspect either a str or Stream of data; or by resource directory path and filename.
        Note that the "data" and "options" paramaters are mutually exclusive, which "data"
        taking precendence over "options".
            :param self: Reference to the Signature instance.
            :param data: Either a string or Stream of data.
            :param options.subdir: Relative of full directory path to a file.
            :param options.filename: The name of the file whose part should be inspected.
            :returns: Violation|None
        """

        violation = None

        resource_data = data or load.data(options, self)

        violation = match.matches(resource_data, self)

        return violation

    def __str__(self):
        """
        Returns a JSON representation of a Signature instance.
            :param self: Reference to Signature instance.
        """

        return json.dumps({
            'caption': self.caption,
            'description': self.description,
            'part': self.part,
            'pattern': self.pattern,
            'type': self.type
        })

    @staticmethod
    def from_list(signatures):
        """
        Convert a list of dicts into a list of Signatures.
          :param signatures: A list of signature dictionaries.
        """

        def callback(params):
            return Signature(params)

        return list(map(callback, signatures))
