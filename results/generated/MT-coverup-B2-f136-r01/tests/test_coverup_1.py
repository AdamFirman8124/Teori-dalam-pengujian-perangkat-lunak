# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers_with_mixed_values():
    values = [-10, -3, 0, 2, 7]
    assert largest_smallest_integers(values) == (-3, 2)
    assert values == [-10, -3, 0, 2, 7]


def test_largest_smallest_integers_without_nonzero_values():
    values = [0, 0]
    assert largest_smallest_integers(values) == (None, None)
    assert values == [0, 0]
