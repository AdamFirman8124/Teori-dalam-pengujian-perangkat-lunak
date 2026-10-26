# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_negative_and_positive_values():
    assert largest_smallest_integers([-7, -2, 0, 3, 9]) == (-2, 3)


def test_largest_smallest_integers_without_negative_values():
    assert largest_smallest_integers([0, 2, 5]) == (None, 2)


def test_largest_smallest_integers_without_positive_values():
    assert largest_smallest_integers([-8, -3, 0]) == (-3, None)


def test_largest_smallest_integers_with_no_negative_or_positive_values():
    assert largest_smallest_integers([0]) == (None, None)
