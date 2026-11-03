# file: project/f076/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f076 import is_simple_power


@pytest.mark.parametrize(
    ("x", "n", "expected"),
    [
        # n == 1 branch (lines 3-4): both True and False outcomes
        (1, 1, True),   # n == 1 and x == 1
        (2, 1, False),  # n == 1 but x != 1
        (5, 1, False),
        # while-loop branch (lines 5-8): loop body executed, returns True
        (8, 2, True),   # 1 -> 2 -> 4 -> 8
        (27, 3, True),  # 1 -> 3 -> 9 -> 27
        (25, 5, True),
        # while-loop branch (lines 5-8): loop body executed, returns False
        (3, 2, False),  # power overshoots: 1 -> 2 -> 4
        (10, 3, False), # power overshoots: 1 -> 3 -> 9 -> 27
        # while-loop branch: loop body never entered (x <= 1)
        (1, 2, True),   # power starts at 1, loop condition 1 < 1 is False
        (1, 7, True),
    ],
)
def test_is_simple_power(x, n, expected):
    result = is_simple_power(x, n)
    assert result is expected, (
        f"is_simple_power({x}, {n}) returned {result!r}, expected {expected!r}"
    )
