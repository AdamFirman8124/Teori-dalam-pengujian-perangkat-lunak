# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


def test_int_to_mini_roman_basic_symbols():
    # Exercises lines 3-16, including the inner `while div` loop (lines 12-14)
    # and the outer `while number` loop terminating (line 9 false branch).
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(9) == "ix"


def test_int_to_mini_roman_tens_and_hundreds():
    # Covers every entry of the num/sym tables (lines 3-5).
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"


def test_int_to_mini_roman_thousands():
    # Reaches i = 12 (the "M" symbol) with div > 0.
    assert int_to_mini_roman(1000) == "m"
    assert int_to_mini_roman(3000) == "mmm"


def test_int_to_mini_roman_repeated_symbols():
    # Forces the inner `while div` loop (lines 12-14) to iterate several times.
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(3888) == "mmmdccclxxxviii"


def test_int_to_mini_roman_mixed_compositions():
    # 19 hits the `while div` false branch at i = 12 (19 // 1000 == 0),
    # then the true branch at i = 9 and i = 8, covering both branches
    # of both loops plus the final return (line 16).
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(3999) == "mmmcmxcix"
