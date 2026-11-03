# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

import pytest

from f149 import sorted_list_sum


def test_filters_odd_lengths_and_sorts_by_length():
    """Covers lines 3-8 including both branches of the parity check."""
    lst = ["school", "AI", "asdf", "b"]
    result = sorted_list_sum(lst)
    # "b" (len 1) is odd -> dropped; remaining sorted by length
    assert result == ["AI", "asdf", "school"]


def test_input_list_is_sorted_in_place():
    """Line 3 (lst.sort()) mutates the caller's list; verify that side effect."""
    lst = ["ccc", "a", "bb"]
    result = sorted_list_sum(lst)
    assert lst == ["a", "bb", "ccc"]          # in-place sort happened
    assert result == ["bb"]                    # only even-length string kept


def test_equal_lengths_keep_alphabetical_order():
    """Stable sort by len must preserve the earlier alphabetical ordering."""
    lst = ["dd", "bb", "cc", "aa"]
    result = sorted_list_sum(lst)
    assert result == ["aa", "bb", "cc", "dd"]


def test_empty_list_returns_empty_list():
    """Covers the loop-skipped branch (line 5 with empty iterable)."""
    assert sorted_list_sum([]) == []


def test_all_odd_lengths_yields_empty_list():
    """Every element takes the False branch of the parity check."""
    assert sorted_list_sum(["a", "abc", "abcde"]) == []


@pytest.mark.parametrize(
    "input_list, expected",
    [
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        (["a", "b", "c"], []),
        (["aaaa", "bb", "cc"], ["bb", "cc", "aaaa"]),
    ],
)
def test_parametrized_behavior(input_list, expected):
    assert sorted_list_sum(list(input_list)) == expected
