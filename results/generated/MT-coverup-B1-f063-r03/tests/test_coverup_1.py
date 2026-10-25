# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


def test_fibfib_base_cases():
    assert fibfib(0) == 0
    assert fibfib(1) == 0
    assert fibfib(2) == 1


def test_fibfib_recursive_branch():
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(6) == 7


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 0),
        (1, 0),
        (2, 1),
        (3, 1),
        (4, 2),
        (5, 4),
        (6, 7),
        (7, 13),
        (8, 24),
    ],
)
def test_fibfib_sequence(n, expected):
    assert fibfib(n) == expected


def test_fibfib_is_pure_and_repeatable():
    first = fibfib(7)
    second = fibfib(7)
    assert first == second == 13
    assert fibfib(0) == 0
