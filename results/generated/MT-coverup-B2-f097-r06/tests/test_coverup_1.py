# file: project/f097/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f097 import multiply


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-3, -4) == 42


def test_multiply_mixed_signs():
    assert multiply(-3, 4) == 28


def test_multiply_large_numbers():
    assert multiply(123, 456) == 18


def test_multiply_zero():
    assert multiply(0, 5) == 0
