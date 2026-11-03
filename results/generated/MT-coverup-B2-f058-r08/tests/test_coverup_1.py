# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_all_lines_and_branches():
    """Exercises lines 3-8: set creation, both loops, both branches of the
    equality check, set addition, and the sorted return."""
    # Both lists non-empty, with elements that match and don't match,
    # plus duplicates to exercise the set-based deduplication.
    result = common([3, 1, 2, 1], [2, 1, 4, 3])
    assert result == [1, 2, 3]


def test_common_no_matches_false_branch():
    """Covers the False branch of the equality check with no matches at all."""
    assert common([1, 2, 3], [4, 5, 6]) == []


def test_common_empty_lists():
    """Covers the case where the outer loop never executes."""
    assert common([], [1, 2]) == []
    assert common([1, 2], []) == []
    assert common([], []) == []


def test_common_with_duplicates_and_strings():
    """Covers the True branch with mixed duplicates and non-numeric types."""
    assert common(["b", "a", "b", "c"], ["c", "b", "b"]) == ["b", "c"]
