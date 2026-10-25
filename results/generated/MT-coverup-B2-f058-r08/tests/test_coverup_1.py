# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_returns_sorted_unique_intersection():
    result = common([3, 1, 2, 2], [4, 2, 1, 2])

    assert result == [1, 2]


def test_common_returns_empty_list_when_inputs_have_no_common_elements():
    result = common([1, 3], [2, 4])

    assert result == []
