# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_common_elements():
    """Covers lines 3-8: set creation, nested loops, equality branch, add, and return."""
    result = common([1, 2, 3, 4], [3, 4, 5, 6])
    assert result == [3, 4]


def test_common_no_common_elements():
    """Covers the False branch of the equality check (line 6)."""
    result = common([1, 2], [3, 4])
    assert result == []


def test_common_empty_lists():
    """Covers loops that never execute (lines 4-5 with empty inputs)."""
    assert common([], [1, 2]) == []
    assert common([1, 2], []) == []
    assert common([], []) == []


def test_common_with_duplicates():
    """Verifies the set deduplicates repeated matches (line 7)."""
    result = common([1, 1, 2, 2, 3], [2, 3, 3, 4])
    assert result == [2, 3]


def test_common_result_is_sorted():
    """Verifies the sorted() call on line 8 orders the output."""
    result = common([5, 1, 3], [3, 5, 1])
    assert result == [1, 3, 5]
    assert result == sorted(result)


def test_common_does_not_mutate_inputs():
    """Ensures the function is side-effect free (no state pollution)."""
    l1 = [3, 1, 2]
    l2 = [2, 4, 3]
    l1_copy = list(l1)
    l2_copy = list(l2)
    result = common(l1, l2)
    assert l1 == l1_copy
    assert l2 == l2_copy
    assert result == [2, 3]
