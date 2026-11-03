# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest

from f022 import filter_integers


def test_filter_integers_mixed_types_executes_line_6():
    """Mixed input exercises both branches of the isinstance filter on line 6."""
    values = [1, "hello", 2.5, 3, None, [4], (5,), {"6": 6}]
    result = filter_integers(values)
    # Only the ints survive; order preserved.
    assert result == [1, 3]
    # Original list must not be mutated (pure function).
    assert values == [1, "hello", 2.5, 3, None, [4], (5,), {"6": 6}]


def test_filter_integers_all_integers():
    """All-integer input takes the True branch for every element."""
    assert filter_integers([10, -20, 0, 999]) == [10, -20, 0, 999]


def test_filter_integers_no_integers():
    """No-integer input takes the False branch for every element."""
    assert filter_integers(["a", 1.5, None, [], ()]) == []


def test_filter_integers_empty_list():
    """Empty input still executes line 6 and returns an empty list."""
    result = filter_integers([])
    assert result == []
    assert result is not None


def test_filter_integers_bool_is_instance_of_int():
    """bool subclasses int, so True/False pass the isinstance check."""
    assert filter_integers([True, False, 7]) == [True, False, 7]


def test_filter_integers_returns_new_list():
    """Result must be a distinct list object, not the input."""
    values = [1, 2]
    result = filter_integers(values)
    assert result == values
    assert result is not values
