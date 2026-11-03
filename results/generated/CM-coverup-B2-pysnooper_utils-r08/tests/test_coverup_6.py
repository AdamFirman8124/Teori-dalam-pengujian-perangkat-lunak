# file: project/pysnooper/utils.py:90-95
# asked: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}
# gained: {"lines": [91, 92, 93, 95], "branches": [[91, 93], [91, 95]]}

"""
Tests for pysnooper.utils.ensure_tuple.

These tests exercise every line and branch of ensure_tuple:

* An iterable that is NOT a string  -> gets unpacked via ``tuple(x)`` (lines 91-93).
* A string (iterable, but special-cased) -> short-circuits to ``(x,)`` (lines 91-92, 95).
* A non-iterable -> the ``and`` short-circuits and ``(x,)`` is returned (lines 91, 95).

``ensure_tuple`` is a pure function with no side effects, so no cleanup /
monkeypatching is required; nothing here mutates global or module state.
"""

import pytest

from pysnooper import utils


def test_ensure_tuple_list_is_unpacked():
    """A list is iterable and not a string, so it must become a tuple."""
    result = utils.ensure_tuple([1, 2, 3])
    assert isinstance(result, tuple)
    assert result == (1, 2, 3)


def test_ensure_tuple_generator_is_consumed():
    """Any non-string iterable (e.g. a generator) is unpacked."""
    result = utils.ensure_tuple(x * 2 for x in range(3))
    assert isinstance(result, tuple)
    assert result == (0, 2, 4)


def test_ensure_tuple_set_and_dict_are_unpacked():
    """Sets and dicts are iterable non-strings too."""
    assert utils.ensure_tuple({1, 2}) in ((1, 2), (2, 1))
    assert utils.ensure_tuple({'a': 1, 'b': 2}) == ('a', 'b')


def test_ensure_tuple_empty_iterable():
    """An empty iterable yields an empty tuple, not a 1-tuple."""
    result = utils.ensure_tuple([])
    assert result == ()
    assert isinstance(result, tuple)


def test_ensure_tuple_string_is_wrapped_not_unpacked():
    """Strings ARE iterable but must be wrapped, covering the False branch
    of ``not isinstance(x, string_types)``."""
    result = utils.ensure_tuple('abc')
    assert isinstance(result, tuple)
    assert result == ('abc',)
    # Make sure the string was not exploded into characters.
    assert len(result) == 1
    assert result[0] == 'abc'


def test_ensure_tuple_non_iterable_int_is_wrapped():
    """Ints are not iterable, so the first isinstance check fails and the
    ``and`` short-circuits straight to the else branch."""
    result = utils.ensure_tuple(42)
    assert result == (42,)
    assert isinstance(result, tuple)


def test_ensure_tuple_none_is_wrapped():
    """None is not iterable either."""
    result = utils.ensure_tuple(None)
    assert result == (None,)


def test_ensure_tuple_arbitrary_object_is_wrapped():
    """Plain objects are not iterable and must simply be wrapped."""

    class Foo(object):
        pass

    obj = Foo()
    result = utils.ensure_tuple(obj)
    assert result == (obj,)
    assert result[0] is obj


@pytest.mark.parametrize('value, expected', [
    ([1, 2], (1, 2)),
    ((1, 2), (1, 2)),          # tuples are iterable non-strings
    ('hi', ('hi',)),           # strings stay wrapped
    (3.5, (3.5,)),             # floats are not iterable
    (b'xy', (120, 121)),       # bytes are iterable non-strings under py3
])
def test_ensure_tuple_parametrized(value, expected):
    assert utils.ensure_tuple(value) == expected
