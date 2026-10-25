# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_single_operand_no_loop():
    assert do_algebra([], [5]) == 5


def test_do_algebra_two_operands_single_operator():
    assert do_algebra(['+'], [2, 3]) == 5


def test_do_algebra_multiple_operators_loop():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10
    assert do_algebra(['//'], [7, 2]) == 3
    assert do_algebra(['**'], [2, 3]) == 8
