# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length_two_returns_yes():
    """Covers is_prime num == 2 branch and the 'YES' return (lines 6-7, 16-17)."""
    # Overlap is [2, 4], length = 2, which is prime.
    assert intersection((2, 4), (2, 4)) == "YES"


def test_intersection_prime_length_three_returns_yes():
    """Covers is_prime loop completing without finding a divisor (lines 8-11)."""
    # Overlap is [2, 5], length = 3, prime verified via the loop.
    assert intersection((1, 5), (2, 6)) == "YES"


def test_intersection_composite_length_returns_no():
    """Covers is_prime loop finding a divisor and returning False (lines 9-10)."""
    # Overlap is [2, 6], length = 4, composite (divisible by 2).
    assert intersection((1, 6), (2, 7)) == "NO"


def test_intersection_length_one_returns_no():
    """Covers is_prime num == 1 branch (lines 4-5) and the final 'NO' return (line 18)."""
    # Overlap is [2, 3], length = 1, not prime.
    assert intersection((1, 3), (2, 4)) == "NO"


def test_intersection_zero_length_returns_no():
    """Covers the short-circuit when length == 0 (line 16 condition False)."""
    # Intervals touch at a single point: length = 0.
    assert intersection((1, 2), (2, 3)) == "NO"


def test_intersection_negative_length_returns_no():
    """Covers the short-circuit when length < 0 (line 16 condition False)."""
    # Disjoint intervals: length = -1.
    assert intersection((1, 2), (3, 4)) == "NO"


def test_intersection_uses_max_start_and_min_end():
    """Verifies l = max(starts) and r = min(ends) regardless of argument order."""
    # Overlap is [3, 5], length = 2 (prime) -> "YES".
    assert intersection((3, 10), (1, 5)) == "YES"
    assert intersection((1, 5), (3, 10)) == "YES"
