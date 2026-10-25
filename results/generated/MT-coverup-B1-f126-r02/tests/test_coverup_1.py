# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_true_counts_lines_3_to_9():
    # Exercises lines 3-5 (count_digit construction and increment loop)
    # and line 9 (all elements non-decreasing, no digit more than twice).
    assert is_sorted([1, 2, 2, 3]) is True


def test_is_sorted_false_too_many_duplicates_line_7():
    # Exercises line 7: an element appears more than twice -> False,
    # even though the list is non-decreasing.
    assert is_sorted([1, 2, 2, 2]) is False


def test_is_sorted_false_unsorted_line_11():
    # Exercises line 11 (else branch): counts are fine but the list
    # is not non-decreasing.
    assert is_sorted([1, 3, 2]) is False


def test_is_sorted_empty_list():
    # Edge case: empty list -> count_digit is empty, any() is False,
    # all() over empty range is True -> returns True (line 9).
    assert is_sorted([]) is True


def test_is_sorted_single_element():
    # Single element: counting loop runs once, all() over empty range
    # is True -> returns True (line 9).
    assert is_sorted([5]) is True


def test_is_sorted_does_not_mutate_input():
    # Postcondition: the input list is left untouched.
    lst = [2, 1]
    is_sorted(lst)
    assert lst == [2, 1]
