# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_mixed_operators_multiple_iterations():
    """Covers lines 3-6, with the loop body (line 5) executing several times.

    Builds the expression '2+3*4-5' which evaluates to 9 (multiplication
    binds tighter than addition/subtraction).
    """
    result = do_algebra(['+', '*', '-'], [2, 3, 4, 5])
    assert result == 9


def test_do_algebra_single_operand_no_operators():
    """Covers lines 3 and 6 with an empty operator list (loop body skipped)."""
    result = do_algebra([], [42])
    assert result == 42


def test_do_algebra_floor_division():
    """Covers line 5 with the '//' operator: 7 // 2 == 3."""
    result = do_algebra(['//'], [7, 2])
    assert result == 3


def test_do_algebra_modulo():
    """Covers line 5 with the '%' operator: 10 % 3 == 1."""
    result = do_algebra(['%'], [10, 3])
    assert result == 1


def test_do_algebra_exponentiation():
    """Covers line 5 with the '**' operator: 2 ** 3 == 8."""
    result = do_algebra(['**'], [2, 3])
    assert result == 8


def test_do_algebra_negative_first_operand():
    """Covers line 3 stringifying a negative operand: '-3+5' == 2."""
    result = do_algebra(['+'], [-3, 5])
    assert result == 2


def test_do_algebra_long_chain_left_to_right():
    """Covers many loop iterations with same-precedence operators.

    '100-20+3-1' evaluates left to right: 100-20=80, 80+3=83, 83-1=82.
    """
    result = do_algebra(['-', '+', '-'], [100, 20, 3, 1])
    assert result == 82
