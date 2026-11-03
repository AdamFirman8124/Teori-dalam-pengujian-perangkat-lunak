# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra


def test_single_operator_covers_all_lines():
    """Lines 3-6: builds '2+3' and evaluates it; loop body runs once."""
    assert do_algebra(['+'], [2, 3]) == 5


def test_multiple_operators_loop_runs_multiple_times():
    """Line 5 executes repeatedly; Python precedence applies: 2+3*4-5 == 9."""
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9


def test_empty_operator_list_loop_not_taken():
    """Covers the branch where the for-loop body never executes."""
    assert do_algebra([], [42]) == 42


def test_floor_division_and_power():
    """'7//2**3' evaluates to 7 // 8 == 0."""
    assert do_algebra(['//', '**'], [7, 2, 3]) == 0


def test_multiplication_and_modulo():
    """'10*3%4' evaluates to 30 % 4 == 2."""
    assert do_algebra(['*', '%'], [10, 3, 4]) == 2


def test_negative_operand():
    """'2+-3' is valid Python and evaluates to -1."""
    assert do_algebra(['+'], [2, -3]) == -1


def test_subtraction_chain():
    """'100-30-20' evaluates left-to-right to 50."""
    assert do_algebra(['-', '-'], [100, 30, 20]) == 50


def test_inputs_are_not_mutated():
    """The function must not modify its arguments (no state pollution)."""
    operators = ['+', '*']
    operands = [2, 3, 4]
    result = do_algebra(operators, operands)
    assert result == 2 + 3 * 4
    assert operators == ['+', '*']
    assert operands == [2, 3, 4]
