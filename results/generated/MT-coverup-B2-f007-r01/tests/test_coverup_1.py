# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_mixed():
    """Covers line 6 and both branches of the comprehension condition:
    strings that contain the substring (True branch) and strings that
    do not (False branch)."""
    strings = ["apple", "banana", "grape", "pineapple"]
    result = filter_by_substring(strings, "apple")
    assert result == ["apple", "pineapple"]
    # Ensure the original list is not mutated
    assert strings == ["apple", "banana", "grape", "pineapple"]


def test_filter_by_substring_no_matches():
    """Covers the False branch of the condition for every element."""
    result = filter_by_substring(["abc", "def"], "xyz")
    assert result == []


def test_filter_by_substring_all_matches():
    """Covers the True branch of the condition for every element."""
    result = filter_by_substring(["abc", "abcd"], "abc")
    assert result == ["abc", "abcd"]


def test_filter_by_substring_empty_input():
    """Covers the case where the loop body never executes."""
    result = filter_by_substring([], "anything")
    assert result == []


def test_filter_by_substring_empty_substring():
    """An empty substring is contained in every string."""
    result = filter_by_substring(["a", "b"], "")
    assert result == ["a", "b"]
