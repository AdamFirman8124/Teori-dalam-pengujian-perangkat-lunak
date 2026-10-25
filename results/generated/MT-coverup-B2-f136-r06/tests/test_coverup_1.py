# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers_returns_extremes_for_both_signs():
    assert largest_smallest_integers([-8, -3, -5, 2, 7, 4]) == (-3, 2)


def test_largest_smallest_integers_returns_none_when_no_negative_integers():
    assert largest_smallest_integers([0, 2, 7, 4]) == (None, 2)


def test_largest_smallest_integers_returns_none_when_no_positive_integers():
    assert largest_smallest_integers([-8, -3, -5, 0]) == (-3, None)


def test_largest_smallest_integers_returns_none_for_empty_list():
    assert largest_smallest_integers([]) == (None, None)
