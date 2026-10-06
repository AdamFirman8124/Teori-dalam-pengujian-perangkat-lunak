# file: script_24.py:1-8
# asked: {"lines": [6, 7, 8], "branches": [[6, 0], [6, 7], [7, 6], [7, 8]]}
# gained: {"lines": [6, 7, 8], "branches": [[6, 7], [7, 6], [7, 8]]}

import pytest
from script_24 import largest_divisor


def test_largest_divisor_15():
    """Test largest divisor of 15 is 5"""
    assert largest_divisor(15) == 5


def test_largest_divisor_prime():
    """Test largest divisor of a prime number"""
    assert largest_divisor(7) == 1


def test_largest_divisor_even():
    """Test largest divisor of an even number"""
    assert largest_divisor(10) == 5


def test_largest_divisor_perfect_square():
    """Test largest divisor of a perfect square"""
    assert largest_divisor(16) == 8


def test_largest_divisor_2():
    """Test largest divisor of 2"""
    assert largest_divisor(2) == 1


def test_largest_divisor_3():
    """Test largest divisor of 3"""
    assert largest_divisor(3) == 1
