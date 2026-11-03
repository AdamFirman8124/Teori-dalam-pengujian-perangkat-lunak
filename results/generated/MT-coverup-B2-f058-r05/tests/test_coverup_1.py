# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_returns_sorted_common_elements():
    assert common([3, 1, 2], [2, 3, 4]) == [2, 3]
    assert common([], [1, 2]) == []
    assert common([1, 2], []) == []
    assert common(["b", "a"], ["a", "b", "c"]) == ["a", "b"]
    assert common([1, 1, 2], [2, 1]) == [1, 2]
    assert common([1], [2]) == []
