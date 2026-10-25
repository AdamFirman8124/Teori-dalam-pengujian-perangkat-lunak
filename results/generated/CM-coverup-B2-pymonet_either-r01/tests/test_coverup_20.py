# file: project/pymonet/either.py:175-180
# asked: {"lines": [180], "branches": []}
# gained: {"lines": [180], "branches": []}

from pymonet.either import Right


def test_right_is_right_returns_true():
    right = Right(42)

    assert right.is_right() is True
    assert right.value == 42


def test_right_is_right_returns_true_for_falsy_value():
    right = Right(None)

    assert right.is_right() is True
    assert right.value is None
