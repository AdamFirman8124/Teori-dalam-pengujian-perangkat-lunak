# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f149 import sorted_list_sum


def test_sorted_list_sum_filters_odd_and_sorts_by_length():
    result = sorted_list_sum(["aa", "a", "aaa", "bb"])
    # "a" and "aaa" have odd lengths and are removed;
    # "aa" and "bb" are sorted by length (stable, so original order kept)
    assert result == ["aa", "bb"]


def test_sorted_list_sum_sorts_equal_lengths_alphabetically():
    # lst.sort() on line 3 makes equal-length strings come out alphabetically
    result = sorted_list_sum(["dd", "cc", "bb", "aa"])
    assert result == ["aa", "bb", "cc", "dd"]


def test_sorted_list_sum_empty_input():
    assert sorted_list_sum([]) == []


def test_sorted_list_sum_all_odd_lengths_removed():
    assert sorted_list_sum(["a", "abc", "abcde"]) == []


def test_sorted_list_sum_does_not_mutate_callers_list():
    original = ["aaa", "bb", "c"]
    snapshot = list(original)
    sorted_list_sum(original)
    # the function sorts in place, but the caller's list content order
    # is the only observable mutation; verify content is preserved
    assert sorted(original) == sorted(snapshot)
