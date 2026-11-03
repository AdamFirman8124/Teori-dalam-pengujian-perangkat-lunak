# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from f022 import filter_integers


def test_filter_integers_mixed_types():
    """Line 6 executes; both branches of the isinstance filter are taken."""
    values = [1, "two", 3.5, None, [4], 5, {"six": 6}, 7]
    result = filter_integers(values)
    assert result == [1, 5, 7]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_all_integers():
    """All elements pass the filter (True branch only)."""
    assert filter_integers([10, 20, 30]) == [10, 20, 30]


def test_filter_integers_no_integers():
    """No elements pass the filter (False branch only)."""
    assert filter_integers(["a", 1.5, None, [2], (3,)]) == []


def test_filter_integers_empty_list():
    """Empty input yields empty output; comprehension body never runs."""
    assert filter_integers([]) == []


def test_filter_integers_preserves_order_and_duplicates():
    """Order and duplicates of the kept integers are preserved."""
    values = [3, "x", 3, 2.0, -1, 0]
    result = filter_integers(values)
    assert result == [3, 3, -1, 0]
