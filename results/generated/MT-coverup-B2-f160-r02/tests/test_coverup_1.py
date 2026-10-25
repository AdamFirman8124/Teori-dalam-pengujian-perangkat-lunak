# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_combines_operators_and_operands():
    assert do_algebra(["+", "*"], [2, 3, 4]) == 14


def test_do_algebra_with_no_operators_returns_operand():
    assert do_algebra([], [7]) == 7
