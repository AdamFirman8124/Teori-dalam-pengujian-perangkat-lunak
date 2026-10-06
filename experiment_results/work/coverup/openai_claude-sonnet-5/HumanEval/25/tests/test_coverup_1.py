# file: script_25.py:4-27
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27], "branches": [[18, 19], [18, 25], [19, 20], [19, 23], [25, 26], [25, 27]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27], "branches": [[18, 19], [18, 25], [19, 20], [19, 23], [25, 26], [25, 27]]}

import pytest
from script_25 import factorize


def test_factorize_power_of_two():
    """Test factorization of a power of 2 (executes lines 15-23)"""
    result = factorize(8)
    assert result == [2, 2, 2]
    assert len(result) == 3


def test_factorize_perfect_square():
    """Test factorization of a perfect square (executes lines 15-23)"""
    result = factorize(25)
    assert result == [5, 5]
    assert len(result) == 2


def test_factorize_composite_with_distinct_primes():
    """Test factorization with multiple distinct prime factors (executes lines 15-27)"""
    result = factorize(70)
    assert result == [2, 5, 7]
    assert len(result) == 3


def test_factorize_prime_number():
    """Test factorization of a prime number (executes lines 15-27, especially line 25-26)"""
    result = factorize(13)
    assert result == [13]
    assert len(result) == 1


def test_factorize_large_prime():
    """Test factorization of a larger prime (executes lines 15-27, especially line 25-26)"""
    result = factorize(97)
    assert result == [97]
    assert len(result) == 1


def test_factorize_two():
    """Test factorization of 2 itself (executes lines 15-27)"""
    result = factorize(2)
    assert result == [2]
    assert len(result) == 1


def test_factorize_composite_with_large_prime_factor():
    """Test composite number with a large prime factor (executes line 25-26)"""
    result = factorize(14)
    assert result == [2, 7]
    assert len(result) == 2


def test_factorize_product_equals_input():
    """Test that the product of factors equals the input"""
    n = 100
    result = factorize(n)
    product = 1
    for factor in result:
        product *= factor
    assert product == n
    assert result == [2, 2, 5, 5]
