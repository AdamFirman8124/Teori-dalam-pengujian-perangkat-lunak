# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length_greater_than_two_returns_yes():
    # Overlap is (2, 5) -> length 3, prime found by completing the loop.
    assert intersection((1, 6), (2, 5)) == "YES"


def test_intersection_length_two_returns_yes():
    # Overlap is (2, 4) -> length 2, the special-case prime.
    assert intersection((1, 5), (2, 4)) == "YES"


def test_intersection_length_one_returns_no():
    # Overlap is (2, 3) -> length 1, handled by the num == 1 branch.
    assert intersection((1, 3), (2, 4)) == "NO"


def test_intersection_zero_length_returns_no():
    # Intervals merely touch: length 0 short-circuits before is_prime.
    assert intersection((1, 2), (2, 3)) == "NO"


def test_intersection_negative_length_returns_no():
    # Disjoint intervals: negative length, non-positive branch of the guard.
    assert intersection((3, 4), (1, 2)) == "NO"


def test_intersection_composite_length_returns_no():
    # Overlap is (2, 8) -> length 6, composite: loop finds divisor 2.
    assert intersection((1, 10), (2, 8)) == "NO"
