# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f116.sort_array.

sort_array(arr) returns a NEW list with the elements of ``arr`` sorted
first by numeric value, then (stably) by the number of '1' bits in the
binary representation of each element.  The function is pure, so no
monkeypatching or teardown is required to avoid state pollution.
"""

from f116 import sort_array


def test_sort_array_orders_by_number_of_one_bits():
    # 1, 2 and 4 have one '1' bit; 3 and 5 have two.
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_ties_fall_back_to_ascending_value():
    # Every power of two has exactly one '1' bit, so the inner
    # sorted(arr) decides the final order among them.
    assert sort_array([8, 1, 4, 2]) == [1, 2, 4, 8]


def test_sort_array_zero_comes_first():
    # bin(0)[2:] == '0' contains zero '1' bits, so 0 sorts first.
    assert sort_array([3, 0, 1, 2]) == [0, 1, 2, 3]


def test_sort_array_handles_duplicates():
    assert sort_array([2, 3, 2, 3]) == [2, 2, 3, 3]


def test_sort_array_empty_and_single_element():
    assert sort_array([]) == []
    assert sort_array([7]) == [7]


def test_sort_array_negative_numbers():
    # bin(-n)[2:] keeps the magnitude's bits (the 'b' character
    # contributes no '1'), e.g. bin(-3)[2:] == 'b11' -> two '1' bits,
    # bin(-1)[2:] == 'b1' -> one '1' bit.
    assert sort_array([-3, -1]) == [-1, -3]
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]


def test_sort_array_returns_new_list_and_does_not_mutate_input():
    original = [3, 1, 2]
    snapshot = list(original)
    result = sort_array(original)
    assert result == [1, 2, 3]
    assert original == snapshot          # input list left untouched
    assert result is not original        # a fresh list is returned
