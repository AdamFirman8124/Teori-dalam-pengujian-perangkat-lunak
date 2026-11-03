# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested covering all lines and branches (lines 3-18).

is_nested is a pure function (no I/O, no globals, no side effects), so no
monkeypatching/teardown is required; each test is self-contained and leaves
no state behind.
"""

from f132 import is_nested


def test_is_nested_fully_nested_returns_true():
    # '[[]]': opening=[0,1], closing=[2,3] -> reversed [3,2]
    # idx=0: 0<3 -> cnt=1,i=1 ; idx=1: 1<2 -> cnt=2,i=2  => True
    # Exercises: both '[' branch (line 7), else branch (line 9),
    # reverse (line 10), and the if-condition True branch twice (lines 16-17).
    assert is_nested('[[]]') is True


def test_is_nested_deeply_nested_returns_true():
    # '[[[]]]': opening=[0,1,2], closing reversed [5,4,3]
    # cnt reaches 3 => True (condition True branch, lines 16-17).
    assert is_nested('[[[]]]') is True


def test_is_nested_single_pair_returns_false():
    # '[]': opening=[0], closing reversed [1]; idx=0: 0<1 -> cnt=1
    # cnt >= 2 is False (exercises lines 3-18 with a single match).
    assert is_nested('[]') is False


def test_is_nested_sequential_pairs_returns_false():
    # '[][]': opening=[0,2], closing reversed [3,1]
    # idx=0: 0<3 -> cnt=1,i=1 ; idx=2: i=1<2 but 2<1 is False
    # Covers the False branch of line 15 via 'idx >= closing_bracket_index[i]'.
    assert is_nested('[][]') is False


def test_is_nested_extra_openings_exhausts_closings_returns_true():
    # '[[]][[': opening=[0,1,4,5], closing reversed [3,2]
    # idx=0: 0<3 -> cnt=1 ; idx=1: 1<2 -> cnt=2 ;
    # idx=4: i=2 is not < l=2 -> False branch of line 15 via 'i >= l'.
    assert is_nested('[[]][[') is True


def test_is_nested_closings_before_openings_returns_false():
    # '][[': opening=[1,2], closing reversed [0]
    # idx=1: 1<0 False ; idx=2: 2<0 False -> cnt=0 => False
    # Exercises the False branch of line 15 for every iteration.
    assert is_nested('][[') is False


def test_is_nested_no_opening_brackets_returns_false():
    # '][': opening=[] so the second for loop body never runs; cnt=0 => False.
    assert is_nested('][') is False


def test_is_nested_empty_string_returns_false():
    # '': both loops see empty sequences; cnt=0 => False.
    assert is_nested('') is False


def test_is_nested_non_bracket_char_treated_as_closing():
    # '[x]': any non-'[' char goes to the else branch (line 9).
    # opening=[0], closing reversed [2,1]; idx=0: 0<2 -> cnt=1 => False.
    assert is_nested('[x]') is False
