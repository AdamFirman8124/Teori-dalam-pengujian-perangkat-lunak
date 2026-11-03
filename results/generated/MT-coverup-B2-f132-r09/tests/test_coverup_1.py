# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested.

The function is pure (no module state, no I/O), so no monkeypatching or
teardown is required; each test is fully isolated and leaves no state behind.

Coverage plan:
- lines 3-5, 10-14, 18: executed by every call below.
- line 6-7 (if string[i] == '[' -> True): '[[]]', '[[['.
- line 9 (else branch): '][', '[]', '[][]', '[[]]['.
- line 15-17 (if i < l and idx < closing_bracket_index[i] -> True): '[[]]'.
- line 15 (condition False because idx >= closing_bracket_index[i]): ']['.
- line 15 (condition False because i >= l, empty closing list): '[[['.
- loop at line 5 never entered: ''.
"""

import pytest

from f132 import is_nested


def test_fully_nested_returns_true():
    # opening=[0,1], closing=[2,3] -> reversed [3,2]
    # idx=0 matches 3, idx=1 matches 2 -> cnt == 2 -> True
    assert is_nested('[[]]') is True


def test_nested_with_trailing_unmatched_opener_returns_true():
    # opening=[0,1,4], closing reversed=[5,3,2]
    # idx=0 and idx=1 match -> cnt == 2 -> True; idx=4 exercises the
    # False side of 'idx < closing_bracket_index[i]' with i < l still true.
    assert is_nested('[[]][') is True


def test_single_pair_returns_false():
    # Only one match possible -> cnt == 1 -> False
    assert is_nested('[]') is False


def test_two_disjoint_pairs_returns_false():
    # opening=[0,2], closing reversed=[3,1]
    # idx=0 matches 3 (cnt=1); idx=2 fails 'idx < closing[1]' -> cnt stays 1
    assert is_nested('[][]') is False


def test_closing_before_opening_returns_false():
    # opening=[1], closing reversed=[0]; idx=1 fails 'idx < closing[0]'
    # -> cnt == 0 -> False (covers the False branch of the second if
    # through its right-hand operand).
    assert is_nested('][') is False


def test_only_opening_brackets_returns_false():
    # closing_bracket_index is empty -> l == 0 -> 'i < l' is False for
    # every idx (covers the False branch of the second if through its
    # left-hand operand).
    assert is_nested('[[[') is False


def test_empty_string_returns_false():
    # No brackets at all: both loops never execute, cnt == 0 -> False.
    assert is_nested('') is False


def test_result_is_always_a_bool():
    # Postcondition: the return value is a real bool, not just truthy.
    assert isinstance(is_nested('[[]]'), bool)
    assert isinstance(is_nested(']['), bool)
