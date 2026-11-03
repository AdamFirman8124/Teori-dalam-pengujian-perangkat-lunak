# file: project/f088/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f088.sort_array.

Covers every branch of the single-line implementation:
  - empty input  -> returns []
  - non-empty, (first + last) % 2 == 0 -> sorted descending (reverse=True)
  - non-empty, (first + last) % 2 != 0 -> sorted ascending  (reverse=False)

sort_array is a pure function (no I/O, no globals mutated), so no
monkeypatching/cleanup is required; each test works on fresh literals,
avoiding any state pollution between tests.
"""

from f088 import sort_array


def test_sort_array_empty_returns_empty_list():
    """Branch: len(array) == 0 -> []"""
    result = sort_array([])
    assert result == []
    assert isinstance(result, list)


def test_sort_array_odd_first_last_sum_sorted_ascending():
    """Branch: non-empty, (array[0] + array[-1]) % 2 != 0 -> reverse=False."""
    # 2 + 5 = 7 -> odd -> ascending order
    result = sort_array([2, 4, 3, 0, 1, 5])
    assert result == [0, 1, 2, 3, 4, 5]
    assert result == sorted(result, reverse=False)


def test_sort_array_even_first_last_sum_sorted_descending():
    """Branch: non-empty, (array[0] + array[-1]) % 2 == 0 -> reverse=True."""
    # 2 + 6 = 8 -> even -> descending order
    result = sort_array([2, 4, 3, 0, 1, 5, 6])
    assert result == [6, 5, 4, 3, 2, 1, 0]
    assert result == sorted(result, reverse=True)


def test_sort_array_does_not_mutate_input():
    """Postcondition: the original list is left untouched."""
    original = [3, 1, 2]
    snapshot = list(original)
    sort_array(original)  # 3 + 2 = 5 -> odd -> ascending copy
    assert original == snapshot
