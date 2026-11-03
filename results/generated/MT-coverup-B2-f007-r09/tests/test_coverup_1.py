# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

"""Tests for f007.filter_by_substring.

Line 6 (the return statement with the list comprehension) is executed by
every call below. The comprehension's condition ``substring in x`` has two
branches, both exercised by the mixed-match test; the empty-input test
covers the zero-iteration case.

The function under test is pure (no I/O, no globals, no side effects), so
no monkeypatching is required; tests additionally assert that the input
list is not mutated, guarding against state pollution.
"""

from typing import List

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_mixed_matches() -> None:
    """Covers both branches of the comprehension condition (true and false)."""
    strings: List[str] = ["abc", "bcd", "cde", "abcde"]
    result = filter_by_substring(strings, "bc")
    assert result == ["abc", "bcd", "abcde"]
    # Postcondition: original list is untouched (no state pollution).
    assert strings == ["abc", "bcd", "cde", "abcde"]


def test_filter_by_substring_no_matches() -> None:
    """Covers the false branch exclusively."""
    strings: List[str] = ["abc", "def"]
    result = filter_by_substring(strings, "xyz")
    assert result == []
    assert strings == ["abc", "def"]


def test_filter_by_substring_all_match() -> None:
    """Covers the true branch exclusively, preserving order."""
    strings: List[str] = ["abc", "xabcx", "ab"]
    result = filter_by_substring(strings, "abc")
    assert result == ["abc", "xabcx"]
    assert strings == ["abc", "xabcx", "ab"]


def test_filter_by_substring_empty_input() -> None:
    """Covers the zero-iteration case of the comprehension."""
    result = filter_by_substring([], "abc")
    assert result == []


def test_filter_by_substring_empty_substring() -> None:
    """An empty substring is contained in every string."""
    strings: List[str] = ["a", "b", ""]
    result = filter_by_substring(strings, "")
    assert result == ["a", "b", ""]
    assert strings == ["a", "b", ""]


def test_filter_by_substring_returns_new_list() -> None:
    """The result must be a fresh list, not an alias of the input."""
    strings: List[str] = ["abc"]
    result = filter_by_substring(strings, "abc")
    assert result == ["abc"]
    assert result is not strings
