# file: project/f136/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

from f136 import largest_smallest_integers


def test_largest_smallest_integers():
    assert largest_smallest_integers([-5, -1, 0, 2, 8]) == (-1, 2)
    assert largest_smallest_integers([3, 1, 7]) == (None, 1)
    assert largest_smallest_integers([-9, -2, -4]) == (-2, None)
    assert largest_smallest_integers([0, 0]) == (None, None)
