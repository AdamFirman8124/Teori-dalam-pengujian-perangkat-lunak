# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f097 import multiply


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    # In Python, -3 % 10 == 7 and -4 % 10 == 6, so result is 7 * 6 == 42
    assert multiply(-3, -4) == 42


def test_multiply_mixed_signs():
    # -3 % 10 == 7, 4 % 10 == 4, so result is 7 * 4 == 28
    assert multiply(-3, 4) == 28


def test_multiply_large_numbers():
    # 123 % 10 == 3, 456 % 10 == 6, so result is 3 * 6 == 18
    assert multiply(123, 456) == 18


def test_multiply_zero():
    assert multiply(0, 5) == 0
