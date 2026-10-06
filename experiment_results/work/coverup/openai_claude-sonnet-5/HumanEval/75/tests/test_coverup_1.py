# file: script_75.py:1-22
# asked: {"lines": [9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[10, 11], [10, 13], [11, 10], [11, 12], [15, 16], [15, 22], [16, 16], [16, 17], [17, 15], [17, 18], [18, 18], [18, 19], [19, 17], [19, 20], [20, 20], [20, 21], [21, 19], [21, 21]]}
# gained: {"lines": [9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[10, 11], [10, 13], [11, 10], [11, 12], [15, 16], [15, 22], [16, 16], [16, 17], [17, 15], [17, 18], [18, 18], [18, 19], [19, 17], [19, 20], [20, 20], [20, 21], [21, 19], [21, 21]]}

import pytest
from script_75 import is_multiply_prime


def test_is_multiply_prime_30():
    """Test that 30 is the product of three primes (2 * 3 * 5)"""
    assert is_multiply_prime(30) == True


def test_is_multiply_prime_8():
    """Test that 8 is the product of three primes (2 * 2 * 2)"""
    assert is_multiply_prime(8) == True


def test_is_multiply_prime_125():
    """Test that 125 is the product of three primes (5 * 5 * 5)"""
    assert is_multiply_prime(125) == True


def test_is_multiply_prime_12():
    """Test that 12 is the product of three primes (2 * 2 * 3)"""
    assert is_multiply_prime(12) == True


def test_is_multiply_prime_50():
    """Test that 50 is the product of three primes (2 * 5 * 5)"""
    assert is_multiply_prime(50) == True


def test_is_multiply_prime_99():
    """Test that 99 is the product of three primes (3 * 3 * 11)"""
    assert is_multiply_prime(99) == True


def test_is_multiply_prime_1():
    """Test that 1 is not the product of three primes"""
    assert is_multiply_prime(1) == False


def test_is_multiply_prime_2():
    """Test that 2 is not the product of three primes"""
    assert is_multiply_prime(2) == False


def test_is_multiply_prime_4():
    """Test that 4 is not the product of three primes"""
    assert is_multiply_prime(4) == False


def test_is_multiply_prime_17():
    """Test that 17 is not the product of three primes"""
    assert is_multiply_prime(17) == False


def test_is_multiply_prime_100():
    """Test that 100 is not the product of three primes"""
    assert is_multiply_prime(100) == False
