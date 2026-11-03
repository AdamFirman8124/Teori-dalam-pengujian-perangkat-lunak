# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_mixed_lengths_filters_and_sorts():
    lst = ["aa", "a", "aaa", "ab", "abc", "abcd"]
    result = sorted_list_sum(lst)
    # Odd-length strings are filtered out; result sorted by length
    assert result == ["aa", "ab", "abcd"]
    # The input list is sorted in place (line 3 side effect)
    assert lst == ["a", "aa", "aaa", "ab", "abc", "abcd"]


def test_sorted_list_sum_sorts_by_length():
    lst = ["aaaa", "aa", "bb"]
    result = sorted_list_sum(lst)
    # Length-based ordering, not lexicographic
    assert result == ["aa", "bb", "aaaa"]


def test_sorted_list_sum_all_odd_filtered_out():
    lst = ["a", "abc", "abcde"]
    result = sorted_list_sum(lst)
    assert result == []
    # Input still sorted in place even though nothing is kept
    assert lst == ["a", "abc", "abcde"]


def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []


def test_sorted_list_sum_stable_ties():
    lst = ["dd", "cc", "bb", "aa"]
    result = sorted_list_sum(lst)
    # All even-length; stable sort preserves alphabetical order for ties
    assert result == ["aa", "bb", "cc", "dd"]
