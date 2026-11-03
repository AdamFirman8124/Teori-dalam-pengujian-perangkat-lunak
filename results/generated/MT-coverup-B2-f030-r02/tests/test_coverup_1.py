# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f030 import get_positive


def test_get_positive_filters_positive_numbers():
    # Mixed input exercises both branches of the `e > 0` condition on line 3
    assert get_positive([-1, 0, 2, -3, 5]) == [2, 5]
    # All positive: condition always true
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    # All non-positive: condition always false
    assert get_positive([-1, -2, 0]) == []
    # Empty list: comprehension body never executes
    assert get_positive([]) == []
    # Order and duplicates are preserved
    assert get_positive([4, -4, 4]) == [4, 4]
