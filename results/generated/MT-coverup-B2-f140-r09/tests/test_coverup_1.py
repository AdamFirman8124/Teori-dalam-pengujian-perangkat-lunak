# file: project/f140/__init__.py:1-22
# asked: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22], "branches": [[6, 7], [6, 18], [7, 8], [7, 10], [10, 11], [10, 12], [12, 13], [12, 15], [18, 19], [18, 20], [20, 21], [20, 22]]}

import pytest

from f140 import fix_spaces


# fix_spaces is a pure function (no I/O, no globals, no side effects),
# so no monkeypatching/cleanup is required to avoid state pollution.


@pytest.mark.parametrize(
    "text, expected",
    [
        # Empty input: while-loop body never runs, no trailing branch taken.
        ("", ""),
        # No spaces at all: covers inner else (line 15) and no trailing branch.
        ("abc", "abc"),
        # Single space before a char: covers inner elif end-start > 0 (lines 12-13).
        ("a b", "a_b"),
        # Two spaces before a char: covers inner elif end-start > 0 (lines 12-13).
        ("a  b", "a__b"),
        # Three spaces before a char: covers inner if end-start > 2 (lines 10-11).
        ("a   b", "a-b"),
        # Leading spaces: spaces counted from the initial start=0.
        ("  a", "__a"),
        # Trailing single space: covers outer elif end-start > 0 (lines 20-21);
        # the function appends exactly one "_" on the trailing branch.
        ("a ", "a_"),
        # Trailing two spaces: end-start == 2, so still the outer elif branch
        # (lines 20-21), which appends only a single "_".
        ("a  ", "a_"),
        # Trailing three spaces: end-start == 3, covers outer if end-start > 2
        # (lines 18-19), which appends "-".
        ("a   ", "a-"),
        # Only spaces: covers outer if end-start > 2 (lines 18-19).
        ("   ", "-"),
        # Single space only: covers outer elif end-start > 0 (lines 20-21).
        (" ", "_"),
        # Mixed run lengths in one string: exercises all inner branches together.
        ("a b  c   d", "a_b__c-d"),
    ],
)
def test_fix_spaces(text, expected):
    assert fix_spaces(text) == expected


def test_fix_spaces_returns_new_string():
    # Postcondition: a new string object is returned, input is not mutated.
    text = "a   b"
    result = fix_spaces(text)
    assert result == "a-b"
    assert result is not text
    assert text == "a   b"


def test_fix_spaces_result_type():
    # Postcondition: result is always a str, even for empty input.
    assert isinstance(fix_spaces(""), str)
    assert isinstance(fix_spaces("x y"), str)
