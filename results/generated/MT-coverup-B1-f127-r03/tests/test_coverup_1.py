# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length_returns_yes():
    # Overlap [2, 4] -> length 2, which is prime (covers num == 2 branch)
    assert intersection([1, 5], [2, 4]) == "YES"


def test_intersection_odd_prime_length_returns_yes():
    # Overlap [2, 5] -> length 3, prime found via the loop's "return True" path
    assert intersection([1, 6], [2, 5]) == "YES"


def test_intersection_length_one_returns_no():
    # Overlap [2, 3] -> length 1, hits the "num == 1" early return in is_prime
    assert intersection([1, 3], [2, 4]) == "NO"


def test_intersection_zero_length_returns_no():
    # Overlap is a single point -> length 0, hits the "num == 0" early return
    # and the "length > 0" short-circuit
    assert intersection([1, 3], [3, 5]) == "NO"


def test_intersection_composite_length_returns_no():
    # Overlap [2, 6] -> length 4, composite: loop finds num % i == 0
    assert intersection([1, 7], [2, 6]) == "NO"


def test_intersection_large_composite_length_returns_no():
    # Overlap [1, 9] -> length 8, composite, exercises loop iterations
    assert intersection([0, 10], [1, 9]) == "NO"


def test_intersection_no_overlap_returns_no():
    # Disjoint intervals -> r < l, negative length, "length > 0" is False
    assert intersection([1, 2], [5, 8]) == "NO"
