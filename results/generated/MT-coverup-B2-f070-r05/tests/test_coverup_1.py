# file: project/f070/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest

from f070 import strange_sort_list


def test_empty_list_covers_loop_skip_and_return():
    # Covers line 3 (init), line 4 (while condition false), line 8 (return).
    # Pass a fresh list: the function mutates its argument via lst.remove.
    result = strange_sort_list([])
    assert result == []


def test_single_element_covers_min_branch():
    # Covers lines 3-8 with switch=True (min branch) taken once.
    result = strange_sort_list([7])
    assert result == [7]


def test_even_length_alternates_min_and_max():
    # Covers both branches of line 5 (min when switch=True, max when
    # switch=False), line 6 (remove), line 7 (toggle), line 8 (return).
    src = [1, 2, 3, 4]
    result = strange_sort_list(list(src))  # copy: function mutates its arg
    assert result == [1, 4, 2, 3]
    # The original list must be untouched (no state pollution).
    assert src == [1, 2, 3, 4]


def test_odd_length_alternates_min_and_max():
    src = [5, 1, 3]
    result = strange_sort_list(list(src))
    assert result == [1, 5, 3]
    assert src == [5, 1, 3]


def test_unsorted_input_with_negatives():
    result = strange_sort_list([10, -1, 7, 3, 0])
    assert result == [-1, 10, 0, 7, 3]


def test_duplicates():
    # remove() removes the first occurrence; result must still be complete.
    result = strange_sort_list([2, 2, 2])
    assert result == [2, 2, 2]
