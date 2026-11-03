# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_matching_and_non_matching():
    """Covers line 6 with both branches of the startswith condition."""
    strings = ["apple", "banana", "avocado", "cherry"]
    result = filter_by_prefix(strings, "a")
    # Only strings starting with "a" are kept, in original order.
    assert result == ["apple", "avocado"]


def test_filter_by_prefix_no_matches():
    """Covers line 6 when the startswith condition is False for every item."""
    strings = ["banana", "cherry"]
    result = filter_by_prefix(strings, "x")
    assert result == []


def test_filter_by_prefix_empty_input():
    """Covers line 6 with an empty input list (comprehension iterates zero times)."""
    assert filter_by_prefix([], "a") == []


def test_filter_by_prefix_empty_prefix():
    """Covers line 6 with an empty prefix (every string matches)."""
    strings = ["apple", "banana"]
    result = filter_by_prefix(strings, "")
    assert result == ["apple", "banana"]


def test_filter_by_prefix_does_not_mutate_input():
    """Ensures the function is pure: the input list is left unchanged."""
    strings = ["apple", "banana"]
    snapshot = list(strings)
    result = filter_by_prefix(strings, "a")
    assert result == ["apple"]
    assert strings == snapshot
