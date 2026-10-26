# file: project/f022/__init__.py:4-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

from typing import Any, List

import pytest

from f022 import filter_integers


def test_filter_integers_returns_only_ints():
    values: List[Any] = [1, "a", 2.5, None, 3, [4], {"k": 5}, (6,), 7]
    result = filter_integers(values)
    assert result == [1, 3, 7]
    assert all(isinstance(x, int) for x in result)


def test_filter_integers_empty_list():
    assert filter_integers([]) == []


def test_filter_integers_no_ints():
    assert filter_integers(["a", 1.0, None, b"bytes"]) == []


def test_filter_integers_all_ints():
    values = [0, -1, 42]
    result = filter_integers(values)
    assert result == values
    assert result is not values


def test_filter_integers_bool_is_int_subclass():
    # bool is a subclass of int, so True/False are kept by isinstance
    assert filter_integers([True, False, 1, 0]) == [True, False, 1, 0]


def test_filter_integers_does_not_mutate_input():
    values: List[Any] = [1, "x", 2]
    snapshot = list(values)
    filter_integers(values)
    assert values == snapshot


def test_filter_integers_accepts_tuple_iterable():
    assert filter_integers((1, "a", 2)) == [1, 2]


def test_filter_integers_raises_on_none():
    with pytest.raises(TypeError):
        filter_integers(None)
