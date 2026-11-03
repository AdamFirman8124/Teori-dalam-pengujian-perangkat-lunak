# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested — cover every line and branch (lines 3-18).

is_nested is a pure function (no I/O, no module state), so no monkeypatching
or teardown is required; each test is self-contained and leaves no state
behind.
"""

from f132 import is_nested


def test_is_nested_nested_pair_returns_true():
    # "[[]]": opening=[0, 1], closing reversed=[3, 2].
    # Both opening brackets match -> cnt == 2 -> True.
    # Covers: initialisation (3-4), scan loop (5), '[' branch (6-7),
    # ']' else-branch (9), reverse (10), counters (11-13), matching
    # loop (14), True branch of the match condition (15) and the
    # counting statements (16-17), and the return (18).
    assert is_nested("[[]]") is True


def test_is_nested_multiple_nested_returns_true():
    # "[[][]]": opening=[0, 1, 3, 4], closing reversed=[5, 4, 2].
    # Two matches -> cnt == 2 -> True.
    assert is_nested("[[][]]") is True


def test_is_nested_single_pair_returns_false():
    # "[]": exactly one match -> cnt == 1 < 2 -> False.
    assert is_nested("[]") is False


def test_is_nested_empty_string_returns_false():
    # "": neither the scan loop (line 5) nor the matching loop (line 14)
    # executes at all; cnt stays 0 -> False.
    assert is_nested("") is False


def test_is_nested_no_closing_brackets_returns_false():
    # "[[[": closing list is empty, so l == 0; the guard "i < l" is False
    # on the first iteration, covering the short-circuit False branch of
    # the first condition in line 15.
    assert is_nested("[[[") is False


def test_is_nested_unmatchable_opening_returns_false():
    # "[]][": opening=[0, 3], closing reversed=[2, 1], l == 2.
    # idx=0 matches (cnt=1, i=1); for idx=3 the guard "i < l" is True but
    # "idx < closing_bracket_index[i]" (3 < 1) is False, covering the
    # False branch of the second condition in line 15.
    assert is_nested("[]][") is False


def test_is_nested_flat_sequence_returns_false():
    # "[][]": opening=[0, 2], closing reversed=[3, 1].
    # Only the first opening bracket matches -> cnt == 1 -> False.
    assert is_nested("[][]") is False
