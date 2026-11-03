# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_multiple_operators():
    """Covers lines 3-6: builds a multi-operator expression string and evals it."""
    # expression = "2+3*4-5" -> 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9


def test_do_algebra_single_operator():
    """Covers the loop body (line 5) with exactly one operator/operand pair."""
    assert do_algebra(['+'], [1, 2]) == 3


def test_do_algebra_floor_division_and_power():
    """Exercises other supported operators through the same code path."""
    # "7//3*4" -> 2 * 4 = 8
    assert do_algebra(['//', '*'], [7, 3, 4]) == 8
    # "2**3" -> 8
    assert do_algebra(['**'], [2, 3]) == 8


def test_do_algebra_no_operators_returns_first_operand():
    """With no operators, zip yields nothing; the first operand is returned."""
    assert do_algebra([], [42]) == 42
