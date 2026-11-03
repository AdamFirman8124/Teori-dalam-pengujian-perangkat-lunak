# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_mixed_types():
    """Covers line 6 and both branches of the isinstance check:
    integers kept (True branch), non-integers filtered out (False branch)."""
    values = [1, "two", 3.5, 4, None, [5], 6, {"seven": 7}]
    result = filter_integers(values)
    assert result == [1, 4, 6]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_empty_list():
    """Covers line 6 with an empty input (comprehension body not entered)."""
    assert filter_integers([]) == []


def test_filter_integers_no_integers():
    """Covers line 6 where every element takes the False branch."""
    values = ["a", 1.5, None, [2], (3,)]
    assert filter_integers(values) == []


def test_filter_integers_all_integers():
    """Covers line 6 where every element takes the True branch."""
    values = [10, 20, 30]
    assert filter_integers(values) == [10, 20, 30]
