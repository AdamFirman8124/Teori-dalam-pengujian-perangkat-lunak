# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

"""Tests for f149.sorted_list_sum.

These tests execute every line/branch (lines 3-8):
  - line 3: in-place sort of the input list
  - lines 5-6: loop over items, even-length check (taken AND not taken)
  - line 7: append of an even-length item
  - line 8: return sorted by length (including length ties)

Each test builds its own fresh list, so there is no shared state to
pollute between tests (no monkeypatching needed).
"""

from f149 import sorted_list_sum


def test_keeps_even_length_strings_and_sorts_by_length():
    original = ["aa", "a", "aaa"]
    result = sorted_list_sum(original)
    # Only the even-length item survives, ordered by length.
    assert result == ["aa"]
    # Verifies line 3: the input list is sorted in place.
    assert original == ["a", "aa", "aaa"]


def test_false_branch_of_length_check_is_exercised():
    # "a" (len 1) and "aaa" (len 3) exercise the False branch of the
    # even-length test on line 6; only "ab"/"cd" (len 2) are kept.
    result = sorted_list_sum(["ab", "a", "aaa", "cd"])
    assert result == ["ab", "cd"]


def test_length_ties_preserve_lexicographic_order():
    # All strings have even length; after sorting by key=len (all equal),
    # the stable sort must preserve the lexicographic order from line 3.
    result = sorted_list_sum(["cc", "bb", "aa"])
    assert result == ["aa", "bb", "cc"]


def test_all_odd_length_strings_yield_empty_list():
    # Every item fails the even-length check, so the loop appends nothing.
    result = sorted_list_sum(["a", "abc", "abcde"])
    assert result == []


def test_empty_list_returns_empty_list():
    # Covers the branch where the loop body never runs.
    assert sorted_list_sum([]) == []


def test_result_is_sorted_by_length_across_groups():
    # Mixed lengths among the even ones: 2-letter before 4-letter items.
    result = sorted_list_sum(["dddd", "bb", "c", "aa"])
    assert result == ["aa", "bb", "dddd"]
