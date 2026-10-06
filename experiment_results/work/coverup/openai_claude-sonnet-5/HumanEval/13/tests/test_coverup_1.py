# file: script_13.py:1-10
# asked: {"lines": [8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [8, 9, 10], "branches": [[8, 9], [8, 10]]}

import pytest
from script_13 import greatest_common_divisor


def test_greatest_common_divisor_coprime():
    """Test GCD of two coprime numbers."""
    assert greatest_common_divisor(3, 5) == 1


def test_greatest_common_divisor_with_common_factor():
    """Test GCD of two numbers with a common factor."""
    assert greatest_common_divisor(25, 15) == 5


def test_greatest_common_divisor_zero_b():
    """Test GCD when b is zero (base case, while loop doesn't execute)."""
    assert greatest_common_divisor(10, 0) == 10


def test_greatest_common_divisor_zero_a():
    """Test GCD when a is zero."""
    assert greatest_common_divisor(0, 10) == 10


def test_greatest_common_divisor_both_zero():
    """Test GCD when both are zero."""
    assert greatest_common_divisor(0, 0) == 0


def test_greatest_common_divisor_same_numbers():
    """Test GCD of identical numbers."""
    assert greatest_common_divisor(7, 7) == 7


def test_greatest_common_divisor_large_numbers():
    """Test GCD with large numbers."""
    assert greatest_common_divisor(48, 18) == 6


def test_greatest_common_divisor_one_divides_other():
    """Test GCD when one number divides the other."""
    assert greatest_common_divisor(100, 10) == 10
