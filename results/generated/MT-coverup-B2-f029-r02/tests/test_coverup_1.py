# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_matching_and_non_matching():
    """Covers both branches of the comprehension condition: items that
    start with the prefix (True branch) and items that don't (False branch)."""
    strings = ["abc", "bcd", "cde", "array"]
    result = filter_by_prefix(strings, "a")
    assert result == ["abc", "array"]
    # Original list is untouched (no side effects)
    assert strings == ["abc", "bcd", "cde", "array"]


def test_filter_by_prefix_no_matches():
    """Covers the case where the condition is False for every item."""
    strings = ["bcd", "cde"]
    result = filter_by_prefix(strings, "a")
    assert result == []


def test_filter_by_prefix_empty_input():
    """Covers the case where the iterable is empty (loop body never runs,
    but line 6 still executes and returns an empty list)."""
    result = filter_by_prefix([], "a")
    assert result == []


def test_filter_by_prefix_empty_prefix_matches_all():
    """Covers the case where every string starts with the empty prefix."""
    strings = ["abc", "def", ""]
    result = filter_by_prefix(strings, "")
    assert result == ["abc", "def", ""]


def test_filter_by_prefix_returns_new_list():
    """Verifies postcondition: the returned list is a new list object,
    not an alias of the input."""
    strings = ["ax", "bx"]
    result = filter_by_prefix(strings, "a")
    assert result is not strings
    assert result == ["ax"]


def test_filter_by_prefix_prefix_longer_than_items():
    """Covers items shorter than the prefix; startswith returns False."""
    result = filter_by_prefix(["a", "ab", "abc"], "abc")
    assert result == ["abc"]
