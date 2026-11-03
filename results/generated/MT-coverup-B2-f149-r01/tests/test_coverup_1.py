# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_filters_odd_and_sorts():
    """Covers lines 3-8: in-place sort, loop, both branches of the even-length
    check, and the final sort by length."""
    lst = ["aa", "a", "aaa", "ab", "abc"]
    result = sorted_list_sum(lst)
    # "a" and "aaa" and "abc" have odd length -> filtered out
    # "aa" and "ab" remain, sorted by length (both len 2, stable -> lexicographic)
    assert result == ["aa", "ab"]
    # the function sorts the input list in place (line 3)
    assert lst == ["a", "aa", "aaa", "ab", "abc"]


def test_sorted_list_sum_length_ordering():
    """Verifies the final sort is by length, not lexicographic."""
    lst = ["dddd", "bb", "cccc", "aa"]
    result = sorted_list_sum(lst)
    # all even lengths kept; sorted by length: 2, 2, 4, 4
    # ties keep the lexicographic order established by lst.sort()
    assert result == ["aa", "bb", "cccc", "dddd"]


def test_sorted_list_sum_all_odd_lengths():
    """Covers the False branch of the even-length check for every element."""
    lst = ["a", "abc", "abcde"]
    result = sorted_list_sum(lst)
    assert result == []
    # input was still sorted in place
    assert lst == ["a", "abc", "abcde"]


def test_sorted_list_sum_empty_list():
    """Covers the zero-iteration branch of the for loop."""
    lst = []
    result = sorted_list_sum(lst)
    assert result == []
    assert lst == []


def test_sorted_list_sum_single_element():
    lst = ["ab"]
    result = sorted_list_sum(lst)
    assert result == ["ab"]
    assert lst == ["ab"]


def test_sorted_list_sum_does_not_leak_state():
    """Each call works on its own input; no shared/module-level state is used."""
    first = sorted_list_sum(["bb", "aa"])
    second = sorted_list_sum(["dd", "cc"])
    assert first == ["aa", "bb"]
    assert second == ["cc", "dd"]
