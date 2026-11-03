# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


def test_fib_base_case_zero():
    """Covers lines 3-4: the n == 0 branch."""
    assert fib(0) == 0


def test_fib_base_case_one():
    """Covers lines 5-6: the n == 1 branch."""
    assert fib(1) == 1


def test_fib_recursive_case():
    """Covers line 7: the recursive branch."""
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(10) == 55


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
    ],
)
def test_fib_known_values(n, expected):
    """Exercises all branches (base cases and recursion) with known Fibonacci values."""
    assert fib(n) == expected
