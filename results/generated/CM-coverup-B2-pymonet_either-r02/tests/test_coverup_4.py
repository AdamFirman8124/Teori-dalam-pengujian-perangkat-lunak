# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

from pymonet.either import Left, Right
from pymonet.monad_try import Try


def test_left_to_try_returns_failed_try():
    value = "failure"

    result = Left(value).to_try()

    assert isinstance(result, Try)
    assert result.value == value
    assert result.is_success is False
    assert result == Try(value, is_success=False)


def test_right_to_try_returns_successful_try():
    value = "success"

    result = Right(value).to_try()

    assert isinstance(result, Try)
    assert result.value == value
    assert result.is_success is True
    assert result == Try(value, is_success=True)
