# file: script_138.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_138 import is_equal_to_sum_even


def test_is_equal_to_sum_even_with_4():
    """Test that 4 cannot be written as sum of 4 positive even numbers."""
    assert is_equal_to_sum_even(4) == False


def test_is_equal_to_sum_even_with_6():
    """Test that 6 cannot be written as sum of 4 positive even numbers."""
    assert is_equal_to_sum_even(6) == False


def test_is_equal_to_sum_even_with_8():
    """Test that 8 can be written as sum of 4 positive even numbers (2+2+2+2)."""
    assert is_equal_to_sum_even(8) == True


def test_is_equal_to_sum_even_with_10():
    """Test that 10 can be written as sum of 4 positive even numbers (2+2+2+4)."""
    assert is_equal_to_sum_even(10) == True


def test_is_equal_to_sum_even_with_12():
    """Test that 12 can be written as sum of 4 positive even numbers (2+2+4+4)."""
    assert is_equal_to_sum_even(12) == True


def test_is_equal_to_sum_even_with_odd_number():
    """Test that odd numbers return False."""
    assert is_equal_to_sum_even(7) == False
    assert is_equal_to_sum_even(9) == False
    assert is_equal_to_sum_even(11) == False


def test_is_equal_to_sum_even_with_negative():
    """Test that negative numbers return False."""
    assert is_equal_to_sum_even(-2) == False
    assert is_equal_to_sum_even(-8) == False


def test_is_equal_to_sum_even_with_zero():
    """Test that zero returns False."""
    assert is_equal_to_sum_even(0) == False


def test_is_equal_to_sum_even_with_two():
    """Test that 2 returns False."""
    assert is_equal_to_sum_even(2) == False
