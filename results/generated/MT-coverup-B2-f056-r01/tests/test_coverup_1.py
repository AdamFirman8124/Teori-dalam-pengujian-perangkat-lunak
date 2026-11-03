# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f056 import correct_bracketing


def test_empty_string_is_balanced():
    # Covers lines 3, 4 (loop skipped) and 11 (True branch).
    assert correct_bracketing("") is True


def test_single_opening_bracket_is_unbalanced():
    # Covers lines 3-6 (increment branch) and 11 (False branch).
    assert correct_bracketing("<") is False


def test_single_closing_bracket_goes_negative():
    # Covers lines 3-5, 7-8 (decrement branch) and 9-10 (early return False).
    assert correct_bracketing(">") is False


def test_simple_pair_is_balanced():
    # Covers both the increment and decrement branches, ending balanced.
    assert correct_bracketing("<>") is True


def test_closing_before_opening_goes_negative():
    # Covers line 10 (early return False) after a decrement.
    assert correct_bracketing("><") is False


def test_nested_brackets_are_balanced():
    # Exercises repeated increments/decrements with a positive final depth of 0.
    assert correct_bracketing("<<>>") is True


def test_sequence_of_pairs_is_balanced():
    # Exercises multiple loop iterations returning to zero depth.
    assert correct_bracketing("<><>") is True


def test_extra_opening_bracket_is_unbalanced():
    # Final depth positive, so line 11 returns False without ever going negative.
    assert correct_bracketing("<<>") is False
