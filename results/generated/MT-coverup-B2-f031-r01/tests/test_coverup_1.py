# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f031 import is_prime


def test_is_prime_less_than_two():
    """Covers line 3 (True branch) and line 4."""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False


def test_is_prime_small_primes_empty_loop():
    """Covers line 3 (False branch), line 5 with empty range, and line 8."""
    assert is_prime(2) is True
    assert is_prime(3) is True


def test_is_prime_composite_first_divisor():
    """Covers lines 5-7: loop entered and n % k == 0 branch taken immediately."""
    assert is_prime(4) is False
    assert is_prime(6) is False


def test_is_prime_composite_later_divisor():
    """Covers the False branch of line 6 (loop continues) followed by line 7."""
    assert is_prime(9) is False
    assert is_prime(15) is False


def test_is_prime_prime_after_full_loop():
    """Covers line 8 reached after non-empty loop iterations (line 6 False branch)."""
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(13) is True
