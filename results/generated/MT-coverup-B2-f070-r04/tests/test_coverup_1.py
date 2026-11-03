# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_empty_list_returns_empty():
    # Covers line 3 (initialization) and line 8 (return) with the while
    # loop never entered (line 4 branch: False).
    assert strange_sort_list([]) == []


def test_single_element():
    # Covers the loop body exactly once: min branch (line 5, switch True),
    # remove (line 6), toggle (line 7), then loop exit and return.
    assert strange_sort_list([7]) == [7]


def test_even_length_alternates_min_max():
    # Exercises both branches of line 5: min when switch is True,
    # max when switch is False.
    assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]


def test_odd_length_alternates_min_max():
    # Unsorted input, odd length: min, max, min, max, min.
    assert strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]


def test_duplicates_are_handled():
    # remove() removes the first occurrence; duplicates still alternate.
    assert strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]


def test_function_consumes_a_copy_leaving_original_intact():
    # The function mutates its argument via lst.remove(); pass a copy so
    # no state pollution occurs, and assert the documented side effect.
    original = [3, 1, 2]
    working = list(original)
    result = strange_sort_list(working)
    assert result == [1, 3, 2]
    assert working == []          # input list fully consumed
    assert original == [3, 1, 2]  # caller's list untouched
