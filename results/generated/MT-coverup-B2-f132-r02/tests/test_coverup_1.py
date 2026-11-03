# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested — covering lines 3-18 and all branches.

is_nested is a pure function (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; each test is fully isolated.
"""

import pytest

from f132 import is_nested


def test_is_nested_nested_pairs_returns_true():
    # '[[]]': opening=[0,1], closing reversed=[3,2]
    # idx=0 matches closing 3 (cnt=1, i=1); idx=1 matches closing 2 (cnt=2)
    # Exercises lines 3-18, both arms of the char branch, and the True
    # outcome of the `i < l and idx < closing_bracket_index[i]` condition.
    assert is_nested('[[]]') is True


def test_is_nested_deeply_nested_returns_true():
    # '[[[]]]': three opening brackets each find a later closing bracket.
    assert is_nested('[[[]]]') is True


def test_is_nested_single_pair_returns_false():
    # '[]': only one match -> cnt == 1 -> False (condition True branch taken
    # once, but the cnt >= 2 threshold is not met).
    assert is_nested('[]') is False


def test_is_nested_no_opening_brackets_returns_false():
    # '][': opening_bracket_index is empty, so the second for-loop body
    # (lines 15-17) never runs; cnt stays 0.
    assert is_nested('][') is False


def test_is_nested_no_closing_brackets_returns_false():
    # '[[[': closing_bracket_index is empty -> l == 0, so `i < l` is False
    # for every idx (False branch of the line-15 condition via its first clause).
    assert is_nested('[[[') is False


def test_is_nested_unmatched_opening_returns_false():
    # '[][]': closing reversed=[3,1]; idx=0 matches 3 (cnt=1, i=1), but for
    # idx=2 the second clause `idx < closing_bracket_index[i]` (2 < 1) is
    # False -> cnt stays 1.
    assert is_nested('[][]') is False


def test_is_nested_empty_string_returns_false():
    # '': both loops execute zero iterations; falls straight through to
    # `return cnt >= 2` with cnt == 0.
    assert is_nested('') is False


def test_is_nested_exhausted_closing_list_returns_false():
    # '[][': closing reversed=[1]; idx=0 matches (cnt=1, i=1), then for
    # idx=2 `i < l` is False (1 < 1) -> short-circuit False branch.
    assert is_nested('[][') is False
