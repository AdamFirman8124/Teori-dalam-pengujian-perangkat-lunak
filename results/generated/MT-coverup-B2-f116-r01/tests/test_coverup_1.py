# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f116.sort_array.

The function under test (from f116/__init__.py):

    def sort_array(arr):
        return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

Each test below calls sort_array, which guarantees that line 3 is
executed, and asserts postconditions about the returned ordering:
numeric order first (via the inner sorted), then a stable re-ordering
by ascending popcount (number of '1' bits in the binary representation).

sort_array is a pure function, so no monkeypatching/fixture teardown is
required to avoid state pollution; we additionally assert that the input
list is never mutated.
"""

import f116


def test_sort_array_basic():
    # bit counts: 1->1, 2->1, 3->2, 4->1, 5->2
    # numeric order [1,2,3,4,5], grouped by popcount -> [1,2,4,3,5]
    arr = [1, 5, 2, 3, 4]
    result = f116.sort_array(arr)
    assert result == [1, 2, 4, 3, 5]
    # input must not be mutated
    assert arr == [1, 5, 2, 3, 4]


def test_sort_array_empty():
    assert f116.sort_array([]) == []


def test_sort_array_single_element():
    assert f116.sort_array([7]) == [7]


def test_sort_array_duplicates():
    # 3->11 (2 ones), 6->110 (2 ones): all tie, numeric order retained
    arr = [6, 3, 3]
    result = f116.sort_array(arr)
    assert result == [3, 3, 6]
    assert arr == [6, 3, 3]


def test_sort_array_zero():
    # 0 has popcount 0, so it sorts before everything
    assert f116.sort_array([2, 0, 1]) == [0, 1, 2]


def test_sort_array_stability_on_equal_popcounts():
    # 1->1, 2->10, 8->1000, 15->1111
    # popcounts [1,1,1,3]: ties broken by the inner numeric sort
    assert f116.sort_array([8, 15, 1, 2]) == [1, 2, 8, 15]


def test_sort_array_mixed_popcounts():
    # 0->0 ones, 1->1, 4->1, 7->3, 5->2, 6->2, 3->2
    # numeric order [0,1,3,4,5,6,7]
    # grouped by popcount -> 0 | 1,4 | 3,5,6 | 7
    assert f116.sort_array([7, 3, 6, 5, 4, 1, 0]) == [0, 1, 4, 3, 5, 6, 7]


def test_sort_array_power_of_two_pattern():
    # powers of two each have exactly one '1' bit -> numeric order kept
    assert f116.sort_array([16, 2, 8, 4]) == [2, 4, 8, 16]


def test_sort_array_result_is_sorted_by_popcount():
    arr = [9, 12, 7, 1, 5, 14, 2]
    result = f116.sort_array(arr)
    popcounts = [bin(x)[2:].count('1') for x in result]
    assert popcounts == sorted(popcounts)
    # same multiset of elements as the input
    assert sorted(result) == sorted(arr)
    # input not mutated
    assert arr == [9, 12, 7, 1, 5, 14, 2]
