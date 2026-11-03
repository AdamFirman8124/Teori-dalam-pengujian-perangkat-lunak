# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import math

import pytest

from f139 import special_factorial


def test_special_factorial_zero_skips_loop():
    """n = 0: the loop body (lines 6-7) never executes; result stays 1."""
    assert special_factorial(0) == 1


def test_special_factorial_one_single_iteration():
    """n = 1: loop runs exactly once; 1! == 1."""
    assert special_factorial(1) == 1


def test_special_factorial_multiple_iterations():
    """n = 4: loop runs several times; 1! * 2! * 3! * 4! == 288."""
    assert special_factorial(4) == 288


def test_special_factorial_matches_product_of_factorials():
    """For a larger n, verify against an independent computation."""
    n = 6
    expected = 1
    for i in range(1, n + 1):
        expected *= math.factorial(i)
    assert special_factorial(n) == expected


def test_special_factorial_is_pure_no_state_pollution(monkeypatch):
    """Calling repeatedly with the same argument yields identical results,
    confirming the function mutates no shared state."""
    monkeypatch.setattr(math, "factorial", math.factorial)  # no-op guard; nothing patched
    first = special_factorial(5)
    second = special_factorial(5)
    assert first == second == 34560  # 1! * 2! * 3! * 4! * 5! = 34560
