# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


def test_special_factorial_zero():
    assert special_factorial(0) == 1


def test_special_factorial_one():
    assert special_factorial(1) == 1


def test_special_factorial_small_values():
    assert special_factorial(2) == 2
    assert special_factorial(3) == 12
    assert special_factorial(4) == 288
    assert special_factorial(5) == 34560


def test_special_factorial_matches_product_of_factorials():
    def fact(k):
        result = 1
        for j in range(1, k + 1):
            result *= j
        return result

    for n in range(0, 8):
        expected = 1
        for k in range(1, n + 1):
            expected *= fact(k)
        assert special_factorial(n) == expected


def test_special_factorial_is_monotonic_and_positive():
    values = [special_factorial(n) for n in range(0, 6)]
    assert values[0] == 1
    assert all(v > 0 for v in values)
    assert all(values[i] < values[i + 1] for i in range(1, len(values) - 1))


def test_special_factorial_rejects_negative_loop_body():
    # range(1, n+1) is empty for negative n, so the loop body is skipped.
    assert special_factorial(-5) == 1
