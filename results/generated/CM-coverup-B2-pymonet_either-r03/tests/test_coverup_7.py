# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failure_with_left_value_as_error():
    result = Left("error").to_validation()

    assert isinstance(result, Validation)
    assert result.is_fail()
    assert not result.is_success()
    assert result.value is None
    assert result.errors == ["error"]
