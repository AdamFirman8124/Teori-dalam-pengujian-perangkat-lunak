# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

from f160 import do_algebra


def test_do_algebra_with_multiple_operators():
    assert do_algebra(["+", "*"], [2, 3, 4]) == 14


def test_do_algebra_without_operators():
    assert do_algebra([], [7]) == 7
