# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    """Covers lines 6-7: empty input returns None."""
    assert longest([]) is None


def test_longest_single_element():
    """Covers lines 9-12 with a single-element list."""
    assert longest(["hello"]) == "hello"


def test_longest_returns_longest_string():
    """Covers lines 9-12: the longest string is returned."""
    assert longest(["a", "abc", "ab"]) == "abc"


def test_longest_returns_first_of_tied_max_length():
    """Covers the loop skipping shorter strings and returning the first max-length one."""
    assert longest(["ab", "cd", "e"]) == "ab"


def test_longest_all_same_length_returns_first():
    """All strings tie for max length; the first is returned."""
    assert longest(["x", "y", "z"]) == "x"
