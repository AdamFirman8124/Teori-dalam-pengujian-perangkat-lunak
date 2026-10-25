# file: project/pymonet/either.py:175-180
# asked: {"lines": [180], "branches": []}
# gained: {"lines": [180], "branches": []}

from pymonet.either import Right


def test_right_is_right_returns_true():
    instance = Right(42)
    result = instance.is_right()
    assert result is True
    assert result == True


def test_right_is_right_various_values():
    assert Right(None).is_right() is True
    assert Right("value").is_right() is True
    assert Right(0).is_right() is True
