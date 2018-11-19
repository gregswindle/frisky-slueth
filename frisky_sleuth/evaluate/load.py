"""
Load the data-leakage signatures.
"""

import json
import os
from pathlib import Path
from ..constants import SignatureConstants
from ..signature import Signature
from . import validate

def __filepath(params=SignatureConstants.Files.PATH_PARAMS):
    filepath = os.path.join(params['subdir'], params['filename'])

    return os.path.join(Path.cwd(), filepath)

def contents(params=SignatureConstants.Files.PATH_PARAMS):
    """
    docstring here
        :param subdir:
        :param file_name:
    """
    file_data = ''

    try:
        with open(__filepath(params), 'r') as content_file:
            file_data = content_file.readlines()
    except IOError as io_err:
        raise io_err

    return file_data

def data(params, signature):
    """
    Return data to be evaluate by signature.part.
        :param data: The resource part to be evaluated.
        :param signature: A signature that defines a type of evaluation.
        :return data: The data to be evaluated.
    """
    validate.single(signature)

    subject = ''

    loader = {}
    loader[SignatureConstants.Parts.CONTENTS] = contents
    loader[SignatureConstants.Parts.EXTENSION] = extension
    loader[SignatureConstants.Parts.FILENAME] = filename
    loader[SignatureConstants.Parts.PATH] = path

    load_fxn = loader.get(signature.part)
    subject = load_fxn(params)

    return subject

def extension(params=SignatureConstants.Files.PATH_PARAMS):
    """
    docstring here
        :param file_name:
    """

    return os.path.splitext(params.get('filename'))[1][1:]

def filename(params=SignatureConstants.Files.PATH_PARAMS):
    """
    docstring here
        :param file_name:
    """
    return params.get('filename')

def path(params=SignatureConstants.Files.PATH_PARAMS):
    """
    docstring here
        :param subdir:
        :param file_name:
    """
    return os.path.join(params.get('subdir'), params.get('filename'))

def signatures(params=SignatureConstants.PATH_PARAMS):
    """
    Load signatures from file.
      :param subdir:
      :param file_name='signatures.json':
    """
    signature_definitions = []
    try:
        with open(__filepath(params), 'r') as signatures_file:
            signature_definitions = Signature.from_list(json.load(signatures_file))
            validate.every(signature_definitions)
    except IOError as io_err:
        raise io_err

    return signature_definitions
