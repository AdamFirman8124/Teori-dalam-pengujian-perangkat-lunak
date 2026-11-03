# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_filters_odd_length_strings_and_sorts_in_place():
    lst = ["aa", "a", "aaa"]
    result = sorted_list_sum(lst)
    # "a" (len 1) and "aaa" (len 3) are odd -> filtered out
    assert result == ["aa"]
    # line 3 sorts the caller's list in place
    assert lst == ["a", "aa", "aaa"]


def test_mixed_lengths_filter_and_length_sorting():
    lst = ["ab", "a", "aaa", "cd"]
    result = sorted_list_sum(lst)
    # odd-length "a" and "aaa" dropped; even-length kept, sorted by len
    assert result == ["ab", "cd"]


def test_length_key_reorders_beyond_lexicographic_sort():
    lst = ["aaaa", "bb"]
    result = sorted_list_sum(lst)
    # lexicographic sort gives ["aaaa", "bb"], but key=len gives ["bb", "aaaa"]
    assert result == ["bb", "aaaa"]


def test_equal_lengths_keep_lexicographic_order():
    lst = ["bb", "aa", "cc"]
    result = sorted_list_sum(lst)
    assert result == ["aa", "bb", "cc"]


def test_all_odd_length_strings_are_filtered_out():
    lst = ["a", "abc", "abcde"]
    result = sorted_list_sum(lst)
    assert result == []


def test_empty_list_skips_loop_body():
    lst = []
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == []
