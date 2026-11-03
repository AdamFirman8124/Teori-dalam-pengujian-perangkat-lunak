# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length_two_returns_yes():
    # l = max(1, 3) = 3, r = min(5, 7) = 5, length = 2
    # Covers: is_prime(2) -> True branch (line 6-7), and "YES" return (line 17)
    assert intersection([1, 5], [3, 7]) == "YES"


def test_intersection_prime_length_greater_than_two_returns_yes():
    # l = max(1, 2) = 2, r = min(10, 9) = 9, length = 7
    # Covers: is_prime loop with no divisor found -> return True (lines 8, 9-False, 11)
    assert intersection([1, 10], [2, 9]) == "YES"


def test_intersection_length_one_returns_no():
    # l = max(1, 3) = 3, r = min(4, 7) = 4, length = 1
    # Covers: is_prime(1) -> num == 1 branch returns False (lines 4-5), "NO" return (line 18)
    assert intersection([1, 4], [3, 7]) == "NO"


def test_intersection_composite_length_returns_no():
    # l = max(1, 3) = 3, r = min(10, 7) = 7, length = 4
    # Covers: is_prime loop finding a divisor -> return False (lines 8-10), "NO" return
    assert intersection([1, 10], [3, 7]) == "NO"


def test_intersection_zero_length_returns_no():
    # l = max(1, 3) = 3, r = min(3, 7) = 3, length = 0
    # Covers: short-circuit of `length > 0` being False (line 16-False), "NO" return
    assert intersection([1, 3], [3, 7]) == "NO"


def test_intersection_negative_length_returns_no():
    # Disjoint intervals: l = max(5, 1) = 5, r = min(10, 3) = 3, length = -2
    # Covers: negative length -> "NO" return (line 18)
    assert intersection([5, 10], [1, 3]) == "NO"


def test_intersection_max_of_starts_and_min_of_ends():
    # interval2 starts later and interval1 ends earlier:
    # l = max(1, 4) = 4, r = min(6, 9) = 6, length = 2 (prime) -> "YES"
    # Verifies that max/min are taken over the correct endpoints.
    assert intersection([1, 6], [4, 9]) == "YES"


@pytest.mark.parametrize(
    "interval1, interval2, expected",
    [
        ([1, 5], [3, 7], "YES"),      # length 2, prime
        ([1, 10], [2, 9], "YES"),     # length 7, prime > 2
        ([1, 4], [3, 7], "NO"),       # length 1, not prime
        ([1, 10], [3, 7], "NO"),      # length 4, composite
        ([1, 3], [3, 7], "NO"),       # length 0
        ([5, 10], [1, 3], "NO"),      # negative length
        ([2, 3], [2, 3], "NO"),       # length 1, touching interval
        ([0, 3], [0, 6], "YES"),      # length 3, prime, with zero start
    ],
)
def test_intersection_parametrized(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected
