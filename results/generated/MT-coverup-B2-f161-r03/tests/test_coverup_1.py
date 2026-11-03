# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_solve_no_alpha_returns_reversed_string():
    # Covers lines 3-15, specifically the flg == 0 branch (lines 14-15):
    # no alphabetic characters means the result string is returned reversed.
    assert solve("12345") == "54321"
    assert solve("!@# $%") == "%$ #@!"
    assert solve("") == ""  # empty string also hits the flg == 0 branch


def test_solve_with_alpha_returns_swapcased_string():
    # Covers lines 3-13 and line 16 (flg == 1): alphabetic characters are
    # swapcased, non-alphabetic characters are left unchanged, and the
    # result is NOT reversed.
    assert solve("abCD") == "ABcd"
    assert solve("a1b2!") == "A1B2!"
    assert solve("Hello, World!") == "hELLO, wORLD!"
