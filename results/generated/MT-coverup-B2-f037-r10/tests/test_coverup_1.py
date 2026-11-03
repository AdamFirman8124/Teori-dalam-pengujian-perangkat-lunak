# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

"""Tests for f037.sort_even covering all previously unexecuted lines (3-11)."""

from f037 import sort_even


def test_sort_even_odd_length_covers_append_branch():
    """Odd-length input: len(evens) > len(odds), so line 10 (append) executes."""
    # evens = [4, 2] -> sorted [2, 4]; odds = [1]; ans = [2, 1]; append evens[-1] = 4
    assert sort_even([4, 1, 2]) == [2, 1, 4]


def test_sort_even_even_length_covers_false_branch():
    """Even-length input: len(evens) == len(odds), so the if on line 9 is False."""
    # evens = [5, 1] -> sorted [1, 5]; odds = [3, 2]; ans = [1, 3, 5, 2]; no append
    assert sort_even([5, 3, 1, 2]) == [1, 3, 5, 2]


def test_sort_even_empty_list_covers_loop_not_taken():
    """Empty input: loop body (line 8) never runs and the if is False."""
    assert sort_even([]) == []


def test_sort_even_single_element_covers_loop_not_taken_and_append():
    """Single element: zip is empty (loop skipped) but the if is True."""
    assert sort_even([7]) == [7]


def test_sort_even_does_not_mutate_input():
    """evens is a slice copy, so sorting it must not mutate the caller's list."""
    original = [3, 2, 1]
    result = sort_even(original)
    # evens = [3, 1] -> sorted [1, 3]; odds = [2]; ans = [1, 2]; append 3
    assert result == [1, 2, 3]
    assert original == [3, 2, 1]


def test_sort_even_duplicates_and_negatives():
    """Sorting must be stable w.r.t. values, including duplicates and negatives."""
    # evens = [0, -5, 0] -> sorted [-5, 0, 0]; odds = [1, 2, 3]
    # ans = [-5, 1, 0, 2, 0, 3]; len(evens) == len(odds), no append
    assert sort_even([0, 1, -5, 2, 0, 3]) == [-5, 1, 0, 2, 0, 3]
