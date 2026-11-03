# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_mixed():
    """Covers line 6 with both branches of the comprehension condition:
    strings containing the substring (kept) and not containing it (filtered out)."""
    strings = ["apple", "banana", "grape", "pineapple"]
    result = filter_by_substring(strings, "apple")
    assert result == ["apple", "pineapple"]
    # Ensure the input list is not mutated
    assert strings == ["apple", "banana", "grape", "pineapple"]


def test_filter_by_substring_no_matches():
    """Covers line 6 with the condition always false (empty result)."""
    result = filter_by_substring(["dog", "cat"], "zebra")
    assert result == []


def test_filter_by_substring_empty_input():
    """Covers line 6 with an empty input list (loop body never runs)."""
    result = filter_by_substring([], "anything")
    assert result == []


def test_filter_by_substring_empty_substring():
    """An empty substring is contained in every string, so all are kept."""
    result = filter_by_substring(["a", "b", ""], "")
    assert result == ["a", "b", ""]


def test_filter_by_substring_exact_match():
    """A string equal to the substring contains it."""
    result = filter_by_substring(["abc", "abd"], "abc")
    assert result == ["abc"]
