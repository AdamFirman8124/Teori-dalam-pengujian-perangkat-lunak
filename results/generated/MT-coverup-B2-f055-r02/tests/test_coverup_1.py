# file: project/f055/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[3, 4], [3, 5], [5, 6], [5, 7]]}

import pytest

from f055 import fib


def test_fib_base_case_zero():
    """Covers lines 3-4: the n == 0 base case."""
    result = fib(0)
    assert result == 0


def test_fib_base_case_one():
    """Covers lines 5-6: the n == 1 base case."""
    result = fib(1)
    assert result == 1


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
    ],
)
def test_fib_recursive_cases(n, expected):
    """Covers line 7: the recursive case, including calls back into
    the base cases, and verifies the Fibonacci postcondition."""
    assert fib(n) == expected
    # Postcondition: result matches the closed-form definition
    # fib(n) = fib(n-1) + fib(n-2) for n >= 2, verified indirectly
    # by the expected values derived from the recurrence.
