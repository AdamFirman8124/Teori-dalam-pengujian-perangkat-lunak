# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_empty_list():
    lst = []
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == []


def test_mixed_even_and_odd_lengths():
    lst = ["a", "aa", "aaa", "aaaa"]
    result = sorted_list_sum(lst)
    assert result == ["aa", "aaaa"]


def test_all_odd_lengths_returns_empty():
    lst = ["a", "abc", "abcde"]
    result = sorted_list_sum(lst)
    assert result == []


def test_filters_even_and_sorts_by_length():
    lst = ["abc", "abcd", "ab", "a", "abcde", "abcdef"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "abcd", "abcdef"]
    # verify all returned strings have even length
    assert all(len(s) % 2 == 0 for s in result)
    # verify sorted by length
    assert [len(s) for s in result] == sorted([len(s) for s in result])


def test_same_length_keeps_sorted_order():
    lst = ["dc", "ab", "ba", "c"]
    original_copy = list(lst)
    result = sorted_list_sum(lst)
    assert result == ["ab", "ba", "dc"]
    # input list itself is sorted in place as postcondition of implementation
    assert lst == sorted(original_copy)
