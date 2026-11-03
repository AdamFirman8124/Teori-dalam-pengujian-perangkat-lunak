# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_non_overlapping_intervals_returns_no():
    """length <= 0 short-circuits the prime check -> 'NO'."""
    # l = max(1, 3) = 3, r = min(2, 4) = 2, length = -1
    assert intersection((1, 2), (3, 4)) == "NO"


def test_intersection_zero_length_returns_no():
    """is_prime(0) returns False via the num == 0 branch -> 'NO'."""
    # l = max(2, 5) = 5, r = min(5, 8) = 5, length = 0
    assert intersection((2, 5), (5, 8)) == "NO"


def test_intersection_length_one_returns_no():
    """is_prime(1) returns False via the num == 1 branch -> 'NO'."""
    # l = max(1, 2) = 2, r = min(3, 4) = 3, length = 1
    assert intersection((1, 3), (2, 4)) == "NO"


def test_intersection_length_two_returns_yes():
    """is_prime(2) returns True via the num == 2 branch -> 'YES'."""
    # l = 1, r = 3, length = 2
    assert intersection((1, 3), (1, 3)) == "YES"


def test_intersection_length_three_prime_loop_completes_returns_yes():
    """is_prime(3) completes the for-loop without a divisor -> 'YES'."""
    # l = 1, r = 4, length = 3
    assert intersection((1, 4), (1, 4)) == "YES"


def test_intersection_length_four_composite_loop_returns_no():
    """is_prime(4) finds a divisor inside the for-loop -> 'NO'."""
    # l = 1, r = 5, length = 4 (divisible by 2)
    assert intersection((1, 5), (1, 5)) == "NO"
