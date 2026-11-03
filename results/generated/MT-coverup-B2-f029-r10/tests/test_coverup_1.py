# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_basic():
    """Strings matching the prefix are kept, others are dropped."""
    result = filter_by_prefix(["abc", "abd", "bcd", "abcde"], "abc")
    assert result == ["abc", "abcde"]


def test_filter_by_prefix_no_matches():
    """When no string starts with the prefix, an empty list is returned."""
    result = filter_by_prefix(["hello", "world"], "xyz")
    assert result == []


def test_filter_by_prefix_empty_input():
    """An empty input list yields an empty output list."""
    result = filter_by_prefix([], "abc")
    assert result == []


def test_filter_by_prefix_empty_prefix():
    """An empty prefix matches every string, preserving order."""
    strings = ["b", "a", "c"]
    result = filter_by_prefix(strings, "")
    assert result == ["b", "a", "c"]


def test_filter_by_prefix_exact_match():
    """A string exactly equal to the prefix is included."""
    result = filter_by_prefix(["abc", "abcd"], "abc")
    assert result == ["abc", "abcd"]


def test_filter_by_prefix_case_sensitive():
    """Prefix matching is case-sensitive."""
    result = filter_by_prefix(["Apple", "apple"], "a")
    assert result == ["apple"]


def test_filter_by_prefix_does_not_mutate_input():
    """The input list is not modified by the function."""
    strings = ["abc", "def"]
    filter_by_prefix(strings, "abc")
    assert strings == ["abc", "def"]
