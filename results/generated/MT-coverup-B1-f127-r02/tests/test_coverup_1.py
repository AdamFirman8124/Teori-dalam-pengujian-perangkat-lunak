# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length():
    # Overlap [1, 5] and [2, 6] -> [2, 5], length 3 (prime) -> "YES"
    assert intersection((1, 5), (2, 6)) == "YES"


def test_intersection_composite_length():
    # Overlap [1, 10] and [2, 11] -> [2, 10], length 8 (composite) -> "NO"
    assert intersection((1, 10), (2, 11)) == "NO"


def test_intersection_no_overlap():
    # No overlap: r - l <= 0 -> "NO" (covers the length <= 0 branch)
    assert intersection((1, 3), (5, 7)) == "NO"


def test_intersection_touching_endpoints():
    # Touching endpoints: length == 0 -> "NO"
    assert intersection((1, 3), (3, 5)) == "NO"


def test_intersection_negative_overlap():
    # Overlap is negative (interval1 entirely left of interval2) -> "NO"
    assert intersection((1, 2), (4, 6)) == "NO"


def test_intersection_length_one_is_not_prime():
    # Overlap [2, 3] and [1, 4] -> [2, 3], length 1 -> not prime -> "NO"
    assert intersection((2, 3), (1, 4)) == "NO"


def test_intersection_length_two_is_prime():
    # Overlap [1, 4] and [2, 5] -> [2, 4], length 2 -> prime -> "YES"
    assert intersection((1, 4), (2, 5)) == "YES"


def test_intersection_length_zero_not_prime():
    # Overlap [0, 1] and [0, 1] -> length 0 -> "NO" (covers is_prime(0) branch)
    assert intersection((0, 1), (0, 1)) == "NO"


def test_intersection_length_nine_composite():
    # Overlap [1, 11] and [2, 12] -> [2, 11], length 9 (composite, odd) -> "NO"
    assert intersection((1, 11), (2, 12)) == "NO"


def test_intersection_length_seven_prime():
    # Overlap [1, 9] and [2, 10] -> [2, 9], length 7 (prime) -> "YES"
    assert intersection((1, 9), (2, 10)) == "YES"
