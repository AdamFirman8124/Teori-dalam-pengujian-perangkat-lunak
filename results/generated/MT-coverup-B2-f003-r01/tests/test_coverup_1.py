# file: project/f003/__init__.py:4-13
# asked: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}
# gained: {"lines": [6, 8, 9, 10, 11, 13], "branches": [[8, 9], [8, 13], [10, 8], [10, 11]]}

import pytest

from f003 import below_zero


@pytest.mark.parametrize(
    "operations, expected",
    [
        # Empty list: loop body never executes, falls through to `return False`
        ([], False),
        # All positive operations: balance never drops below zero
        ([1, 2, 3], False),
        # Mixed but never negative: balance hits zero exactly, never below
        ([1, -1, 5, -5, 10], False),
        # Single negative operation triggers early `return True`
        ([-1], True),
        # Balance dips below zero after some positive operations
        ([10, 5, -20], True),
        # Balance briefly goes negative then recovers; early return on dip
        ([5, -6, 10], True),
    ],
)
def test_below_zero(operations, expected):
    result = below_zero(operations)
    assert isinstance(result, bool)
    assert result is expected
