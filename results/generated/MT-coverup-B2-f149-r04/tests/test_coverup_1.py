# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_empty_list():
    lst = []
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == []


def test_sorted_list_sum_mixed_even_odd_filters_and_sorts_by_len():
    lst = ["abcdef", "a", "ab", "abc", "abcd", "abcde"]
    original_copy = list(lst)
    result = sorted_list_sum(lst)
    assert result == ["ab", "abcd", "abcdef"]
    # postcondition: only even-length strings kept
    assert all(len(s) % 2 == 0 for s in result)
    # postcondition: sorted by length
    assert [len(s) for s in result] == sorted(len(s) for s in result)
    # postcondition: input list was sorted in place
    assert lst == sorted(original_copy)


def test_sorted_list_sum_all_odd_returns_empty():
    lst = ["a", "abc", "abcde"]
    result = sorted_list_sum(lst)
    assert result == []


def test_sorted_list_sum_all_even_sorted_by_len():
    lst = ["abcd", "ab", "abcdef"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "abcd", "abcdef"]
