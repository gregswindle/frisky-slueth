"""
Evaluate a file for secrets.
"""

from . import load
from .match import matches
from ..constants import SignatureConstants
from ..violation import Violation


def evaluate(params=SignatureConstants.Files.PATH_PARAMS, options=SignatureConstants.PATH_PARAMS):
    """
    Evalutate files for secrets.
      :param subdir:
      :param filename:
    """

    signatures = load.signatures(options)

    results = None
    violations = []

    for signature in signatures:

        data = load.data(params, signature)

        if matches(data, signature):
            violations.append(Violation.factory(violations, signature))
            results = violations

    return results
