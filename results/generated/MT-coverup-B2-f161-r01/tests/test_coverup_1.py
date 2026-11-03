# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

import pytest

from f161 import solve


def test_solve_all_alpha_swaps_case():
    # Covers lines 3-9 (isalpha True branch), 10-13, and the final return (line 16).
    assert solve("abcd") == "ABCD"


def test_solve_mixed_case_swap():
    # Verifies swapcase behavior on mixed-case letters.
    assert solve("AbCdEf") == "aBcDeF"


def test_solve_alpha_with_non_alpha_keeps_order():
    # Covers the isalpha False branch (line 7) with non-letter characters;
    # flg becomes 1 so the swapped (non-reversed) string is returned.
    assert solve("a1b2!") == "A1B2!"


def test_solve_no_alpha_returns_reversed():
    # Covers the flg == 0 branch (lines 14-15): no letters, so the
    # original characters are returned reversed.
    assert solve("12345") == "54321"


def test_solve_no_alpha_with_symbols_returns_reversed():
    # Non-alpha characters, including spaces and punctuation,
    # still take the flg == 0 reversal path.
    # "  #!@" reversed is "@!#  ".
    assert solve("  #!@") == "@!#  "


def test_solve_empty_string():
    # Empty input: loop never runs, flg stays 0, reversed empty string
    # is an empty string.
    assert solve("") == ""


def test_solve_unicode_alpha():
    # Unicode letters are also detected by isalpha and swapped;
    # ensures the flg == 1 return path with non-ASCII input.
    assert solve("naïve") == "NAÏVE"
