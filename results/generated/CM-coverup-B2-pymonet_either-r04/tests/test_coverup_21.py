# file: project/pymonet/either.py:182-187
# asked: {"lines": [187], "branches": []}
# gained: {"lines": [187], "branches": []}

from pymonet.either import Right


def test_right_is_left_returns_false():
    assert Right(42).is_left() is False


def test_right_is_left_returns_false_other_values():
    assert Right(None).is_left() is False
    assert Right("value").is_left() is False
    assert Right(0).is_left() is False
