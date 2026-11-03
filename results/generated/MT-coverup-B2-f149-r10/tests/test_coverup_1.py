# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_filters_out_odd_length_strings():
    # Covers lines 3-8, including the False branch of the len check (line 6)
    lst = ["aa", "a", "aaa"]
    result = sorted_list_sum(lst)
    assert result == ["aa"]


def test_sorted_list_sum_keeps_even_length_strings():
    # Covers the True branch of the len check (lines 6-7)
    lst = ["ab", "a", "aaa", "cd"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "cd"]


def test_sorted_list_sum_returns_list_sorted_by_length():
    # Covers line 8: final sorted(new_lst, key=len) reordering
    lst = ["abcd", "ab", "cd", "a"]
    result = sorted_list_sum(lst)
    assert result == ["ab", "cd", "abcd"]


def test_sorted_list_sum_empty_list():
    # Covers the for-loop exit branch without any iterations
    assert sorted_list_sum([]) == []


def test_sorted_list_sum_sorts_input_in_place():
    # Verifies the side effect of line 3 (lst.sort())
    lst = ["ccc", "a", "bb"]
    result = sorted_list_sum(lst)
    assert lst == ["a", "bb", "ccc"]
    assert result == ["bb"]


def test_sorted_list_sum_stable_order_for_equal_lengths():
    # Same-length even strings keep their alphabetical (pre-sorted) order
    lst = ["bb", "aa"]
    result = sorted_list_sum(lst)
    assert result == ["aa", "bb"]
