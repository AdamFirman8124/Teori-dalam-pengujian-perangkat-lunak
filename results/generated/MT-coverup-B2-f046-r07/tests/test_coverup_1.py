# file: project/f046/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 11], "branches": [[4, 5], [4, 7], [7, 8], [7, 11]]}

import pytest

from f046 import fib4


@pytest.mark.parametrize(
    "n, expected",
    [
        # Base cases: exercise lines 3-5 (initial list + `n < 4` early return).
        (0, 0),
        (1, 0),
        (2, 2),
        (3, 0),
        # Loop cases: exercise lines 7-9 (loop body) and line 11 (final return).
        (4, 2),
        (5, 4),
        (6, 8),
        (7, 14),
        (8, 28),
        (9, 54),
        (10, 104),
    ],
)
def test_fib4_known_values(n, expected):
    """fib4 must return the expected element of the tetranacci-like sequence
    starting with [0, 0, 2, 0]."""
    assert fib4(n) == expected


def test_fib4_satisfies_recurrence():
    """For n >= 4 each value must be the sum of the four preceding values,
    which validates the append/pop(0) sliding-window logic on lines 7-9."""
    values = [fib4(i) for i in range(12)]
    assert values[:4] == [0, 0, 2, 0]
    for n in range(4, 12):
        assert values[n] == sum(values[n - 4:n])


def test_fib4_is_pure():
    """fib4 must not mutate any shared state: repeated calls with the same
    argument return the same result (no cleanup/monkeypatching needed since
    the function is pure)."""
    assert fib4(6) == 8
    assert fib4(6) == 8
    assert fib4(2) == 2
