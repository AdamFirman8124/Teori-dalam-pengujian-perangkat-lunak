# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


def test_fib_base_case_zero():
    """Covers lines 3-4: the n == 0 branch taken, n == 1 branch not taken."""
    assert fib(0) == 0


def test_fib_base_case_one():
    """Covers lines 5-6: the n == 1 branch taken (n == 0 branch not taken)."""
    assert fib(1) == 1


def test_fib_recursive_case():
    """Covers line 7: the recursive branch, exercising both recursive calls."""
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(10) == 55


def test_fib_first_values_match_sequence():
    """Sanity check of the full Fibonacci sequence across all branches."""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert [fib(n) for n in range(len(expected))] == expected
