# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra


def test_multiple_operators_covers_loop_body():
    """Lines 3-6 with the for-loop body executing several times."""
    # expression = "2+3*4-5" -> 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9


def test_integer_division_and_multiplication():
    # expression = "7//3*4" -> (7 // 3) * 4 = 8
    assert do_algebra(['//', '*'], [7, 3, 4]) == 8


def test_exponentiation():
    # expression = "2**3" -> 8
    assert do_algebra(['**'], [2, 3]) == 8


def test_single_operand_loop_body_skipped():
    """Covers the branch where the for-loop body (line 5) never runs."""
    assert do_algebra([], [42]) == 42


def test_negative_operand_stringification():
    # str(-2) yields "-2", so expression is "3+-2-1" -> 0
    assert do_algebra(['+', '-'], [3, -2, 1]) == 0


def test_float_operand_stringification():
    # str(2.5) yields "2.5", so expression is "2.5*2" -> 5.0
    assert do_algebra(['*'], [2.5, 2]) == 5.0
