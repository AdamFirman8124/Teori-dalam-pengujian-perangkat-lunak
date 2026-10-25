# file: project/pymonet/either.py:120-125
# asked: {"lines": [125], "branches": []}
# gained: {"lines": [125], "branches": []}

import pytest

from pymonet.either import Left, Right


def test_left_is_right_returns_false():
    left = Left(42)

    assert left.is_right() is False
    assert left.is_left() is True
    assert left.value == 42


def test_left_is_right_returns_false_for_none_value():
    left = Left(None)

    assert left.is_right() is False
    assert left.value is None


def test_left_is_right_returns_false_for_falsy_value():
    left = Left(0)

    assert left.is_right() is False
    assert left.value == 0


def test_left_is_right_contrasts_with_right_is_right():
    left = Left('error')
    right = Right('ok')

    assert left.is_right() is False
    assert right.is_right() is True
    assert left.is_left() is True
    assert right.is_left() is False


def test_left_is_right_does_not_mutate_value(monkeypatch):
    left = Left({'a': 1})
    original_value = left.value

    assert left.is_right() is False
    assert left.value is original_value
    assert left.value == {'a': 1}
