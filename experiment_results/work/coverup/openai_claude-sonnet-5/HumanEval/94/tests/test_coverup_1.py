# file: script_94.py:1-26
# asked: {"lines": [13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26], "branches": [[14, 15], [14, 18], [15, 14], [15, 16], [21, 22], [21, 25], [22, 23], [22, 24]]}
# gained: {"lines": [13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26], "branches": [[14, 15], [14, 18], [15, 14], [15, 16], [21, 22], [21, 25], [22, 23], [22, 24]]}

import pytest
from script_94 import skjkasdkd


def test_skjkasdkd_with_prime_numbers():
    """Test with a list containing prime numbers."""
    result = skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
    assert result == 10


def test_skjkasdkd_with_larger_prime():
    """Test with a list containing a larger prime number."""
    result = skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
    assert result == 25


def test_skjkasdkd_with_very_large_prime():
    """Test with a list containing very large prime number."""
    result = skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
    assert result == 13


def test_skjkasdkd_with_two_digit_prime():
    """Test with a list containing two-digit primes."""
    result = skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6])
    assert result == 11


def test_skjkasdkd_with_small_primes():
    """Test with a list containing small primes."""
    result = skjkasdkd([0, 81, 12, 3, 1, 21])
    assert result == 3


def test_skjkasdkd_with_single_digit_prime():
    """Test with a list where the largest prime is single digit."""
    result = skjkasdkd([0, 8, 1, 2, 1, 7])
    assert result == 7


def test_skjkasdkd_empty_list():
    """Test with an empty list."""
    result = skjkasdkd([])
    assert result == 0


def test_skjkasdkd_no_primes():
    """Test with a list containing no primes (note: 0 and 1 are not prime, but isPrime(1) returns True)."""
    result = skjkasdkd([0, 4, 6, 8, 9, 10])
    assert result == 0


def test_skjkasdkd_only_two():
    """Test with a list where 2 is the only and largest prime."""
    result = skjkasdkd([2])
    assert result == 2


def test_skjkasdkd_composite_numbers():
    """Test with a list of composite numbers and small primes."""
    result = skjkasdkd([4, 6, 8, 9, 10, 12, 15, 3])
    assert result == 3


def test_skjkasdkd_with_one():
    """Test that 1 is treated as prime by the isPrime function."""
    result = skjkasdkd([0, 1])
    assert result == 1
