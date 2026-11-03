# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

"""Tests for f161.solve covering all lines and branches (lines 3-16)."""

from f161 import solve


def test_solve_swaps_case_when_letters_present():
    # Letters present -> flg becomes 1 -> returns swapped-case string (line 16).
    assert solve("ab") == "AB"
    assert solve("ABC") == "abc"


def test_solve_mixed_string_swaps_only_letters():
    # Non-letter characters are preserved; letters are case-swapped (lines 7-10).
    assert solve("#a@C") == "#A@c"
    assert solve("a1b2!") == "A1B2!"


def test_solve_reverses_when_no_letters():
    # No letters -> flg stays 0 -> returns reversed string (lines 14-15).
    assert solve("1234") == "4321"
    assert solve("!@#") == "#@!"


def test_solve_empty_string_returns_empty():
    # Empty input: loop bodies never run, flg == 0, reversed empty string is ''.
    assert solve("") == ""
