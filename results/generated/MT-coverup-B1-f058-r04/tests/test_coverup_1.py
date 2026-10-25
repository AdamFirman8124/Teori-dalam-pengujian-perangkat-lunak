# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_returns_sorted_unique_matches():
    assert common([3, 1, 2, 2], [2, 3, 4, 2]) == [2, 3]


def test_common_returns_empty_list_when_no_values_match():
    assert common([1, 2], [3, 4]) == []


def test_common_handles_empty_inputs():
    assert common([], [1, 2]) == []
    assert common([1, 2], []) == []
