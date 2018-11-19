"""
frisky_sleuth.evaluate.match
"""

import re
from . import validate
from ..constants import SignatureConstants
from ..violation import Violation

def by_regex(data, signature):
    """
    Look for a secret using a regular expression.
      :param data: The resource you want to inspect.
      :param pattern: The regular expression you want to use.
      :return: Matching data or None.
    """

    result = None

    is_match = re.compile(signature.pattern, re.IGNORECASE).search(data)

    if is_match:
        result = data.strip()

    return result


def by_string(data, signature):
    """
    Look for exact matches.
      :param data: The string you want to inspect.
      :param pattern: The string you want to find.
      :return: Matching data or None.
    """

    result = None
    if data == signature.pattern:
        result = data

    return result

def by_type(data, signature):
    """
    docstring here
        :param data:
        :param signature:
    """

    validate.single(signature)

    typematcher = {}
    typematcher[SignatureConstants.Types.MATCH] = by_string
    typematcher[SignatureConstants.Types.REGEX] = by_regex

    match_fxn = typematcher.get(signature.type)
    return match_fxn(data, signature)

def contents(file_contents, signature):
    """
    Evaluate a file's contents line-by-line for secrets.
        :param data: A list of strings (each line in a file).
        :param signature: A formal data-leakage definition with pattern detection.
        :returns: list<Violation> or None.
    """
    results = None
    violations = []
    line = 1
    for entry in file_contents:
        data = by_type(entry, signature)
        if data:
            violations.append(Violation.factory(file_contents, signature, line))
            results = violations
        line += 1

    return results

def extension(ext, signature):
    """
    Match by file extension.
    """
    violation = None

    if by_type(ext, signature):
        violation = Violation.factory(ext, signature)
    return violation


def filename(file_name, signature):
    """
    Match by filename.
    """
    violation = None
    if by_type(file_name, signature):
        violation = Violation.factory(file_name, signature)
    return violation

def matches(data, signature):
    """
    Look for secret matches.
      :param data: The resource you want to inspect.
      :param pattern: A string sequence to check for.
      :param match: Either "regex" for string patterns or "match" for string equivalence.
      :raise ValueError:
      :return: Matching data or None.
    """

    validate.single(signature)

    matchmaker = {}
    matchmaker[SignatureConstants.Parts.CONTENTS] = contents
    matchmaker[SignatureConstants.Parts.EXTENSION] = extension
    matchmaker[SignatureConstants.Parts.FILENAME] = filename
    matchmaker[SignatureConstants.Parts.PATH] = path

    match_fxn = matchmaker.get(signature.part)
    return match_fxn(data, signature)

def path(filepath, signature):
    """
    Match by path.
    """

    violation = None

    # filepath = os.path.join(subdir, file_name)
    if by_type(filepath, signature):
        violation = Violation.factory(filepath, signature)
    return violation
