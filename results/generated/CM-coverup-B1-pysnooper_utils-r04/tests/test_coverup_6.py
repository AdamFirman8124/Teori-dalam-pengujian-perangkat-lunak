# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_iterable_returns_tuple():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_generator_is_consumed_into_tuple():
    result = ensure_tuple(i * 2 for i in range(3))
    assert result == (0, 2, 4)
    assert isinstance(result, tuple)


def test_ensure_tuple_set_is_converted():
    result = ensure_tuple({1})
    assert result == (1,)
    assert isinstance(result, tuple)


def test_ensure_tuple_string_is_wrapped_not_split():
    result = ensure_tuple('abc')
    assert result == ('abc',)
    assert isinstance(result, tuple)


def test_ensure_tuple_non_iterable_is_wrapped():
    result = ensure_tuple(42)
    assert result == (42,)
    assert isinstance(result, tuple)


def test_ensure_tuple_none_is_wrapped():
    result = ensure_tuple(None)
    assert result == (None,)
    assert isinstance(result, tuple)


def test_ensure_tuple_empty_iterable_returns_empty_tuple():
    result = ensure_tuple([])
    assert result == ()
    assert isinstance(result, tuple)


def test_ensure_tuple_tuple_passthrough_equality():
    original = (1, 2)
    result = ensure_tuple(original)
    assert result == original
    assert isinstance(result, tuple)
