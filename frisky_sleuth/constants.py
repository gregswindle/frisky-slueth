"""
frisky_sleuth.constants
String enumerator with valid values.
"""


class SignatureConstants(object):
    """
    SignatureConstants.
    """

    class Attributes(object):
        """
        Valid signature attribute names.
        """

        CAPTION = 'caption'
        DESCRIPTION = 'description'
        PART = 'part'
        PATTERN = 'pattern'
        TYPE = 'type'

    class Files(object):
        """
        Files.
        """

        PATH_PARAMS = {
            'subdir': None,
            'filename': None
        }

    class Parts(object):
        """
        Valid signature.part values.
        """

        CONTENTS = 'contents'
        EXTENSION = 'extension'
        FILENAME = 'filename'
        PATH = 'path'

        VALUES = [CONTENTS, EXTENSION, FILENAME, PATH]

    PATH_PARAMS = {
        'subdir': 'frisky_sleuth',
        'filename': 'signatures.json'
    }

    class Types(object):
        """
        Valid signature.type values.
        """

        MATCH = 'match'
        REGEX = 'regex'

        VALUES = [MATCH, REGEX]
