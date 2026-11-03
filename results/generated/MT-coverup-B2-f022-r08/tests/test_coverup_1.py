# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_mixed_types():
    """Exercises line 6 with both branches of the isinstance filter taken."""
    values = [1, "a", 2.5, 3, None, [4], {"k": 6}, 5]
    result = filter_integers(values)
    assert result == [1, 3, 5]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_all_ints():
    """All elements pass the filter (True branch of isinstance)."""
    result = filter_integers([10, 20, 30])
    assert result == [10, 20, 30]


def test_filter_integers_no_ints():
    """No element passes the filter (False branch of isinstance)."""
    result = filter_integers(["x", 3.14, None, [1], (2,)])
    assert result == []


def test_filter_integers_empty_list():
    """Empty input: comprehension body never runs, line 6 still executes."""
    assert filter_integers([]) == []
