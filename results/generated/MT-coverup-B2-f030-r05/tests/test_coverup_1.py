# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f030 import get_positive


def test_get_positive_filters_negatives_and_zero():
    """Covers the comprehension line, both the true branch (e > 0)
    and the false branch (e <= 0) of the filter condition."""
    result = get_positive([1, -2, 3, 0, -5, 7])
    assert result == [1, 3, 7]
    # Postcondition: every returned element is strictly positive
    assert all(e > 0 for e in result)


def test_get_positive_all_negative():
    """Covers the false branch of the condition for every element."""
    result = get_positive([-1, -2, -3])
    assert result == []


def test_get_positive_empty_list():
    """Covers the branch where the loop body never executes."""
    result = get_positive([])
    assert result == []


def test_get_positive_all_positive():
    """Covers the true branch of the condition for every element."""
    result = get_positive([1, 2, 3])
    assert result == [1, 2, 3]
