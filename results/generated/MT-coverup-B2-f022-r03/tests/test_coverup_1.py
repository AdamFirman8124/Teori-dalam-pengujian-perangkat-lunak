# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from typing import Any, List

from f022 import filter_integers


def test_filter_integers_mixed_types_executes_line_6():
    """Call the function with a mix of ints and non-ints so that line 6
    (the list comprehension) executes and both outcomes of the
    isinstance(x, int) condition are exercised."""
    values: List[Any] = [1, "two", 3.5, None, [4], (5,), {"six": 6}, 7, -8, 0]
    result = filter_integers(values)
    assert result == [1, 7, -8, 0]
    assert all(isinstance(x, int) and not isinstance(x, bool) for x in result)


def test_filter_integers_all_ints():
    """All elements pass the isinstance check (true branch only)."""
    assert filter_integers([10, 20, 30]) == [10, 20, 30]


def test_filter_integers_no_ints():
    """No element passes the isinstance check (false branch only)."""
    assert filter_integers(["a", 1.5, None, object()]) == []


def test_filter_integers_empty_list():
    """Empty input exercises the comprehension with zero iterations."""
    assert filter_integers([]) == []


def test_filter_integers_bools_are_ints():
    """bool is a subclass of int, so True/False pass the isinstance check."""
    result = filter_integers([True, False, "x", 2])
    assert result == [True, False, 2]
    assert all(isinstance(x, int) for x in result)
