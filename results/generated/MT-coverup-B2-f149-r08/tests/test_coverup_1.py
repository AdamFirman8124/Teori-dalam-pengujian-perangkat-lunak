# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f149 import sorted_list_sum


def test_empty_list_returns_empty():
    lst = []
    assert sorted_list_sum(lst) == []
    assert lst == []


def test_all_odd_lengths_filtered_out():
    lst = ["a", "abc", "abcde"]
    assert sorted_list_sum(lst) == []
    # postcondition: input list sorted in place
    assert lst == ["a", "abc", "abcde"]


def test_mixed_lengths_sorted_by_length():
    lst = ["abcd", "a", "abc", "ab", "abcde", "abcdef"]
    assert sorted_list_sum(lst) == ["ab", "abcd", "abcdef"]


def test_equal_lengths_keep_alphabetical_order():
    lst = ["dd", "bb", "cc", "aa"]
    assert sorted_list_sum(lst) == ["aa", "bb", "cc", "dd"]


def test_input_list_is_mutated_in_place():
    lst = ["zzzz", "b", "aa", "ccc"]
    result = sorted_list_sum(lst)
    assert lst == ["aa", "b", "ccc", "zzzz"]
    assert result == ["aa", "zzzz"]


def test_returns_new_list_not_input():
    lst = ["aa", "bb"]
    result = sorted_list_sum(lst)
    assert result == ["aa", "bb"]
    assert result is not lst


def test_single_even_element():
    lst = ["xy"]
    assert sorted_list_sum(lst) == ["xy"]


def test_single_odd_element():
    lst = ["xyz"]
    assert sorted_list_sum(lst) == []


def test_duplicates_preserved():
    lst = ["aa", "aa", "b", "bb"]
    assert sorted_list_sum(lst) == ["aa", "aa", "bb"]
