# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

"""Tests for f139.special_factorial.

This module covers all previously untested lines (3-8), including the
loop body (lines 6-7) and both outcomes of the loop condition (line 5).
"""

import pytest

from f139 import special_factorial


def test_special_factorial_executes_loop_body():
    """Covers lines 3-8: initialization, loop body, and return.

    For n=4 the Brazilian factorial is 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288.
    """
    result = special_factorial(4)

    assert result == 288


def test_special_factorial_single_iteration():
    """Covers a single loop iteration: n=1 gives 1! = 1."""
    result = special_factorial(1)

    assert result == 1


def test_special_factorial_two_iterations():
    """Verifies the running product: n=2 gives 1! * 2! = 2."""
    result = special_factorial(2)

    assert result == 2


def test_special_factorial_three_iterations():
    """Verifies the running product: n=3 gives 1! * 2! * 3! = 12."""
    result = special_factorial(3)

    assert result == 12


def test_special_factorial_zero_skips_loop_body():
    """Covers the loop not executing (branch of line 5): n=0 returns 1."""
    result = special_factorial(0)

    assert result == 1
