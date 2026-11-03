# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_common_elements():
    """Covers lines 3-8: set creation, both loops, matching branch (ret.add), and return."""
    result = common([1, 2, 3, 4], [3, 4, 5, 6])
    assert result == [3, 4]
    assert isinstance(result, list)
    assert result == sorted(result)


def test_common_no_common_elements():
    """Covers lines 3-6 and 8 with the False branch of the equality check."""
    result = common([1, 2, 3], [4, 5, 6])
    assert result == []


def test_common_empty_first_list():
    """Covers lines 3 and 8; the inner loop (line 5) never runs."""
    assert common([], [1, 2, 3]) == []


def test_common_empty_second_list():
    """Covers lines 3, 4 and 8; the inner loop (line 5) never runs."""
    assert common([1, 2, 3], []) == []


def test_common_both_empty():
    """Covers lines 3 and 8 only; neither loop body executes."""
    assert common([], []) == []


def test_common_duplicates_deduplicated():
    """Duplicates in inputs must not produce duplicates in the result (set semantics, line 7)."""
    result = common([1, 1, 2, 2, 3], [2, 2, 3, 3, 1])
    assert result == [1, 2, 3]


def test_common_result_is_sorted():
    """Line 8: result must be sorted regardless of input order."""
    result = common([9, 5, 1, 7], [7, 1, 9, 5])
    assert result == [1, 5, 7, 9]


def test_common_strings():
    """Works for non-numeric comparable elements too."""
    result = common(["b", "a", "c"], ["c", "a", "d"])
    assert result == ["a", "c"]


def test_common_does_not_mutate_inputs():
    """The function must be side-effect free on its arguments."""
    l1 = [3, 1, 2]
    l2 = [2, 3, 4]
    l1_copy = list(l1)
    l2_copy = list(l2)
    result = common(l1, l2)
    assert result == [2, 3]
    assert l1 == l1_copy
    assert l2 == l2_copy
