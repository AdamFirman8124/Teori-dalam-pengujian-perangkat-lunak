# file: project/pymonet/either.py:113-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from pymonet.either import Left, Right


def test_left_is_left_returns_true():
    left = Left(42)

    assert left.is_left() is True
    assert left.value == 42


def test_left_is_left_does_not_mutate_value():
    left = Left('error')

    assert left.is_left() is True
    assert left.is_left() is True
    assert left.value == 'error'


def test_left_is_left_differs_from_right_is_left():
    left = Left(1)
    right = Right(1)

    assert left.is_left() is True
    assert right.is_left() is False
