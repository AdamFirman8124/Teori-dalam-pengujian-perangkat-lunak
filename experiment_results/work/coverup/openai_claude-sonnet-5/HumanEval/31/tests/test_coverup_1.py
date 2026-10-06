# file: script_31.py:1-23
# asked: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22]]}
# gained: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22]]}

import pytest
from script_31 import is_prime


def test_is_prime_less_than_2():
    """Test that numbers less than 2 return False"""
    assert is_prime(0) == False
    assert is_prime(1) == False
    assert is_prime(-1) == False
    assert is_prime(-10) == False


def test_is_prime_2():
    """Test that 2 returns True (edge case: only one iteration in range)"""
    assert is_prime(2) == True


def test_is_prime_3():
    """Test that 3 returns True (edge case: range(2, 2) is empty)"""
    assert is_prime(3) == True


def test_is_prime_composite():
    """Test composite numbers return False"""
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(15) == False


def test_is_prime_primes():
    """Test prime numbers return True"""
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(17) == True
    assert is_prime(19) == True
