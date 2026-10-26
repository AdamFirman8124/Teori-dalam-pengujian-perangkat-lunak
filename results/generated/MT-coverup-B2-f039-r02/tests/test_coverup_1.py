# file: project/f039/__init__.py:1-18
# asked: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}
# gained: {"lines": [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[6, 7], [6, 8], [8, 9], [8, 11], [9, 8], [9, 10], [13, 14], [15, 16], [15, 17], [17, 13], [17, 18]]}

import pytest

from f039 import prime_fib


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),      # first Fibonacci prime; exercises is_prime(1) -> p < 2 branch
        (2, 3),      # exercises empty-range prime path
        (3, 5),      # exercises loop body with non-divisor
        (4, 13),     # exercises composite rejection (8, 21, 34, 55) and prime accept
        (5, 89),
        (6, 233),
        (7, 1597),
    ],
)
def test_prime_fib_returns_nth_fibonacci_prime(n, expected):
    result = prime_fib(n)
    assert result == expected
    assert isinstance(result, int)


def test_prime_fib_handles_composites_before_answer():
    # 8, 21, 34, 55, 144, 377, 610, 987 are Fibonacci numbers that are not prime;
    # reaching 13 and 1597 requires is_prime to return False for them.
    assert prime_fib(4) == 13
    assert prime_fib(7) == 1597


def test_prime_fib_is_pure_and_repeatable():
    first = prime_fib(5)
    second = prime_fib(5)
    assert first == second == 89
    # Calling with a smaller n afterwards must not be affected by prior calls.
    assert prime_fib(1) == 2
