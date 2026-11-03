# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),   # covers lines 3-4 (n == 0 branch)
        (1, 0),   # covers lines 5-6 (n == 1 branch)
        (2, 1),   # covers lines 7-8 (n == 2 branch)
        (3, 1),   # covers line 9 (recursive branch)
        (4, 2),
        (5, 4),
        (6, 7),
        (7, 13),
        (8, 24),
    ],
)
def test_fibfib_known_values(n, expected):
    """fibfib must return the correct value for base cases and recursive cases."""
    assert fibfib(n) == expected


def test_fibfib_satisfies_recurrence():
    """For n >= 3, fibfib(n) must equal fibfib(n-1) + fibfib(n-2) + fibfib(n-3)."""
    values = [fibfib(i) for i in range(12)]
    assert values[0] == 0
    assert values[1] == 0
    assert values[2] == 1
    for n in range(3, 12):
        assert values[n] == values[n - 1] + values[n - 2] + values[n - 3]
