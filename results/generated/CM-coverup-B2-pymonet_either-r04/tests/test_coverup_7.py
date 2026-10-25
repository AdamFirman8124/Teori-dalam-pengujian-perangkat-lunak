# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation_with_value_as_error():
    left = Left("error_value")

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.is_fail()
    assert validation.value is None
    assert validation.errors == ["error_value"]
    assert validation == Validation.fail(["error_value"])
