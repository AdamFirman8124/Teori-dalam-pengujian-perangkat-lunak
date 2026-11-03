# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two_returns_false():
    """Covers lines 3-4: n < 2 branch."""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-3) is False


def test_is_prime_composite_returns_false():
    """Covers lines 5-7: loop finds a divisor and returns False."""
    assert is_prime(4) is False   # k=2 divides 4
    assert is_prime(9) is False   # k=3 divides 9
    assert is_prime(15) is False  # k=3 divides 15


def test_is_prime_returns_true():
    """Covers line 8: loop completes (or is empty) without finding a divisor."""
    assert is_prime(2) is True    # range(2, 1) is empty, falls through to line 8
    assert is_prime(3) is True    # range(2, 2) is empty
    assert is_prime(5) is True    # loop runs but no divisor found
    assert is_prime(7) is True
