# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_both_negative_and_positive():
    assert largest_smallest_integers([-5, -1, 2, 4]) == (-1, 2)


def test_only_negatives():
    assert largest_smallest_integers([-5, -3, 0]) == (-3, None)


def test_only_positives():
    assert largest_smallest_integers([0, 1, 5]) == (None, 1)


def test_empty_and_zeros_only():
    assert largest_smallest_integers([]) == (None, None)
    assert largest_smallest_integers([0, 0]) == (None, None)
