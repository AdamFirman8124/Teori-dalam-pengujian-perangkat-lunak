# file: project/f012/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 0], [10, 11], [11, 10], [11, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[6, 7], [6, 9], [10, 11], [11, 10], [11, 12]]}

import pytest

from f012 import longest


def test_longest_empty_list_returns_none():
    """Covers lines 6-7: empty input short-circuits to None."""
    assert longest([]) is None


def test_longest_single_element():
    """Covers lines 9-12 with a single-element list."""
    assert longest(["only"]) == "only"


def test_longest_returns_first_of_max_length():
    """Covers lines 9-12, including the False branch of the length check
    (elements before the first longest one are skipped)."""
    assert longest(["a", "bb", "cc", "d"]) == "bb"


def test_longest_last_element_is_longest():
    """Covers lines 9-12 when the maximum-length element is last."""
    assert longest(["ab", "c", "def"]) == "def"


def test_longest_all_same_length_returns_first():
    """Covers lines 9-12 when all elements tie for max length."""
    assert longest(["x", "y", "z"]) == "x"
