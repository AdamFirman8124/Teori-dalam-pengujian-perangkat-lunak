# file: script_123.py:1-31
# asked: {"lines": [18, 19, 21, 22, 23, 24, 26, 28, 29, 31], "branches": [[18, 19], [18, 21], [22, 23], [22, 31], [23, 24], [23, 26], [28, 22], [28, 29]]}
# gained: {"lines": [18, 19, 21, 22, 23, 24, 26, 28, 29, 31], "branches": [[18, 19], [18, 21], [22, 23], [22, 31], [23, 24], [23, 26], [28, 22], [28, 29]]}

import pytest
from script_123 import get_odd_collatz


def test_get_odd_collatz_even_start():
    """Test with an even starting number to execute line 18-19 (if n%2==0 branch)."""
    result = get_odd_collatz(4)
    # Collatz sequence for 4: [4, 2, 1]
    # Odd numbers: [1]
    assert result == [1]


def test_get_odd_collatz_odd_start():
    """Test with an odd starting number to execute line 21 (else branch)."""
    result = get_odd_collatz(5)
    # Collatz sequence for 5: [5, 16, 8, 4, 2, 1]
    # Odd numbers: [5, 1]
    assert result == [1, 5]


def test_get_odd_collatz_even_division():
    """Test that executes line 24 (n = n/2 for even n in while loop)."""
    result = get_odd_collatz(8)
    # Collatz sequence for 8: [8, 4, 2, 1]
    # Odd numbers: [1]
    assert result == [1]


def test_get_odd_collatz_odd_multiplication():
    """Test that executes line 26 (n = n*3 + 1 for odd n in while loop)."""
    result = get_odd_collatz(3)
    # Collatz sequence for 3: [3, 10, 5, 16, 8, 4, 2, 1]
    # Odd numbers: [3, 5, 1]
    assert result == [1, 3, 5]


def test_get_odd_collatz_append_odd():
    """Test that executes line 28-29 (appending odd numbers during iteration)."""
    result = get_odd_collatz(7)
    # Collatz sequence for 7: [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    # Odd numbers: [7, 11, 17, 13, 5, 1]
    assert result == [1, 5, 7, 11, 13, 17]


def test_get_odd_collatz_sorted_output():
    """Test that the return statement on line 31 returns sorted list."""
    result = get_odd_collatz(9)
    # Collatz sequence for 9: [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    # Odd numbers: [9, 7, 11, 17, 13, 5, 1]
    assert result == sorted(result)
    assert result == [1, 5, 7, 9, 11, 13, 17]


def test_get_odd_collatz_one():
    """Test with n=1 (edge case)."""
    result = get_odd_collatz(1)
    # Collatz sequence for 1: [1]
    # Odd numbers: [1]
    assert result == [1]
