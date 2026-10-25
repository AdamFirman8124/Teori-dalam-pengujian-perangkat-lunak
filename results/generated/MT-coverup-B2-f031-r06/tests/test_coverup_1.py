# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two():
    """Covers lines 3-4: n < 2 returns False."""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False


def test_is_prime_composite():
    """Covers lines 5-7: loop finds a divisor and returns False."""
    assert is_prime(4) is False
    assert is_prime(9) is False
    assert is_prime(15) is False


def test_is_prime_prime():
    """Covers line 8: no divisor found, returns True."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(13) is True
