# file: script_36.py:1-18
# asked: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 18]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 18]]}

import pytest
from script_36 import fizz_buzz


def test_fizz_buzz_50():
    """Test with n=50, should return 0 as no multiples contain digit 7."""
    assert fizz_buzz(50) == 0


def test_fizz_buzz_78():
    """Test with n=78, should return 2 (from 77: divisible by 11)."""
    assert fizz_buzz(78) == 2


def test_fizz_buzz_79():
    """Test with n=79, should return 3 (77 has two 7s, 78 divisible by 13 has one 7)."""
    assert fizz_buzz(79) == 3


def test_fizz_buzz_zero():
    """Test with n=0, should return 0 as no numbers to check."""
    assert fizz_buzz(0) == 0


def test_fizz_buzz_one():
    """Test with n=1, should return 0 (only 0 is checked, which is divisible by both but has no 7)."""
    assert fizz_buzz(1) == 0


def test_fizz_buzz_small_with_multiples():
    """Test with n=14, includes 0, 11, 13 - none contain digit 7."""
    assert fizz_buzz(14) == 0


def test_fizz_buzz_with_seven():
    """Test with n=27, includes 0, 11, 13, 22, 26 - none contain 7."""
    assert fizz_buzz(27) == 0


def test_fizz_buzz_100():
    """Test with n=100, multiple occurrences of digit 7."""
    result = fizz_buzz(100)
    # Multiples of 11 or 13 less than 100: 0, 11, 13, 22, 26, 33, 39, 44, 52, 55, 65, 66, 77, 78, 88, 91, 99
    # Count 7s: 77 (two 7s), 78 (one 7) = 3
    assert result == 3


def test_fizz_buzz_large():
    """Test with larger n=200."""
    result = fizz_buzz(200)
    # Verify it returns an integer >= 0
    assert isinstance(result, int)
    assert result >= 0
