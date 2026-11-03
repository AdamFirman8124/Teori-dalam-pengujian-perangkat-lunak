# file: project/f029/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

"""Tests for f029.filter_by_prefix.

These tests call the function directly so that line 6 (the list
comprehension return) executes, covering both branches of the
comprehension condition (elements that match the prefix and elements
that do not), as well as edge cases (empty input list, empty prefix,
prefix equal to a whole string).

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; importing
the module and calling the function leaves no state behind.
"""

from typing import List

import pytest

from f029 import filter_by_prefix


def test_filter_by_prefix_matches_and_non_matches() -> None:
    """Both comprehension branches execute: some items match, some don't."""
    strings: List[str] = ["abc", "abd", "bcd", "abcd", "xyz"]
    result = filter_by_prefix(strings, "abc")
    assert result == ["abc", "abcd"]
    # Original list must not be mutated (pure function postcondition).
    assert strings == ["abc", "abd", "bcd", "abcd", "xyz"]


def test_filter_by_prefix_no_matches() -> None:
    """The comprehension's false branch executes for every element."""
    result = filter_by_prefix(["hello", "world"], "zzz")
    assert result == []


def test_filter_by_prefix_empty_input_list() -> None:
    """An empty input yields an empty output without errors."""
    result = filter_by_prefix([], "abc")
    assert result == []


def test_filter_by_prefix_empty_prefix_matches_all() -> None:
    """Every string starts with the empty prefix, so all are kept."""
    strings = ["alpha", "beta", ""]
    result = filter_by_prefix(strings, "")
    assert result == ["alpha", "beta", ""]


def test_filter_by_prefix_prefix_equals_whole_string() -> None:
    """A prefix equal to the entire string still matches (startswith)."""
    result = filter_by_prefix(["abc", "abcd"], "abc")
    assert result == ["abc", "abcd"]


def test_filter_by_prefix_result_is_new_list() -> None:
    """The result is a distinct list object, not the input list."""
    strings = ["a", "b"]
    result = filter_by_prefix(strings, "")
    assert result == strings
    assert result is not strings


def test_filter_by_prefix_preserves_order_and_duplicates() -> None:
    """Order is preserved and duplicates are kept."""
    strings = ["ab", "cd", "ab", "ef"]
    result = filter_by_prefix(strings, "ab")
    assert result == ["ab", "ab"]


@pytest.mark.parametrize(
    "strings,prefix,expected",
    [
        (["prefix_one", "other", "prefix_two"], "prefix", ["prefix_one", "prefix_two"]),
        (["a"], "b", []),
        ([], "", []),
        (["case"], "Case", []),  # startswith is case-sensitive
    ],
)
def test_filter_by_prefix_parametrized(
    strings: List[str], prefix: str, expected: List[str]
) -> None:
    """Parametrized coverage of line 6 across many input shapes."""
    assert filter_by_prefix(strings, prefix) == expected
