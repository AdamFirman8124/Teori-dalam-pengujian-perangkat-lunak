# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f042 import incr_list


def test_incr_list_nonempty_executes_line_3():
    """Calling with a non-empty list executes line 3 (the comprehension)."""
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]


def test_incr_list_empty_covers_zero_iteration_branch():
    """Calling with an empty list covers the branch where the loop body never runs."""
    result = incr_list([])
    assert result == []


def test_incr_list_does_not_mutate_input():
    """The function must not modify its argument (postcondition check)."""
    original = [0, -1, 100]
    snapshot = list(original)
    result = incr_list(original)
    assert original == snapshot
    assert result == [1, 0, 101]


def test_incr_list_result_is_new_list():
    """The result must be a distinct list object, not the input aliased."""
    data = [5]
    result = incr_list(data)
    assert result is not data
    assert result == [6]
