# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_with_multiple_operations():
    operators = ["+", "*"]
    operands = [1, 2, 3]

    assert do_algebra(operators, operands) == 7
    assert operators == ["+", "*"]
    assert operands == [1, 2, 3]


def test_do_algebra_with_no_operations():
    operators = []
    operands = [42]

    assert do_algebra(operators, operands) == 42
    assert operators == []
    assert operands == [42]
