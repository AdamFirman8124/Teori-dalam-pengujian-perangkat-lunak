# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_matches():
    """Covers lines 3-8: set creation, both loops, matching branch, add, and return."""
    result = common([1, 2, 3], [2, 3, 4])
    assert result == [2, 3]
    assert result == sorted(result)


def test_common_without_matches():
    """Covers the False branch of the equality check (line 6)."""
    assert common([1, 2], [3, 4]) == []


def test_common_empty_first_list():
    """Covers line 4 loop body never executing when l1 is empty."""
    assert common([], [1, 2, 3]) == []


def test_common_empty_second_list():
    """Covers line 5 loop body never executing when l2 is empty."""
    assert common([1, 2, 3], []) == []


def test_common_both_empty():
    """Edge case: both lists empty."""
    assert common([], []) == []


def test_common_duplicates_and_unsorted():
    """Verifies deduplication via the set and sorted output ordering."""
    result = common([5, 3, 1, 3], [3, 5, 5])
    assert result == [3, 5]
    assert len(result) == len(set(result))


def test_common_result_is_new_list():
    """Postcondition: returned list is independent of the inputs."""
    l1 = [1, 2]
    l2 = [2, 3]
    result = common(l1, l2)
    result.append(99)
    assert l1 == [1, 2]
    assert l2 == [2, 3]
