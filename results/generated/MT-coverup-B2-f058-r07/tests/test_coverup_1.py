# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_intersection():
    """Covers lines 3-8, including the True branch of the equality check."""
    result = common([1, 2, 3, 4], [3, 4, 5])
    assert result == [3, 4]


def test_common_no_intersection():
    """Covers the False branch of the equality check (line 6 -> no add)."""
    result = common([1, 2], [3, 4])
    assert result == []


def test_common_empty_lists():
    """Covers loops that never execute (empty l1 and l2)."""
    assert common([], []) == []
    assert common([], [1, 2]) == []
    assert common([1, 2], []) == []


def test_common_duplicates_and_unsorted():
    """Duplicates collapse via the set; result is sorted."""
    result = common([5, 1, 5, 3], [3, 5, 5, 9])
    assert result == [3, 5]
