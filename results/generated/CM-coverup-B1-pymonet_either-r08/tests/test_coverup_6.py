# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    left = Left('some error')

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert result == Maybe.nothing()


def test_left_to_maybe_does_not_mutate_left():
    left = Left(42)

    first = left.to_maybe()
    second = left.to_maybe()

    assert first.is_nothing is True
    assert second.is_nothing is True
    assert first == Maybe.nothing()
    assert second == Maybe.nothing()


@pytest.mark.parametrize('value', [None, 0, '', [], {'a': 1}])
def test_left_to_maybe_returns_nothing_for_any_value(value):
    result = Left(value).to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert result == Maybe.nothing()
