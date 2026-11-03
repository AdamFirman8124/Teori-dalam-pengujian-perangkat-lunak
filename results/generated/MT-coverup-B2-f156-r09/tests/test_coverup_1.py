# file: project/f156/__init__.py:1-16
# asked: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}
# gained: {"lines": [3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[9, 10], [9, 16], [12, 13], [12, 15]]}

import pytest

from f156 import int_to_mini_roman


def test_single_symbols_cover_all_list_entries():
    # Exercises lines 3-8 (setup), 9-11 (outer loop), 15 (decrement), 16 (lowercase return)
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(1000) == "m"


def test_subtractive_pairs():
    # Exercises the outer loop skipping indices (i -= 1 repeatedly, line 15)
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"


def test_repeated_symbols_exercise_inner_loop():
    # Exercises lines 12-14 (inner while loop running multiple times)
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(30) == "xxx"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(3000) == "mmm"


def test_mixed_number_multiple_outer_iterations():
    # Exercises many iterations of the outer while loop (line 9) and inner loop (line 12)
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(3999) == "mmmcmxcix"


def test_result_is_lowercase():
    # Verifies the postcondition of line 16 (res.lower())
    result = int_to_mini_roman(2024)
    assert result == "mmxxiv"
    assert result == result.lower()
    assert not any(ch.isupper() for ch in result)
