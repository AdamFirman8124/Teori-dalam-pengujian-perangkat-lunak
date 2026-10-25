# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra


def test_do_algebra_single_operand():
    # Covers line 3 (initial expression) and line 6 (return) with no loop iterations.
    assert do_algebra([], [7]) == 7


def test_do_algebra_multiple_operators():
    # Covers lines 3-6: builds the expression string and evaluates it.
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 2 + 3 * 4 - 5
    assert do_algebra(['//', '+'], [9, 2, 3]) == 9 // 2 + 3
    assert do_algebra(['**'], [2, 3]) == 2 ** 3
