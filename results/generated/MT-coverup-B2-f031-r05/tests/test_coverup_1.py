# file: project/f031/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [5, 6], [5, 8], [6, 5], [6, 7]]}

"""Tests for f031.is_prime covering all previously unexecuted lines (3-8)."""

from f031 import is_prime


def test_is_prime_less_than_two_returns_false():
    """Exercises lines 3-4: the `n < 2` branch returns False."""
    for n in (-7, -1, 0, 1):
        assert is_prime(n) is False, f"is_prime({n}) should be False"


def test_is_prime_composite_returns_false():
    """Exercises lines 5-7: the loop finds a divisor and returns False."""
    for n in (4, 6, 9, 15, 100):
        assert is_prime(n) is False, f"is_prime({n}) should be False"


def test_is_prime_prime_returns_true():
    """Exercises lines 5 and 8: the loop completes without a divisor, returns True."""
    for n in (2, 3, 5, 7, 13, 97):
        assert is_prime(n) is True, f"is_prime({n}) should be True"


def test_is_prime_edge_cases():
    """Covers boundary behavior: 2 and 3 have empty ranges and are prime."""
    assert is_prime(2) is True   # range(2, 1) is empty -> line 8
    assert is_prime(3) is True   # range(2, 2) is empty -> line 8
    assert is_prime(4) is False  # range(2, 3) contains divisor 2 -> lines 6-7
