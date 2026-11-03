# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_empty_list_executes_loop_zero_times():
    """Covers lines 3, 4 (zero iterations) and 7."""
    assert smallest_change([]) == 0


def test_single_element_never_enters_loop_body():
    """len(arr) // 2 == 0, so loop body (lines 5-6) is skipped."""
    assert smallest_change([42]) == 0


def test_already_palindrome_odd_length():
    """Covers line 5 with the False branch (no mismatches)."""
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_already_palindrome_even_length():
    """Covers line 5 with the False branch for even-length input."""
    assert smallest_change([1, 2, 2, 1]) == 0


def test_all_mismatches_even_length():
    """Covers line 5 True branch and line 6 for every pair."""
    assert smallest_change([1, 2, 3, 4, 5, 6]) == 3


def test_all_mismatches_odd_length():
    """Middle element is ignored; both outer pairs mismatch."""
    assert smallest_change([1, 2, 3, 4, 5]) == 2


def test_mixed_matches_and_mismatches():
    """Exercises both branches of the if within a single call."""
    assert smallest_change([1, 2, 3, 2, 4]) == 1


def test_two_element_mismatch():
    """Minimal input that enters the loop body exactly once."""
    assert smallest_change([1, 2]) == 1


def test_result_is_minimum_changes_to_palindrome():
    """Postcondition: applying 'ans' single-element edits yields a palindrome."""
    arr = [1, 2, 3, 4, 5, 6]
    ans = smallest_change(arr)
    assert ans == 3
    fixed = arr[:]
    for i in range(len(fixed) // 2):
        fixed[len(fixed) - i - 1] = fixed[i]
    assert fixed == fixed[::-1]


def test_input_is_not_mutated():
    """The function must not modify its argument (no state pollution)."""
    arr = [1, 2, 3, 4]
    snapshot = list(arr)
    smallest_change(arr)
    assert arr == snapshot
