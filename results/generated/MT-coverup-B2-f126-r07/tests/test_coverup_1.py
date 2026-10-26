# file: project/f126/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11], "branches": [[4, 5], [4, 6], [6, 7], [6, 8], [8, 9], [8, 11]]}

import pytest

from f126 import is_sorted


def test_is_sorted_returns_true_for_ascending_list():
    assert is_sorted([1, 2, 3, 4, 5]) is True


def test_is_sorted_returns_true_for_empty_list():
    assert is_sorted([]) is True


def test_is_sorted_returns_true_for_single_element():
    assert is_sorted([7]) is True


def test_is_sorted_returns_true_for_duplicates_within_limit():
    assert is_sorted([1, 1, 2, 2, 3]) is True


def test_is_sorted_returns_false_when_a_digit_repeats_more_than_twice():
    assert is_sorted([1, 1, 1]) is False


def test_is_sorted_returns_false_for_descending_list():
    assert is_sorted([3, 2, 1]) is False


def test_is_sorted_returns_false_for_unsorted_list_with_duplicates():
    assert is_sorted([1, 2, 1]) is False


def test_is_sorted_does_not_mutate_input():
    lst = [1, 2, 2, 3]
    snapshot = list(lst)
    is_sorted(lst)
    assert lst == snapshot
