# file: project/f063/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[3, 4], [3, 5], [5, 6], [5, 7], [7, 8], [7, 9]]}

import pytest

from f063 import fibfib


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),   # covers lines 3-4: base case n == 0
        (1, 0),   # covers lines 5-6: base case n == 1
        (2, 1),   # covers lines 7-8: base case n == 2
        (3, 1),   # covers line 9: recursion fibfib(2) + fibfib(1) + fibfib(0) = 1 + 0 + 0
        (5, 4),   # covers line 9 with deeper recursion: fibfib(4) + fibfib(3) + fibfib(2) = 2 + 1 + 1
    ],
)
def test_fibfib(n, expected):
    assert fibfib(n) == expected
