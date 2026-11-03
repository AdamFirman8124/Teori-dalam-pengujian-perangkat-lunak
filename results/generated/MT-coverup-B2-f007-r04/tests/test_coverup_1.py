# file: project/f007/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f007 import filter_by_substring


def test_filter_by_substring_mixed():
    """Covers line 6 (the list comprehension) with both branch outcomes:
    elements that contain the substring and elements that do not."""
    strings = ["apple", "banana", "grape", "pineapple", "cherry"]
    result = filter_by_substring(strings, "apple")
    assert result == ["apple", "pineapple"]
    # Postcondition: every returned element contains the substring
    assert all("apple" in x for x in result)
    # Postcondition: order and multiplicity of matches are preserved
    assert result == [x for x in strings if "apple" in x]
    # Original input is not mutated
    assert strings == ["apple", "banana", "grape", "pineapple", "cherry"]


def test_filter_by_substring_no_matches():
    """Covers line 6 with the comprehension yielding an empty result
    (the 'substring in x' condition is False for every element)."""
    result = filter_by_substring(["dog", "cat"], "zebra")
    assert result == []


def test_filter_by_substring_empty_input():
    """Covers line 6 with an empty input list (loop body never runs,
    but the comprehension statement itself still executes)."""
    result = filter_by_substring([], "anything")
    assert result == []


def test_filter_by_substring_empty_substring():
    """An empty substring is contained in every string, so all elements
    are kept; exercises the True branch for every element."""
    strings = ["a", "b", ""]
    result = filter_by_substring(strings, "")
    assert result == ["a", "b", ""]


def test_filter_by_substring_duplicates_and_order():
    """Ensures duplicates are kept and relative order is preserved."""
    strings = ["xx", "yy", "xx", "zz", "xx"]
    result = filter_by_substring(strings, "xx")
    assert result == ["xx", "xx", "xx"]
