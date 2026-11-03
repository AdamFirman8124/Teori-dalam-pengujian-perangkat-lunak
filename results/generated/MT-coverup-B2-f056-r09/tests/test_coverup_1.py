# file: project/f056/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

"""Tests for f056.correct_bracketing.

The function is pure (no I/O, no module-level state), so no monkeypatching
or cleanup is required; each test is fully isolated.
"""

import pytest

from f056 import correct_bracketing


def test_empty_string_is_balanced():
    # Covers lines 3, 4 (loop skipped) and 11 (depth == 0 -> True).
    assert correct_bracketing("") is True


def test_single_open_bracket_is_unbalanced():
    # Covers lines 3-6, 9 (depth >= 0) and 11 (depth == 1 -> False).
    assert correct_bracketing("<") is False


def test_single_close_bracket_goes_negative():
    # Covers lines 3-5, 7-8 (else branch) and 9-10 (early return False).
    assert correct_bracketing(">") is False


def test_matched_pair_is_balanced():
    # Covers both branches of the character check and line 11 (True).
    assert correct_bracketing("<>") is True


def test_inverted_pair_goes_negative():
    # Covers the else branch followed by the early return on line 10.
    assert correct_bracketing("><") is False


def test_nested_brackets_are_balanced():
    # Exercises the '<' branch multiple times before closing.
    assert correct_bracketing("<<>>") is True


def test_sequential_pairs_are_balanced():
    # Exercises both branches alternating; depth never negative.
    assert correct_bracketing("<><>") is True


def test_unclosed_nested_brackets_are_unbalanced():
    # Ends with depth > 0, exercising line 11's False outcome.
    assert correct_bracketing("<<>") is False


def test_extra_closer_after_valid_prefix_goes_negative():
    # Depth reaches 0, then dips negative -> early return False.
    assert correct_bracketing("<>><") is False


@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("", True),
        ("<>", True),
        ("<<>>", True),
        ("<<<>>>", True),
        ("><", False),
        ("<<>", False),
        ("<>>", False),
        (">", False),
    ],
)
def test_parametrized_bracketing(brackets, expected):
    # Broad sweep ensuring every line/branch is hit repeatedly.
    assert correct_bracketing(brackets) is expected
