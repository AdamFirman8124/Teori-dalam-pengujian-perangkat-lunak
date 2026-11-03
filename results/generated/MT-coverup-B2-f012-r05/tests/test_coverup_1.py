# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

from typing import List, Optional

import pytest

from f012 import longest


def test_longest_empty_list_returns_none() -> None:
    """Covers lines 6-7: empty input short-circuits to None."""
    result: Optional[str] = longest([])
    assert result is None


def test_longest_single_string() -> None:
    """Covers lines 9-12 with a single-element list."""
    result: Optional[str] = longest(["hello"])
    assert result == "hello"


def test_longest_returns_first_longest() -> None:
    """Covers lines 9-12: maxlen computed, loop finds first string of max length."""
    result: Optional[str] = longest(["a", "bb", "c", "dd"])
    assert result == "bb"


def test_longest_tie_returns_first_of_max_length() -> None:
    """Covers the loop continuing past non-max strings and returning the first max-length one."""
    result: Optional[str] = longest(["x", "aa", "b", "cc"])
    assert result == "aa"


def test_longest_all_same_length_returns_first() -> None:
    """All strings tie for max length; the first one must be returned."""
    result: Optional[str] = longest(["ab", "cd", "ef"])
    assert result == "ab"


def test_longest_longest_at_end() -> None:
    """The longest string is the last element; loop must reach it."""
    result: Optional[str] = longest(["a", "bc", "def"])
    assert result == "def"
