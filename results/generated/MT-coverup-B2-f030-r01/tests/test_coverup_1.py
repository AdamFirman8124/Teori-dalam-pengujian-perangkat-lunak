# file: project/f030/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f030 import get_positive


def test_get_positive_filters_positive_values():
    """Covers line 3 and both branches of the comprehension condition:
    elements kept (e > 0 is True) and elements filtered out (e > 0 is False)."""
    result = get_positive([-1, 0, 2, 3.5, -7])
    assert result == [2, 3.5]


def test_get_positive_empty_list():
    """Covers line 3 with an empty input list (loop body never runs)."""
    assert get_positive([]) == []


def test_get_positive_all_non_positive():
    """Covers line 3 where every element fails the condition."""
    assert get_positive([-5, 0, -0.1]) == []
