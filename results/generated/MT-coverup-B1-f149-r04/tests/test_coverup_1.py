# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_empty_list():
    lst = []
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == []


def test_sorted_list_sum_all_even_lengths_sorted_by_length():
    lst = ["abcd", "ab", "abcdef", "xy"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "xy", "abcd", "abcdef"]
    assert lst == ["ab", "abcd", "abcdef", "xy"]
    assert all(len(item) % 2 == 0 for item in result)
    assert [len(item) for item in result] == sorted(len(item) for item in result)


def test_sorted_list_sum_all_odd_lengths():
    lst = ["abcde", "a", "abc"]
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == ["a", "abc", "abcde"]


def test_sorted_list_sum_mixed_even_and_odd_lengths():
    lst = ["hello", "hi", "to", "world", "a"]
    result = sorted_list_sum(lst)
    assert result == ["hi", "to"]
    assert lst == ["a", "hello", "hi", "to", "world"]
    assert all(len(item) % 2 == 0 for item in result)
    assert [len(item) for item in result] == sorted(len(item) for item in result)


def test_sorted_list_sum_single_even_and_single_odd():
    even_lst = ["ab"]
    assert sorted_list_sum(even_lst) == ["ab"]
    assert even_lst == ["ab"]

    odd_lst = ["a"]
    assert sorted_list_sum(odd_lst) == []
    assert odd_lst == ["a"]
