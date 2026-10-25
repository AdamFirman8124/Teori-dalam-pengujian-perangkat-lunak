# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f097 import multiply


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    # Python: -3 % 10 == 7, -4 % 10 == 6
    assert multiply(-3, -4) == 42


def test_multiply_mixed_signs():
    # Python: -3 % 10 == 7
    assert multiply(-3, 4) == 28


def test_multiply_large_values_uses_last_digit():
    assert multiply(17, 23) == 21


def test_multiply_zero():
    assert multiply(0, 5) == 0
