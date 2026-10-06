# file: script_59.py:1-19
# asked: {"lines": [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[9, 10], [9, 11], [11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 19], [17, 16], [17, 18]]}
# gained: {"lines": [8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19], "branches": [[9, 11], [11, 12], [11, 14], [12, 11], [12, 13], [16, 17], [16, 19], [17, 16], [17, 18]]}

import pytest
from script_59 import largest_prime_factor


def test_largest_prime_factor_13195():
    """Test largest prime factor of 13195."""
    result = largest_prime_factor(13195)
    assert result == 29


def test_largest_prime_factor_2048():
    """Test largest prime factor of 2048."""
    result = largest_prime_factor(2048)
    assert result == 2


def test_largest_prime_factor_small_composite():
    """Test largest prime factor of a small composite number."""
    result = largest_prime_factor(15)
    assert result == 5


def test_largest_prime_factor_with_multiple_primes():
    """Test largest prime factor with multiple prime factors."""
    result = largest_prime_factor(30)  # 2 * 3 * 5
    assert result == 5


def test_largest_prime_factor_even_number():
    """Test largest prime factor of an even composite number."""
    result = largest_prime_factor(100)  # 2^2 * 5^2
    assert result == 5


def test_largest_prime_factor_square_of_prime():
    """Test largest prime factor of a square of a prime."""
    result = largest_prime_factor(49)  # 7 * 7
    assert result == 7


def test_largest_prime_factor_product_of_two_primes():
    """Test largest prime factor of product of two primes."""
    result = largest_prime_factor(21)  # 3 * 7
    assert result == 7
