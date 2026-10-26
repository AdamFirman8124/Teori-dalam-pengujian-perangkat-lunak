# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    result = Left(42).to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert result == Maybe.nothing()


@pytest.mark.parametrize("value", [42, "error", None, 0, "", [1, 2, 3]])
def test_left_to_maybe_discards_left_value(value):
    result = Left(value).to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert result == Maybe.nothing()


def test_left_to_maybe_does_not_mutate_left_and_is_consistent():
    left = Left("error")

    first = left.to_maybe()
    second = Left("other error").to_maybe()

    assert left.value == "error"
    assert first.is_nothing is True
    assert second.is_nothing is True
    assert first == second == Maybe.nothing()
