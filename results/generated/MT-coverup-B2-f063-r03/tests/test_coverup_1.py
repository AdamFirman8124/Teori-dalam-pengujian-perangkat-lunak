# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


def test_fibfib_base_case_zero():
    """Covers lines 3-4: n == 0 returns 0."""
    assert fibfib(0) == 0


def test_fibfib_base_case_one():
    """Covers lines 5-6: n == 1 returns 0."""
    assert fibfib(1) == 0


def test_fibfib_base_case_two():
    """Covers lines 7-8: n == 2 returns 1."""
    assert fibfib(2) == 1


def test_fibfib_recursive_case():
    """Covers line 9: recursive branch for n >= 3.

    fibfib(3) = fibfib(2) + fibfib(1) + fibfib(0) = 1 + 0 + 0 = 1
    fibfib(4) = fibfib(3) + fibfib(2) + fibfib(1) = 1 + 1 + 0 = 2
    fibfib(5) = fibfib(4) + fibfib(3) + fibfib(2) = 2 + 1 + 1 = 4
    fibfib(8) = 24
    """
    assert fibfib(3) == 1
    assert fibfib(4) == 2
    assert fibfib(5) == 4
    assert fibfib(8) == 24


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
def test_fibfib_known_values(n, expected):
    """Full-branch coverage: every base case and the recursive case."""
    assert fibfib(n) == expected
