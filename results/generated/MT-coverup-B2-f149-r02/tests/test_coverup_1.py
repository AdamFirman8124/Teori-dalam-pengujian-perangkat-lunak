# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_mixed_lengths_filters_odd_and_sorts_by_length():
    # Covers: sort (line 3), init (4), loop (5), both branches of the
    # even-length check (6), append (7), and final return (8).
    result = sorted_list_sum(["ab", "a", "aaa", "cd"])
    assert result == ["ab", "cd"]


def test_all_even_lengths_sorted_by_length():
    result = sorted_list_sum(["dddd", "bb", "aa", "cc"])
    assert result == ["aa", "bb", "cc", "dddd"]


def test_equal_lengths_keep_lexicographic_order():
    # Stable sort by len preserves the lexicographic order from lst.sort().
    result = sorted_list_sum(["dd", "cc", "bb", "aa"])
    assert result == ["aa", "bb", "cc", "dd"]


def test_no_even_length_strings_returns_empty():
    # Exercises the False branch of the length check for every element.
    result = sorted_list_sum(["a", "bbb", "abcde"])
    assert result == []


def test_empty_list_returns_empty():
    result = sorted_list_sum([])
    assert result == []


def test_input_list_is_sorted_in_place():
    # lst.sort() mutates the caller's list; verify that side effect too.
    lst = ["ccc", "a", "bb"]
    result = sorted_list_sum(lst)
    assert lst == ["a", "bb", "ccc"]
    assert result == ["bb"]
