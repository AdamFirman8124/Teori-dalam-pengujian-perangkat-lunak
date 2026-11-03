# file: project/f053/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f053 import add


def test_add_positive_integers():
    """Exercise line 3 (return x + y) with two positive integers."""
    result = add(2, 3)
    assert result == 5


def test_add_zero():
    """Exercise line 3 with a zero operand."""
    assert add(0, 0) == 0
    assert add(0, 7) == 7


def test_add_negative_integers():
    """Exercise line 3 with negative integers."""
    assert add(-1, -2) == -3
    assert add(-1, 2) == 1
