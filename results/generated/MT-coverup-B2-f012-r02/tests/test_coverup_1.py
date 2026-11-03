# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    """Covers lines 6-7: the truthiness check on an empty list and the None return."""
    assert longest([]) is None


def test_longest_single_element():
    """Covers lines 9-12 with a minimal non-empty input."""
    assert longest(["hello"]) == "hello"


def test_longest_returns_longest_string():
    """Covers the loop where the first element is not the longest (line 11 False branch)."""
    assert longest(["a", "bb", "ccc"]) == "ccc"


def test_longest_returns_first_among_ties():
    """Covers the loop returning on the first element (line 11 True branch immediately)."""
    assert longest(["aa", "bb", "c"]) == "aa"


def test_longest_skips_shorter_then_returns():
    """Covers iterating past several shorter strings before hitting the max-length one."""
    assert longest(["a", "abc", "ab", "xyz"]) == "abc"


def test_longest_empty_strings_still_nonempty_list():
    """A non-empty list of empty strings must not take the 'not strings' branch."""
    assert longest(["", ""]) == ""
