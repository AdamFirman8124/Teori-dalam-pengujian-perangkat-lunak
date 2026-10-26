# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_uses_absolute_remainders():
    assert multiply(12, 23) == 6
    assert multiply(-12, 23) == 24
    assert multiply(12, -23) == 14
    assert multiply(-12, -23) == 56


def test_multiply_returns_zero_when_either_remainder_is_zero():
    assert multiply(20, 37) == 0
    assert multiply(42, 0) == 0
