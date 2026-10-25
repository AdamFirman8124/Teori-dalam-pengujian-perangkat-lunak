# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_empty_list_returns_zero():
    assert smallest_change([]) == 0


def test_single_element_returns_zero():
    assert smallest_change([7]) == 0


def test_palindrome_returns_zero():
    # loop runs, if-branch is False for every pair
    assert smallest_change([1, 2, 3, 2, 1]) == 0


def test_even_length_non_palindrome_counts_mismatched_pairs():
    # pairs: (1,4) mismatch, (2,3) mismatch -> 2
    assert smallest_change([1, 2, 3, 4]) == 2


def test_odd_length_mixed_pairs():
    # pairs: (1,1) match, (2,3) mismatch; middle 9 ignored -> 1
    assert smallest_change([1, 2, 9, 3, 1]) == 1


def test_all_pairs_mismatched():
    assert smallest_change([1, 1, 2, 2]) == 2


def test_input_list_not_mutated():
    arr = [1, 2, 3, 4]
    original = list(arr)
    smallest_change(arr)
    assert arr == original
