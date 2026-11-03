# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    """Covers lines 6-7: the empty-list branch returns None."""
    assert longest([]) is None


def test_longest_single_string_returns_it():
    """Covers lines 9-12 with a single-element list."""
    assert longest(["hello"]) == "hello"


def test_longest_returns_longest_string():
    """Covers lines 9-12: maxlen computed and matching string returned."""
    assert longest(["a", "abc", "ab"]) == "abc"


def test_longest_returns_first_on_tie():
    """Covers lines 10-12: the first string of maximal length is returned."""
    assert longest(["ab", "cd", "e"]) == "ab"


def test_longest_returns_none_for_empty_and_value_for_nonempty():
    """Both branches of line 6 exercised in one flow."""
    assert longest([]) is None
    assert longest(["x", "yy"]) == "yy"
