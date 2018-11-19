"""
frisky_sleuth.evaluate.validate
Validate signatures
"""

from ..constants import SignatureConstants

def by_part(signature):
    """
    docstring here
      :param signature:
    """

    valid = signature.part in SignatureConstants.Parts.VALUES

    return valid or throw_value_error(
        signature.part,
        SignatureConstants.Attributes.PART,
        SignatureConstants.Parts.VALUES
    )

def by_type(signature):
    """
    docstring here
      :param signature:
    """

    valid = signature.type in SignatureConstants.Types.VALUES

    return valid or throw_value_error(
        signature.type,
        SignatureConstants.Attributes.TYPE,
        SignatureConstants.Types.VALUES
    )

def every(signatures):
    """
    Checks validity of all signatures in a list.
    Iteration stops on the first invalid signature.
      :param signatures: A list of signatures.
      :return: True when all signatures are valid; otherwise, False.
    """
    result = True

    for signature in signatures:
        result = result and single(signature)
        if result is False:
            break

    return result

def single(signature):
    """
    docstring here
      :param signature: A single signature.
      :return: True if valid, False if invalid.
    """
    return by_type(signature) and by_part(signature)

def throw_value_error(value, attr, valid_values):
    """
    validate.throw_value_error
      :param value: The invalid value.
      :param attr: The attribute/key with the invalid value.
      :param valid_values: A list of valid values.
    """
    separator = '", "'
    msg = f"Invalid {attr} \"{value}\". Valid values are: \"{separator.join(valid_values)}\"."
    raise ValueError(msg)
