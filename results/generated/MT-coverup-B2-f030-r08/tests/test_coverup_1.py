# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f030 import get_positive


def test_get_positive_filters_and_keeps_only_positive_values():
    """Line 3 executes; both branches of `e > 0` are exercised."""
    result = get_positive([-1, 0, 2, -3, 5])
    # Positive elements kept (true branch), zero/negative filtered out (false branch)
    assert result == [2, 5]
    # Also verify with an all-positive list
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    # And an empty list (loop body never runs, but line 3 still executes)
    assert get_positive([]) == []
