# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


@pytest.mark.parametrize(
    "text, expected",
    [
        # Empty string: loop never runs, trailing check sees end - start == 0.
        ("", ""),
        # No spaces at all: only the else branch at line 15 is taken.
        ("abc", "abc"),
        # Single non-space char.
        ("a", "a"),
        # Run of exactly 2 spaces before a char: line 13 branch ("_" * 2).
        ("ab  cd", "ab__cd"),
        # Run of exactly 1 space before a char: line 13 branch ("_" * 1).
        ("a b", "a_b"),
        # Run of 3 spaces before a char: line 11 branch ("-" + char).
        ("a   b", "a-b"),
        # Run of more than 3 spaces before a char: line 11 branch again.
        ("a     b", "a-b"),
        # Trailing run of exactly 2 spaces: line 21 branch (single "_").
        ("ab  ", "ab_"),
        # Trailing run of exactly 1 space: line 21 branch.
        ("ab ", "ab_"),
        # Trailing run of 3 spaces: line 19 branch (single "-").
        ("ab   ", "ab-"),
        # Trailing run of more than 3 spaces: line 19 branch again.
        ("ab      ", "ab-"),
        # Mixed: internal long run replaced by "-", short internal run by "_",
        # and trailing short run by "_".
        ("a   b c  ", "a-b_c_"),
        # Spaces only at the very start, followed by a char (long run).
        ("   a", "-a"),
        # Spaces only at the very start, short run (preserves count).
        ("  a", "__a"),
        # String consisting only of a long space run: only trailing branch fires.
        ("    ", "-"),
        # String consisting only of a short space run: only trailing branch fires.
        ("  ", "_"),
    ],
)
def test_fix_spaces_all_branches(text, expected):
    assert fix_spaces(text) == expected


def test_fix_spaces_returns_new_string_no_mutation():
    text = "a   b  "
    result = fix_spaces(text)
    # Input is not mutated (strings are immutable, but verify value preserved).
    assert text == "a   b  "
    # Long internal run -> "-", short trailing run -> "_".
    assert result == "a-b_"
    # Result is a fresh string object, not the input.
    assert result is not text
