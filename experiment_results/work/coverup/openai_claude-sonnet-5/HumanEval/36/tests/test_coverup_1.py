# file: script_36.py:1-18
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 18]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 18]]}

import pytest
from script_36 import fizz_buzz


def test_fizz_buzz_50():
    """Test fizz_buzz with n=50, should return 0 (no 7s in divisible numbers)."""
    result = fizz_buzz(50)
    assert result == 0


def test_fizz_buzz_78():
    """Test fizz_buzz with n=78, should return 2 (77 contains two 7s)."""
    result = fizz_buzz(78)
    assert result == 2


def test_fizz_buzz_79():
    """Test fizz_buzz with n=79, should return 3 (77 has two 7s, 78 has one 7)."""
    result = fizz_buzz(79)
    assert result == 3


def test_fizz_buzz_zero():
    """Test fizz_buzz with n=0, should return 0 (no numbers to check)."""
    result = fizz_buzz(0)
    assert result == 0


def test_fizz_buzz_small():
    """Test fizz_buzz with n=15, should return 0 (0, 11, 13 have no 7s)."""
    result = fizz_buzz(15)
    assert result == 0


def test_fizz_buzz_with_seven():
    """Test fizz_buzz with n=8, should return 1 (0 is divisible by both, no 7 yet)."""
    result = fizz_buzz(8)
    assert result == 0
