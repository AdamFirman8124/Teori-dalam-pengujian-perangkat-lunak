# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

from pymonet.either import Left, Right
from pymonet.monad_try import Try


def test_right_to_try_creates_successful_try():
    either = Right("value")

    result = either.to_try()

    assert isinstance(result, Try)
    assert result.value == "value"
    assert result.is_success is True


def test_left_to_try_creates_failed_try():
    either = Left("error")

    result = either.to_try()

    assert isinstance(result, Try)
    assert result.value == "error"
    assert result.is_success is False
