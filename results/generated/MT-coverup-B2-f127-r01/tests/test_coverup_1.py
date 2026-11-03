# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection

# NOTE: `intersection` is a pure function with no side effects and no module-level
# state, so no monkeypatching or fixture-based cleanup is required; each test is
# self-contained and leaves no state behind.


def test_intersection_length_one_is_not_prime():
    # l = max(1, 2) = 2, r = min(3, 4) = 3 -> length = 1
    # is_prime(1) takes the `num == 1` branch and returns False (lines 4-5).
    assert intersection((1, 3), (2, 4)) == "NO"


def test_intersection_touching_intervals_zero_length():
    # l = 2, r = 2 -> length = 0 -> `length > 0` is False, so is_prime is
    # never called (short-circuit branch on line 16) and we fall to line 18.
    assert intersection((1, 2), (2, 3)) == "NO"


def test_intersection_disjoint_intervals_negative_length():
    # l = 3, r = 2 -> length = -1 -> `length > 0` is False -> line 18.
    assert intersection((3, 4), (1, 2)) == "NO"


def test_intersection_length_two_is_prime():
    # l = 2, r = 4 -> length = 2 -> is_prime(2) takes the `num == 2` branch
    # and returns True (lines 6-7), so line 17 returns "YES".
    assert intersection((1, 4), (2, 5)) == "YES"


def test_intersection_length_three_is_prime():
    # l = 2, r = 5 -> length = 3 -> the for-loop body runs (line 8) but no
    # divisor is found, so is_prime falls through to `return True` (line 11).
    assert intersection((1, 5), (2, 6)) == "YES"


def test_intersection_length_four_is_composite():
    # l = 2, r = 6 -> length = 4 -> the for-loop finds the divisor 2 and
    # is_prime returns False from inside the loop (lines 9-10).
    assert intersection((1, 6), (2, 7)) == "NO"


def test_intersection_negative_bounds():
    # Exercise the max/min logic with negative endpoints as well.
    assert intersection((-3, -1), (-5, -2)) == "NO"  # length = 1 -> not prime
    assert intersection((-5, 1), (-4, 2)) == "YES"   # length = 5 -> prime
    assert intersection((-5, 0), (-4, 1)) == "NO"    # length = 4 -> composite


@pytest.mark.parametrize(
    ("interval1", "interval2", "expected"),
    [
        ((1, 3), (2, 4), "NO"),      # l=2, r=3 -> length 1 (not prime)
        ((1, 2), (2, 3), "NO"),      # l=2, r=2 -> length 0
        ((3, 4), (1, 2), "NO"),      # l=3, r=2 -> length -1
        ((1, 4), (2, 5), "YES"),     # l=2, r=4 -> length 2 (prime)
        ((1, 5), (2, 6), "YES"),     # l=2, r=5 -> length 3 (prime)
        ((1, 6), (2, 7), "NO"),      # l=2, r=6 -> length 4 (composite)
        ((1, 9), (2, 10), "YES"),    # l=2, r=9 -> length 7 (prime)
        ((1, 8), (2, 9), "NO"),      # l=2, r=8 -> length 6 (composite)
    ],
)
def test_intersection_parametrized(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected
