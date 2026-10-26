# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

import pytest

from pysnooper.utils import ensure_tuple
from pysnooper.pycompat import string_types, collections_abc


def test_ensure_tuple_iterable_non_string():
    result = ensure_tuple([1, 2, 3])
    assert result == (1, 2, 3)
    assert isinstance(result, tuple)


def test_ensure_tuple_generator():
    result = ensure_tuple(x for x in range(3))
    assert result == (0, 1, 2)
    assert isinstance(result, tuple)


def test_ensure_tuple_string():
    result = ensure_tuple('abc')
    assert result == ('abc',)
    assert isinstance(result, tuple)


def test_ensure_tuple_non_iterable():
    result = ensure_tuple(42)
    assert result == (42,)
    assert isinstance(result, tuple)


def test_ensure_tuple_none():
    result = ensure_tuple(None)
    assert result == (None,)
    assert isinstance(result, tuple)
