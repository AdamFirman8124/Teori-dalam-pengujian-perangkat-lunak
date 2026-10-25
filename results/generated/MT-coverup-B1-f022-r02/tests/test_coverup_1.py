# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from typing import List, Any

from f022 import filter_integers


def test_filter_integers_mixed_types():
    values: List[Any] = [1, "two", 3.0, 4, None, [5], 6]
    result = filter_integers(values)
    assert result == [1, 4, 6]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_bool_is_int():
    # bool is a subclass of int, so True/False pass the isinstance check
    assert filter_integers([True, False]) == [True, False]


def test_filter_integers_all_integers():
    assert filter_integers([1, 2, 3]) == [1, 2, 3]


def test_filter_integers_no_integers():
    assert filter_integers(["a", 2.5, None, [1]]) == []


def test_filter_integers_empty():
    assert filter_integers([]) == []
