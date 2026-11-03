# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),   # covers lines 3-4 (n == 0 branch)
        (1, 0),   # covers lines 5-6 (n == 1 branch)
        (2, 1),   # covers lines 7-8 (n == 2 branch)
    ],
)
def test_fibfib_base_cases(n, expected):
    assert fibfib(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (3, 1),    # first recursive call: fibfib(2)+fibfib(1)+fibfib(0) = 1+0+0
        (4, 2),    # 1+1+0
        (5, 4),    # 2+1+1
        (6, 7),    # 4+2+1
        (7, 13),   # 7+4+2
        (8, 24),   # 13+7+4
    ],
)
def test_fibfib_recursive_cases(n, expected):
    # covers line 9 (recursive return) and all three recursive sub-calls
    assert fibfib(n) == expected


def test_fibfib_recurrence_relation():
    # verifies the defining recurrence for a range of values
    values = [fibfib(i) for i in range(3, 10)]
    for i in range(3, 10):
        assert fibfib(i) == fibfib(i - 1) + fibfib(i - 2) + fibfib(i - 3)
    assert values == [1, 2, 4, 7, 13, 24, 44]
