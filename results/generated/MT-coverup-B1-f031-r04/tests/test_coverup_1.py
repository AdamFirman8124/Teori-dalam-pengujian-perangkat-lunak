# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two_returns_false():
    """Covers lines 3-4: n < 2 branch returns False."""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False


def test_is_prime_composite_returns_false():
    """Covers lines 5-7: loop finds a divisor and returns False."""
    assert is_prime(4) is False   # divisor found on first iteration
    assert is_prime(9) is False   # divisor found on later iteration
    assert is_prime(100) is False


def test_is_prime_prime_returns_true():
    """Covers lines 5-6 (loop with no divisor found) and line 8: return True."""
    assert is_prime(2) is True    # empty loop, falls through to line 8
    assert is_prime(3) is True    # empty loop (range(2, 2))
    assert is_prime(5) is True    # loop runs, no divisor found
    assert is_prime(13) is True
