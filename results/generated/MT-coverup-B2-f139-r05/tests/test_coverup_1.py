# file: project/f139/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8]]}

import pytest

from f139 import special_factorial


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),        # single loop iteration: 1! = 1
        (2, 2),        # 1! * 2! = 1 * 2 = 2
        (3, 12),       # 1! * 2! * 3! = 1 * 2 * 6 = 12
        (4, 288),      # 1! * 2! * 3! * 4! = 1 * 2 * 6 * 24 = 288
        (5, 34560),    # 288 * 5! = 288 * 120 = 34560
    ],
)
def test_special_factorial_executes_loop(n, expected):
    """Exercise lines 3-8 (accumulator init, loop body, return)."""
    result = special_factorial(n)
    assert result == expected
    # Postcondition: result equals the product of factorials 1! * 2! * ... * n!
    product = 1
    running_fact = 1
    for i in range(1, n + 1):
        running_fact *= i
        product *= running_fact
    assert result == product


def test_special_factorial_zero_skips_loop_body():
    """n=0 covers lines 3-5 and 8 while skipping the loop body (empty range)."""
    assert special_factorial(0) == 1
