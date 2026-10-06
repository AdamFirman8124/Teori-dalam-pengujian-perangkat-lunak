# file: script_31.py:1-23
# asked: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22]]}
# gained: {"lines": [18, 19, 20, 21, 22, 23], "branches": [[18, 19], [18, 20], [20, 21], [20, 23], [21, 20], [21, 22]]}

import pytest
from script_31 import is_prime


def test_is_prime_less_than_2():
    """Test that numbers less than 2 return False."""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False


def test_is_prime_small_primes():
    """Test small prime numbers."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True


def test_is_prime_small_composites():
    """Test small composite numbers."""
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(10) is False


def test_is_prime_larger_composites():
    """Test larger composite numbers to exercise the loop."""
    assert is_prime(15) is False  # 15 = 3 * 5
    assert is_prime(21) is False  # 21 = 3 * 7
    assert is_prime(25) is False  # 25 = 5 * 5


def test_is_prime_larger_primes():
    """Test larger prime numbers."""
    assert is_prime(11) is True
    assert is_prime(13) is True
    assert is_prime(17) is True
    assert is_prime(19) is True
    assert is_prime(23) is True
