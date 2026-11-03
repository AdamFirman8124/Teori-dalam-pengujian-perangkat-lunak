# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

"""Tests for f132.is_nested (HumanEval-style bracket nesting check).

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or fixture-based cleanup is required; each test is fully
isolated and leaves no state behind.

Coverage plan:
- Lines 3-18: exercised by every call below.
- Branch `string[i] == '['` True/False: strings containing both '[' and ']'.
- Branch `i < l and idx < closing_bracket_index[i]`:
    * True:            '[[]]'  (two successful matches -> True)
    * False via i < l: '[[['   (closing list exhausted, short-circuit)
    * False via idx < closing_bracket_index[i]: '[][' (match fails)
- Inner for-loop never entered: '' and ']]' (no opening brackets).
"""

import pytest

from f132 import is_nested


def test_is_nested_true_when_two_nested_pairs():
    # opening=[0,1], closing reversed=[3,2] -> two matches -> True
    assert is_nested('[[]]') is True
    assert is_nested('[[][]]') is True
    assert is_nested('[[]][[') is True


def test_is_nested_false_with_single_match():
    # Only one opening bracket can be matched -> cnt == 1 -> False
    assert is_nested('[]') is False
    assert is_nested('[][]') is False


def test_is_nested_false_when_closing_brackets_exhausted():
    # l == 0, so 'i < l' is False on the first iteration (short-circuit branch)
    assert is_nested('[[[') is False


def test_is_nested_false_when_match_condition_fails():
    # opening=[0,2], closing reversed=[3,1]: second iteration fails
    # 'idx < closing_bracket_index[i]' (2 < 1 is False)
    assert is_nested('[][') is False


def test_is_nested_false_with_no_opening_brackets():
    # Inner loop over opening_bracket_index never executes
    assert is_nested(']]') is False
    assert is_nested('') is False


def test_is_nested_mixed_non_bracket_characters():
    # Non-bracket characters take the 'else' branch (treated as closers)
    # opening=[0,3], closing reversed=[5,2,1]: only one match -> False
    assert is_nested('[a]b[c') is False
    # opening=[0,1,4], closing reversed=[5,2]: two matches -> True
    assert is_nested('[[x]y]') is True
