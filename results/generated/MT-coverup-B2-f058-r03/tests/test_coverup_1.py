# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_common_elements():
    """Covers lines 3-8 including the true branch of the equality check."""
    result = common([1, 2, 3, 4], [3, 4, 5, 6])
    assert result == [3, 4]
    assert isinstance(result, list)


def test_common_no_common_elements():
    """Covers the false branch of the equality check (line 6)."""
    result = common([1, 2, 3], [7, 8, 9])
    assert result == []


def test_common_empty_first_list():
    """Covers the branch where the outer loop (line 4) is never entered."""
    result = common([], [1, 2, 3])
    assert result == []


def test_common_empty_second_list():
    """Covers the branch where the inner loop (line 5) is never entered."""
    result = common([1, 2, 3], [])
    assert result == []


def test_common_duplicates_and_unsorted_input():
    """Verifies deduplication via the set and sorted output ordering."""
    result = common([5, 1, 5, 3, 1], [1, 5, 5, 2])
    assert result == [1, 5]


def test_common_both_empty():
    result = common([], [])
    assert result == []
