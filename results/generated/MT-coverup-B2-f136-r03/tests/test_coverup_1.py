# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_negative_and_positive_values():
    assert largest_smallest_integers([-5, -2, 0, 3, 8]) == (-2, 3)


def test_largest_smallest_integers_without_negative_or_positive_values():
    assert largest_smallest_integers([0, 0]) == (None, None)
