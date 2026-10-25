# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f116 import sort_array


def test_sort_array_groups_by_popcount_then_value():
    assert sort_array([3, 5, 6, 7, 8]) == [8, 3, 5, 6, 7]
    assert sort_array([1, 2, 4, 3]) == [1, 2, 4, 3]
    assert sort_array([7, 6, 5, 3]) == [3, 5, 6, 7]


def test_sort_array_larger_mixed():
    arr = [1, 5, 3, 7, 8, 2, 4]
    assert sort_array(arr) == [1, 2, 4, 8, 3, 5, 7]
    # verify postcondition: sorted by (popcount, value)
    result = sort_array(arr)
    assert result == sorted(arr, key=lambda x: (bin(x)[2:].count('1'), x))


def test_sort_array_empty_and_single():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([0]) == [0]


def test_sort_array_zero_duplicates_and_no_mutation():
    orig = [2, 0, 1, 2, 3, 3]
    copy = list(orig)
    result = sort_array(orig)
    assert result == [0, 1, 2, 2, 3, 3]
    assert orig == copy
    assert result is not orig
