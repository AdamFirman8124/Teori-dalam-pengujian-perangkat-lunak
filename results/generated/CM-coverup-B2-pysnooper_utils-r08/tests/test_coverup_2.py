# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import pytest

from pysnooper import utils


class ExplodingRepr(object):
    """Class whose repr raises an exception."""

    def __repr__(self):
        raise ValueError('repr failed')


class AddressedObject(object):
    """Class whose repr mimics the default repr, including a memory address."""

    def __repr__(self):
        return 'AddressedObject object at 0x1234abcd'


class MultilineRepr(object):
    """Class whose repr contains actual carriage returns and newlines."""

    def __repr__(self):
        return 'a\r\nb\nc\rd'


class LongRepr(object):
    """Class whose repr is a known 10-character string."""

    def __repr__(self):
        return 'abcdefghij'


class Custom(object):
    """Class used to exercise custom_repr handling."""


def test_get_shortish_repr_basic():
    """Lines 68-70, 73, 78: normal repr path (repr of a str is quoted)."""
    assert utils.get_shortish_repr('foo') == "'foo'"
    assert utils.get_shortish_repr(LongRepr()) == 'abcdefghij'


def test_get_shortish_repr_strips_newlines_and_carriage_returns():
    """Line 73: '\\r' and '\\n' characters are removed from the repr."""
    result = utils.get_shortish_repr(MultilineRepr())
    assert result == 'abcd'


def test_get_shortish_repr_failed_repr():
    """Lines 71-72: exception raised inside repr is caught."""
    assert utils.get_shortish_repr(ExplodingRepr()) == 'REPR FAILED'


def test_get_shortish_repr_failed_repr_with_max_length():
    """Lines 71-72 combined with 76-77: 'REPR FAILED' is also truncated."""
    result = utils.get_shortish_repr(ExplodingRepr(), max_length=8)
    assert result == 'RE...LED'
    assert len(result) == 8


def test_get_shortish_repr_normalize():
    """Lines 74-75: normalize=True strips memory addresses."""
    result = utils.get_shortish_repr(AddressedObject(), normalize=True)
    assert result == 'AddressedObject object'
    assert '0x' not in result


def test_get_shortish_repr_no_normalize_leaves_address():
    """Line 74 (False branch): address kept when normalize=False."""
    result = utils.get_shortish_repr(AddressedObject())
    assert result == 'AddressedObject object at 0x1234abcd'


def test_get_shortish_repr_max_length_truncates():
    """Lines 76-77: long reprs are truncated with '...' in the middle."""
    result = utils.get_shortish_repr(LongRepr(), max_length=5)
    assert result == 'a...j'
    assert len(result) == 5


def test_get_shortish_repr_max_length_short_string_unchanged():
    """Line 76 (True branch) with a short repr: returned as-is."""
    assert utils.get_shortish_repr(LongRepr(), max_length=10) == 'abcdefghij'


def test_get_shortish_repr_no_max_length():
    """Line 76 (False branch): max_length=None leaves repr untouched."""
    assert utils.get_shortish_repr(LongRepr()) == 'abcdefghij'


def test_get_shortish_repr_custom_repr_callable_condition():
    """Line 68: custom_repr with a callable condition is honored."""
    result = utils.get_shortish_repr(
        Custom(),
        custom_repr=((lambda x: isinstance(x, Custom), lambda x: 'CUSTOM!'),),
    )
    assert result == 'CUSTOM!'


def test_get_shortish_repr_custom_repr_type_condition():
    """Line 68: custom_repr with a type as condition is honored."""
    result = utils.get_shortish_repr(
        Custom(), custom_repr=((Custom, lambda x: 'TYPED!'),))
    assert result == 'TYPED!'


def test_get_shortish_repr_custom_repr_not_matching_falls_back():
    """Line 68: non-matching custom_repr falls back to default repr."""
    assert utils.get_shortish_repr(
        'foo', custom_repr=((Custom, lambda x: 'TYPED!'),)) == "'foo'"


def test_get_shortish_repr_combined_options():
    """Lines 68-78 together: custom repr + newline strip + normalize + truncate."""
    result = utils.get_shortish_repr(
        AddressedObject(),
        custom_repr=((AddressedObject,
                      lambda x: 'hello at 0xdeadbeef\nworld'),),
        max_length=7,
        normalize=True,
    )
    # Newline stripped -> 'hello at 0xdeadbeefworld',
    # address normalized away -> 'helloworld', then truncated.
    assert result == 'he...ld'
    assert len(result) == 7
