# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

"""Tests for f007.filter_by_substring.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
operates only on local data, avoiding any state pollution.
"""

from typing import List

from f007 import filter_by_substring


def test_filter_by_substring_mixed_matches():
    """Both branches of the comprehension condition are exercised:
    some strings contain the substring (kept) and some do not (dropped)."""
    strings: List[str] = ["abc", "bcd", "cde", "abcde", "cab"]
    result = filter_by_substring(strings, "abc")
    assert result == ["abc", "abcde"]
    # Original input must be untouched (no in-place mutation).
    assert strings == ["abc", "bcd", "cde", "abcde", "cab"]


def test_filter_by_substring_no_matches():
    """Covers the False branch of the condition for every element."""
    strings: List[str] = ["bcd", "cde", "xyz"]
    result = filter_by_substring(strings, "abc")
    assert result == []


def test_filter_by_substring_all_matches():
    """Covers the True branch of the condition for every element."""
    strings: List[str] = ["abc", "xabcx", "abcabc"]
    result = filter_by_substring(strings, "abc")
    assert result == ["abc", "xabcx", "abcabc"]


def test_filter_by_substring_empty_input_list():
    """Empty input short-circuits the comprehension over zero items."""
    result = filter_by_substring([], "abc")
    assert result == []


def test_filter_by_substring_empty_substring_matches_all():
    """An empty substring is contained in every string."""
    strings: List[str] = ["abc", "bcd", ""]
    result = filter_by_substring(strings, "")
    assert result == ["abc", "bcd", ""]


def test_filter_by_substring_result_is_new_list():
    """The returned list is a fresh object, not the input list."""
    strings: List[str] = ["abc"]
    result = filter_by_substring(strings, "abc")
    assert result == strings
    assert result is not strings
