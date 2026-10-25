# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

from pymonet.either import Left, Right
from pymonet.monad_try import Try


def test_right_to_try_returns_successful_try():
    right = Right(42)
    result = right.to_try()
    assert isinstance(result, Try)
    assert result.is_success is True
    assert result.value == 42
    assert result == Try(42, is_success=True)
    # original Either unchanged
    assert right.value == 42
    assert right.is_right() is True


def test_left_to_try_returns_failed_try():
    left = Left("error")
    result = left.to_try()
    assert isinstance(result, Try)
    assert result.is_success is False
    assert result.value == "error"
    assert result == Try("error", is_success=False)
    # original Either unchanged
    assert left.value == "error"
    assert left.is_right() is False
