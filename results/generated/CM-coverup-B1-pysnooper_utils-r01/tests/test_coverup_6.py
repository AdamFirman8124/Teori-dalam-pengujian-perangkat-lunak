# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest

from pysnooper.utils import ensure_tuple


def test_ensure_tuple_iterable_non_string_returns_tuple():
    result = ensure_tuple([1, 2, 3])
    assert isinstance(result, tuple)
    assert result == (1, 2, 3)


def test_ensure_tuple_generator_is_consumed_into_tuple():
    result = ensure_tuple(i * 2 for i in range(3))
    assert isinstance(result, tuple)
    assert result == (0, 2, 4)


def test_ensure_tuple_string_is_wrapped_not_split():
    result = ensure_tuple('abc')
    assert isinstance(result, tuple)
    assert result == ('abc',)


def test_ensure_tuple_non_iterable_is_wrapped():
    result = ensure_tuple(42)
    assert isinstance(result, tuple)
    assert result == (42,)


def test_ensure_tuple_none_is_wrapped():
    result = ensure_tuple(None)
    assert isinstance(result, tuple)
    assert result == (None,)


def test_ensure_tuple_empty_iterable_returns_empty_tuple():
    result = ensure_tuple([])
    assert isinstance(result, tuple)
    assert result == ()


def test_ensure_tuple_dict_iterates_keys():
    result = ensure_tuple({'a': 1, 'b': 2})
    assert isinstance(result, tuple)
    assert set(result) == {'a', 'b'}
    assert len(result) == 2


def test_ensure_tuple_bytes_is_iterable_and_not_string():
    result = ensure_tuple(b'ab')
    assert isinstance(result, tuple)
    assert result == (97, 98)


def test_ensure_tuple_already_tuple_is_preserved():
    original = (1, 2)
    result = ensure_tuple(original)
    assert isinstance(result, tuple)
    assert result == original
