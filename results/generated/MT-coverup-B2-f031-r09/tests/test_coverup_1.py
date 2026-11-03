# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two_returns_false():
    """Lines 3-4: n < 2 must return False."""
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False


def test_is_prime_composite_returns_false():
    """Lines 5-7: a composite number must be detected via n % k == 0."""
    assert is_prime(4) is False   # divisible by 2
    assert is_prime(9) is False   # divisible by 3
    assert is_prime(15) is False  # divisible by 3 and 5


def test_is_prime_prime_returns_true():
    """Line 8: a prime number must fall through the loop and return True."""
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(13) is True


def test_is_prime_smallest_primes():
    """Edge cases: range(2, n-1) is empty for n == 2 and n == 3."""
    assert is_prime(2) is True
    assert is_prime(3) is True
