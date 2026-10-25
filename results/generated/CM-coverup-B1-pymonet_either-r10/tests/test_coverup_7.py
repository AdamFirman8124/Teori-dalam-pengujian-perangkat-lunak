# file: project/pymonet/either.py:138-147
# asked: {"lines": [145, 147], "branches": []}
# gained: {"lines": [145, 147], "branches": []}

from pymonet.either import Left
from pymonet.validation import Validation


def test_left_to_validation_returns_failed_validation_with_value_as_error():
    left = Left(42)

    validation = left.to_validation()

    assert isinstance(validation, Validation)
    assert validation.is_fail() is True
    assert validation.errors == [42]


def test_left_to_validation_wraps_value_in_single_element_list():
    left = Left('error message')

    validation = left.to_validation()

    assert validation.errors == ['error message']
    assert len(validation.errors) == 1
    assert validation.errors[0] == 'error message'


def test_left_to_validation_does_not_share_errors_list_between_calls():
    first = Left(1).to_validation()
    second = Left(2).to_validation()

    assert first.errors == [1]
    assert second.errors == [2]
    assert first.errors is not second.errors

    first.errors.append('polluted')

    assert Left(3).to_validation().errors == [3]
    assert second.errors == [2]
