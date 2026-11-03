# file: project/f116/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f116.sort_array.

sort_array(arr) returns sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1')),
i.e. the input is first sorted by value, then (stably) by the number of '1'
characters in bin(x)[2:].  For non-negative x that is the popcount of x; for
negative x, bin(x) == '-0b<digits of abs(x)>' so bin(x)[2:] == 'b<digits>' and
the key is the popcount of abs(x).

The function is pure (sorted() copies, nothing global is touched), so no
monkeypatching or teardown is required to avoid state pollution.
"""

from f116 import sort_array


def test_sort_array_orders_by_popcount_then_value():
    # sorted([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    # keys: 1->1, 2->1, 3->2, 4->1, 5->2 ; stable re-sort => [1, 2, 4, 3, 5]
    assert sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]


def test_sort_array_full_byte_range():
    # sorted([7, 3, 5, 1, 6, 2, 4, 0]) == [0, 1, 2, 3, 4, 5, 6, 7]
    # keys: 0->0, 1->1, 2->1, 3->2, 4->1, 5->2, 6->2, 7->3
    # stable re-sort => [0, 1, 2, 4, 3, 5, 6, 7]
    assert sort_array([7, 3, 5, 1, 6, 2, 4, 0]) == [0, 1, 2, 4, 3, 5, 6, 7]


def test_sort_array_empty_list():
    # Exercises the return line without ever invoking the key lambda.
    assert sort_array([]) == []


def test_sort_array_single_element():
    # bin(7)[2:] == '111' -> key 3; result is the element itself.
    assert sort_array([7]) == [7]


def test_sort_array_duplicates_and_zero():
    # sorted([3, 0, 2, 2]) == [0, 2, 2, 3]; keys: 0->0, 2->1, 2->1, 3->2
    assert sort_array([3, 0, 2, 2]) == [0, 2, 2, 3]


def test_sort_array_negative_numbers():
    # bin(-n)[2:] == 'b' + binary digits of abs(n), so key == popcount(abs(n)).
    # sorted([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    # keys: -6->2, -5->2, -4->1, -3->2, -2->1 ; stable => [-4, -2, -6, -5, -3]
    assert sort_array([-2, -3, -4, -5, -6]) == [-4, -2, -6, -5, -3]


def test_sort_array_does_not_mutate_input():
    original = [3, 1, 2]
    result = sort_array(original)
    assert original == [3, 1, 2]  # input list untouched
    assert result == [1, 2, 3]    # keys: 1->1, 2->1, 3->2
