# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested covering all previously uncovered lines (3-18)
and every branch, including both loop bodies, both sides of the
'if string[i] == '[' check, both short-circuit outcomes of
'i < l and idx < closing_bracket_index[i]', and both return values.

is_nested is a pure function (no globals, I/O or mutable module state),
so no monkeypatching/teardown is required; each test is fully isolated.
"""

from f132 import is_nested


def test_is_nested_true_when_two_pairs_match():
    # '[[]]': opening indices [0, 1], closings reversed [3, 2].
    # idx=0 matches closing 3 (cnt=1), idx=1 matches closing 2 (cnt=2).
    # Covers: first loop (both if/else arms), condition-true arm, lines 16-17,
    # and the True return of line 18.
    assert is_nested('[[]]') is True


def test_is_nested_false_with_single_pair():
    # '[]': opening [0], closings reversed [1]; only one match -> cnt == 1.
    # Covers the False return of line 18.
    assert is_nested('[]') is False


def test_is_nested_false_when_open_comes_after_next_close():
    # '[][]': opening [0, 2], closings reversed [3, 1].
    # idx=0 matches (cnt=1, i=1); idx=2: 'i < l' is True but
    # '2 < closing_bracket_index[1] (== 1)' is False -> exercises the
    # second-condition-false branch of line 15.
    assert is_nested('[][]') is False


def test_is_nested_true_short_circuits_when_i_reaches_l():
    # '[[]][[': opening [0, 1, 4, 5], closings reversed [3, 2], l == 2.
    # idx=0 and idx=1 match (cnt=2); for idx=4, 'i < l' is False
    # (i == 2 == l) -> exercises the short-circuit-false branch of line 15.
    assert is_nested('[[]][[') is True


def test_is_nested_empty_string():
    # '': neither the character loop (line 5) nor the opening-index loop
    # (line 14) executes its body; returns False.
    assert is_nested('') is False


def test_is_nested_only_closing_brackets():
    # ']]': the else-branch (line 9) runs, opening_bracket_index stays
    # empty so the loop on line 14 never executes; returns False.
    assert is_nested(']]') is False
