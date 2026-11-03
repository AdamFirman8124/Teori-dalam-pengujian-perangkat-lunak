# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_mixed_types():
    """Line 6: list comprehension must keep only ints, dropping other types."""
    values = [1, 2.5, "three", None, [4], {"five": 5}, 6, (7,), 8.0]
    result = filter_integers(values)
    assert result == [1, 6]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_empty_list():
    """Line 6: comprehension over an empty iterable yields an empty list."""
    assert filter_integers([]) == []


def test_filter_integers_all_integers():
    """Line 6: comprehension keeps every element when all are ints."""
    assert filter_integers([1, 2, 3]) == [1, 2, 3]


def test_filter_integers_negative_zero_and_bool():
    """Line 6: negative ints, zero are kept; bools are ints (subclass) and kept."""
    values = [-1, 0, "x", 2.5, True, False]
    result = filter_integers(values)
    assert result == [-1, 0, True, False]
