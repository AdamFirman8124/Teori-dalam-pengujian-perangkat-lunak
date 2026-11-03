# file: project/f033/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": []}
# gained: {"lines": [3, 4, 5], "branches": []}

import pytest

from f033 import sort_third


def test_sort_third_basic():
    """Covers lines 3-5: copy, sort every third element, return."""
    original = [5, 6, 3, 4, 8, 9, 2]
    result = sort_third(original)

    # Line 3: the input list is copied, not mutated.
    assert result is not original
    assert original == [5, 6, 3, 4, 8, 9, 2]

    # Line 4: elements at indices 0, 3, 6, ... come back sorted.
    assert result == [2, 6, 3, 4, 8, 9, 5]
    third = result[::3]
    assert third == sorted(third)

    # Elements at other indices are untouched.
    assert result[1::3] == original[1::3]
    assert result[2::3] == original[2::3]

    # Multiset of elements is preserved.
    assert sorted(result) == sorted(original)


def test_sort_third_orders_every_third_element():
    l = [9, 2, 3, 4, 5, 6, 1, 8, 7, 0]
    result = sort_third(l)

    # Indices 0, 3, 6, 9 held 9, 4, 1, 0 -> sorted to 0, 1, 4, 9.
    assert result[0] == 0
    assert result[3] == 1
    assert result[6] == 4
    assert result[9] == 9

    # Non-third positions keep their original values.
    assert result[1::3] == l[1::3]
    assert result[2::3] == l[2::3]

    # Input remains unchanged (copy made on line 3).
    assert l == [9, 2, 3, 4, 5, 6, 1, 8, 7, 0]


def test_sort_third_already_sorted_and_empty():
    # Empty list (exercises the slice/sort on an empty copy).
    assert sort_third([]) == []

    # Single element.
    assert sort_third([42]) == [42]

    # Already sorted thirds stay the same.
    l = [1, 2, 3, 4, 5, 6]
    result = sort_third(l)
    assert result == [1, 2, 3, 4, 5, 6]
    assert result is not l
