# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two_returns_false():
    """Covers lines 3-4: n < 2 branch returns False."""
    for n in (-7, -1, 0, 1):
        assert is_prime(n) is False


def test_is_prime_composite_returns_false():
    """Covers lines 5-7: loop finds a divisor and returns False."""
    assert is_prime(4) is False   # divisor found on first iteration
    assert is_prime(9) is False   # divisor found after several iterations
    assert is_prime(100) is False


def test_is_prime_prime_returns_true():
    """Covers line 8: loop completes without finding a divisor."""
    assert is_prime(2) is True    # empty range, straight to return True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(13) is True
    assert is_prime(97) is True
