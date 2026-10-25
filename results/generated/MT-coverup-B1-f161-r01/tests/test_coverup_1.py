# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

import pytest

from f161 import solve


def test_solve_swaps_case_of_letters():
    assert solve("AbC") == "aBc"
    assert solve("Hello World!") == "hELLO wORLD!"


def test_solve_no_letters_returns_reversed():
    assert solve("1234!") == "!4321"
    assert solve("") == ""


def test_solve_mixed_letters_and_digits():
    # letters get swapped, digits stay in place, flg set so no reversal
    assert solve("a1b2") == "A1B2"


def test_solve_does_not_mutate_input():
    s = "aB"
    solve(s)
    assert s == "aB"
