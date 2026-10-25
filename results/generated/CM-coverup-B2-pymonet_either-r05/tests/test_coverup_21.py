# file: project/pymonet/either.py:182-187
# asked: {"lines": [187], "branches": []}
# gained: {"lines": [187], "branches": []}

from pymonet.either import Right


def test_right_is_left_returns_false():
    right = Right(object())

    assert right.is_left() is False
