# file: script_75.py:1-22
# asked: {"lines": [9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[10, 11], [10, 13], [11, 10], [11, 12], [15, 16], [15, 22], [16, 16], [16, 17], [17, 15], [17, 18], [18, 18], [18, 19], [19, 17], [19, 20], [20, 20], [20, 21], [21, 19], [21, 21]]}
# gained: {"lines": [9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[10, 11], [10, 13], [11, 10], [11, 12], [15, 16], [15, 22], [16, 16], [16, 17], [17, 15], [17, 18], [18, 18], [18, 19], [19, 17], [19, 20], [20, 20], [20, 21], [21, 19], [21, 21]]}

import pytest
from script_75 import is_multiply_prime


def test_is_multiply_prime_30():
    """Test that 30 is the product of 3 primes (2 * 3 * 5)"""
    assert is_multiply_prime(30) == True


def test_is_multiply_prime_8():
    """Test that 8 is the product of 3 primes (2 * 2 * 2)"""
    assert is_multiply_prime(8) == True


def test_is_multiply_prime_12():
    """Test that 12 is the product of 3 primes (2 * 2 * 3)"""
    assert is_multiply_prime(12) == True


def test_is_multiply_prime_50():
    """Test that 50 is the product of 3 primes (2 * 5 * 5)"""
    assert is_multiply_prime(50) == True


def test_is_multiply_prime_not_product_of_three():
    """Test that a number that is NOT the product of 3 primes returns False"""
    assert is_multiply_prime(10) == False  # 10 = 2 * 5 (only 2 primes)


def test_is_multiply_prime_prime_itself():
    """Test that a prime number itself is not the product of 3 primes"""
    assert is_multiply_prime(7) == False


def test_is_multiply_prime_1():
    """Test that 1 returns False"""
    assert is_multiply_prime(1) == False


def test_is_multiply_prime_2():
    """Test that 2 (a prime) returns False"""
    assert is_multiply_prime(2) == False


def test_is_multiply_prime_60():
    """Test that 60 returns False (product of 4 primes: 2 * 2 * 3 * 5)"""
    assert is_multiply_prime(60) == False


def test_is_multiply_prime_27():
    """Test that 27 is product of 3 primes (3 * 3 * 3)"""
    assert is_multiply_prime(27) == True


def test_is_multiply_prime_99():
    """Test that 99 is product of 3 primes (3 * 3 * 11)"""
    assert is_multiply_prime(99) == True


def test_is_multiply_prime_66():
    """Test that 66 is product of 3 primes (2 * 3 * 11)"""
    assert is_multiply_prime(66) == True
