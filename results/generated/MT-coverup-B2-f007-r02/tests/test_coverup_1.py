# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_mixed_matches():
    """Covers both branches of the comprehension condition: some strings
    contain the substring (kept) and some do not (filtered out)."""
    strings = ["apple", "banana", "grape", "pineapple"]
    result = filter_by_substring(strings, "apple")
    assert result == ["apple", "pineapple"]


def test_filter_by_substring_no_matches():
    """Covers the false branch of the condition for every element."""
    strings = ["dog", "cat", "bird"]
    result = filter_by_substring(strings, "fish")
    assert result == []


def test_filter_by_substring_all_match():
    """Covers the true branch of the condition for every element."""
    strings = ["abc", "abcd", "xabcx"]
    result = filter_by_substring(strings, "abc")
    assert result == ["abc", "abcd", "xabcx"]


def test_filter_by_substring_empty_input_list():
    """Covers iterating over an empty list (comprehension yields [])."""
    result = filter_by_substring([], "anything")
    assert result == []


def test_filter_by_substring_empty_substring():
    """An empty substring is contained in every string, so all are kept."""
    strings = ["a", "b", "c"]
    result = filter_by_substring(strings, "")
    assert result == ["a", "b", "c"]


def test_filter_by_substring_does_not_mutate_input():
    """Verifies the function is pure: the input list is left unchanged."""
    strings = ["hello", "world"]
    original = list(strings)
    result = filter_by_substring(strings, "hello")
    assert strings == original
    assert result == ["hello"]
    assert result is not strings
