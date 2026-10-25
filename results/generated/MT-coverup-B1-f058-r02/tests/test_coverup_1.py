# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_returns_sorted_unique_intersection():
    assert common([3, 1, 2, 2], [4, 2, 1, 2]) == [1, 2]


def test_common_returns_empty_list_when_inputs_do_not_overlap():
    assert common([1, 3], [2, 4]) == []


def test_common_returns_empty_list_for_empty_input():
    assert common([], [1, 2, 3]) == []
    assert common([1, 2, 3], []) == []
