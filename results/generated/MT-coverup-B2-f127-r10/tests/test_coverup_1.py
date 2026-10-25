# file: project/f127/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [16, 17], [16, 18]]}

import pytest

from f127 import intersection


def test_intersection_prime_length_two_returns_yes():
    assert intersection([0, 2], [0, 10]) == "YES"


def test_intersection_prime_length_three_returns_yes():
    assert intersection([0, 3], [0, 10]) == "YES"


def test_intersection_prime_length_five_partial_overlap_returns_yes():
    assert intersection([0, 10], [3, 8]) == "YES"


def test_intersection_length_one_returns_no():
    assert intersection([0, 1], [0, 10]) == "NO"


def test_intersection_composite_length_four_returns_no():
    assert intersection([0, 4], [0, 10]) == "NO"


def test_intersection_composite_length_nine_returns_no():
    assert intersection([0, 9], [0, 20]) == "NO"


def test_intersection_no_overlap_returns_no():
    assert intersection([5, 10], [0, 3]) == "NO"


def test_intersection_touching_intervals_returns_no():
    assert intersection([0, 5], [5, 10]) == "NO"


@pytest.mark.parametrize(
    "interval1, interval2, expected",
    [
        ([0, 2], [1, 3], "NO"),
        ([1, 4], [0, 10], "YES"),
        ([2, 9], [0, 5], "YES"),
        ([0, 6], [0, 10], "NO"),
        ([10, 20], [0, 5], "NO"),
    ],
)
def test_intersection_parametrized(interval1, interval2, expected):
    assert intersection(interval1, interval2) == expected
