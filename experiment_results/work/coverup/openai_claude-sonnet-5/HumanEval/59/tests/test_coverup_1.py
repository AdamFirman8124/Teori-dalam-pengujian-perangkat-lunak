# file: script_59.py:1-19
# asked: {"lines": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[9, 10], [9, 11], [11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 19], [17, 16], [17, 18]]}
# gained: {"lines": [8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[9, 11], [11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 19], [17, 16], [17, 18]]}

import pytest
from script_59 import largest_prime_factor


def test_largest_prime_factor_composite_number():
    """Test largest prime factor of a composite number."""
    result = largest_prime_factor(15)
    assert result == 5


def test_largest_prime_factor_13195():
    """Test the example from docstring."""
    result = largest_prime_factor(13195)
    assert result == 29


def test_largest_prime_factor_2048():
    """Test power of 2 from docstring."""
    result = largest_prime_factor(2048)
    assert result == 2


def test_largest_prime_factor_small_composite():
    """Test smallest composite number."""
    result = largest_prime_factor(4)
    assert result == 2


def test_largest_prime_factor_product_of_primes():
    """Test product of two primes."""
    result = largest_prime_factor(21)
    assert result == 7


def test_largest_prime_factor_larger_number():
    """Test with a larger composite number."""
    result = largest_prime_factor(30)
    assert result == 5
