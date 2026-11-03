# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

import pytest

from f037 import sort_even


def test_sort_even_even_length():
    """Even-length input: loop body executes, the 'if' branch is False (line 10 skipped)."""
    original = [5, 1, 3, 2]
    result = sort_even(original)
    # evens = [5, 3] -> sorted [3, 5]; odds = [1, 2]; interleaved
    assert result == [3, 1, 5, 2]
    # function must not mutate its input (slicing makes copies)
    assert original == [5, 1, 3, 2]


def test_sort_even_odd_length():
    """Odd-length input: loop body executes and the 'if' branch is True (line 10 runs)."""
    original = [5, 1, 3]
    result = sort_even(original)
    # evens = [5, 3] -> sorted [3, 5]; odds = [1]; zip yields (3, 1);
    # len(evens) > len(odds) so trailing 5 is appended
    assert result == [3, 1, 5]
    assert original == [5, 1, 3]


def test_sort_even_empty_list():
    """Empty input: lines 3-6 execute, loop body and 'if' branch are skipped."""
    assert sort_even([]) == []


def test_sort_even_single_element():
    """Single element: loop body skipped, 'if' branch True (line 10 runs)."""
    assert sort_even([2]) == [2]


def test_sort_even_already_sorted_and_duplicates():
    """Already-sorted evens with duplicates exercise evens.sort() on equal keys."""
    result = sort_even([1, 9, 1, 8, 1])
    # evens = [1, 1, 1] (already sorted); odds = [9, 8];
    # zip yields (1, 9), (1, 8); extra even 1 appended
    assert result == [1, 9, 1, 8, 1]
