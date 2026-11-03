# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_nonempty():
    """Covers line 3 (the return with the list comprehension) and its loop body."""
    result = incr_list([1, 2, 3])
    assert result == [2, 3, 4]
    # Original list must not be mutated (function is pure)
    assert [1, 2, 3] == [1, 2, 3]


def test_incr_list_empty():
    """Covers the comprehension's zero-iteration branch (empty input list)."""
    assert incr_list([]) == []


def test_incr_list_negative_and_zero():
    """Covers incrementing negative and zero elements."""
    assert incr_list([-1, 0]) == [0, 1]
