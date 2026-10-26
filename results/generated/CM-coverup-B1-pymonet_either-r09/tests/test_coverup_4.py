# file: project/pymonet/either.py:59-68
# asked: {"lines": [66, 68], "branches": []}
# gained: {"lines": [66, 68], "branches": []}

import pytest

from pymonet.either import Either, Right, Left
from pymonet.monad_try import Try


def test_to_try_right_returns_successful_try():
    """Either.to_try on a Right must yield a successful Try holding the value."""
    either = Right(42)

    result = either.to_try()

    assert isinstance(result, Try)
    assert result.is_success is True
    assert result.get() == 42


def test_to_try_left_returns_failed_try():
    """Either.to_try on a Left must yield a failed Try holding the value."""
    either = Left("boom")

    result = either.to_try()

    assert isinstance(result, Try)
    assert result.is_success is False
    assert result.get() == "boom"
