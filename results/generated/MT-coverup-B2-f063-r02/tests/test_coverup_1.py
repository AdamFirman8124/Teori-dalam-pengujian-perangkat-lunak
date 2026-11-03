# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        # Base cases: exercise lines 3-4 (n == 0), 5-6 (n == 1), 7-8 (n == 2).
        (0, 0),
        (1, 0),
        (2, 1),
        # Recursive case: exercises line 9 (and the False branches of all three ifs).
        (3, 1),
        (4, 2),
        (5, 4),
        (6, 7),
        (7, 13),
        (8, 24),
    ],
)
def test_fibfib(n, expected):
    """fibfib must match the tribonacci-style recurrence for every branch."""
    assert fibfib(n) == expected


def test_fibfib_recurrence_holds():
    """Verify the recurrence fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)."""
    results = [fibfib(n) for n in range(10)]
    for n in range(3, 10):
        assert results[n] == results[n - 1] + results[n - 2] + results[n - 3]
    # Postconditions for the base cases, ensuring lines 4, 6 and 8 ran correctly.
    assert results[0] == 0
    assert results[1] == 0
    assert results[2] == 1
