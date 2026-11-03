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
        (3, 1),   # covers line 9 (recursive branch): 1 + 0 + 0
        (4, 2),   # recursive: 1 + 1 + 0
        (5, 4),   # recursive: 2 + 1 + 1
        (6, 7),   # recursive: 4 + 2 + 1
        (7, 13),  # recursive: 7 + 4 + 2
        (8, 24),  # recursive: 13 + 7 + 4
    ],
)
def test_fibfib(n, expected):
    """fibfib must return 0 for n in {0, 1}, 1 for n == 2, and the
    tribonacci-style sum fibfib(n-1) + fibfib(n-2) + fibfib(n-3) otherwise."""
    assert fibfib(n) == expected
