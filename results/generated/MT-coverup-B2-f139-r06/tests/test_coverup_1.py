# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_zero_skips_loop():
    # n=0 -> range(1, 1) is empty, loop body never runs
    assert special_factorial(0) == 1


def test_special_factorial_one():
    assert special_factorial(1) == 1


def test_special_factorial_positive_runs_loop():
    # 1! = 1, 2! = 2, 3! = 6, 4! = 24 -> 1*2*6*24 = 288
    assert special_factorial(4) == 288


def test_special_factorial_five():
    # 288 * 120 = 34560
    assert special_factorial(5) == 34560


def test_special_factorial_matches_reference_implementation():
    def reference(n):
        fact_i = 1
        special_fact = 1
        for i in range(1, n + 1):
            fact_i *= i
            special_fact *= fact_i
        return special_fact

    for n in range(0, 8):
        assert special_factorial(n) == reference(n)


def test_special_factorial_is_pure_and_repeatable():
    first = special_factorial(6)
    second = special_factorial(6)
    assert first == second == 24883200
