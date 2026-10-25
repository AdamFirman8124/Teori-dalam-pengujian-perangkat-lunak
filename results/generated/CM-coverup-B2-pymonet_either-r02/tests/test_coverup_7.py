# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failure_containing_error():
    error = object()

    result = Left(error).to_validation()

    assert result == Validation.fail([error])
