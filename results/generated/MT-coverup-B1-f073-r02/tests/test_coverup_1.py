# file: project/f073/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f073 import smallest_change


def test_empty_list_returns_zero():
    assert smallest_change([]) == 0


def test_single_element_returns_zero():
    assert smallest_change([7]) == 0


def test_already_palindrome_returns_zero():
    arr = [1, 2, 3, 2, 1]
    assert smallest_change(arr) == 0
    # postcondition: input not mutated
    assert arr == [1, 2, 3, 2, 1]


def test_even_length_all_pairs_mismatched():
    assert smallest_change([1, 2, 3, 4]) == 2


def test_odd_length_one_mismatched_pair():
    assert smallest_change([1, 2, 9, 3, 1]) == 1


def test_mixed_pairs_counts_only_mismatches():
    # pairs: (1,1) match, (2,3) mismatch, (4,4) match
    assert smallest_change([1, 2, 4, 3, 1]) == 1


def test_two_element_mismatch():
    assert smallest_change([1, 2]) == 1


def test_two_element_match():
    assert smallest_change([5, 5]) == 0


def test_does_not_mutate_input(monkeypatch):
    arr = [1, 2, 3, 4, 5]
    snapshot = list(arr)
    smallest_change(arr)
    assert arr == snapshot
