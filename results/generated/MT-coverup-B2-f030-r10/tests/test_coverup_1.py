# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f030 import get_positive


def test_get_positive_filters_non_positive_elements():
    """Execute line 3 with both branches of the `e > 0` condition taken:
    positive elements are kept, zero and negative elements are filtered out."""
    result = get_positive([1, -2, 3, 0, 4])
    assert result == [1, 3, 4]


def test_get_positive_all_negative():
    """Cover the branch where the comprehension condition is False for every element."""
    assert get_positive([-1, -5, 0]) == []


def test_get_positive_empty_list():
    """Cover the branch where the comprehension loop body never executes."""
    assert get_positive([]) == []
