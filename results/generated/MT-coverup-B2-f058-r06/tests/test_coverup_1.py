# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_with_overlap():
    assert common([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_common_no_overlap():
    assert common([1, 2], [3, 4]) == []


def test_common_empty_l1():
    assert common([], [1, 2, 3]) == []


def test_common_empty_l2():
    assert common([1, 2, 3], []) == []


def test_common_both_empty():
    assert common([], []) == []


def test_common_duplicates_and_sorted():
    assert common([3, 3, 2, 1, 2], [3, 3, 5, 1]) == [1, 3]
