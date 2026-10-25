# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

import pytest

from pymonet.either import Left


def test_left_to_maybe_returns_nothing():
    left = Left('some error')

    result = left.to_maybe()

    from pymonet.maybe import Maybe

    assert isinstance(result, Maybe)
    assert result.is_nothing is True


def test_left_to_maybe_does_not_mutate_left():
    left = Left(42)

    first = left.to_maybe()
    second = left.to_maybe()

    assert first.is_nothing is True
    assert second.is_nothing is True
    assert left.is_left() is True
    assert left.is_right() is False
    assert left.value == 42


@pytest.mark.parametrize('value', [None, 0, '', [], {'a': 1}])
def test_left_to_maybe_returns_nothing_for_any_value(value):
    result = Left(value).to_maybe()

    assert result.is_nothing is True
