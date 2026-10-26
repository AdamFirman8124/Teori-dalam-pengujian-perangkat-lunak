# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


def test_fib_base_case_zero():
    """Covers lines 3-4: n == 0 returns 0."""
    assert fib(0) == 0


def test_fib_base_case_one():
    """Covers lines 5-6: n == 1 returns 1."""
    assert fib(1) == 1


def test_fib_recursive_case():
    """Covers line 7: recursive branch, and exercises all lines together."""
    assert fib(5) == 5
    assert fib(10) == 55


@pytest.mark.parametrize("n,expected", [(0, 0), (1, 1), (2, 1), (3, 2), (7, 13)])
def test_fib_known_values(n, expected):
    assert fib(n) == expected
