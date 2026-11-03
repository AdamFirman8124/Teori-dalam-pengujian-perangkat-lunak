# file: project/pysnooper/utils.py:67-78
# asked: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}
# gained: {"lines": [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[74, 75], [74, 76], [76, 77], [76, 78]]}

import pytest

from pysnooper.utils import get_shortish_repr


class ExplodingRepr(object):
    def __repr__(self):
        raise ValueError('boom')


class MultilineRepr(object):
    def __repr__(self):
        return 'line1\r\nline2\nline3'


class AddressedRepr(object):
    def __repr__(self):
        return '<AddressedRepr object at 0xDEADBEEF>'


class LongRepr(object):
    def __repr__(self):
        return 'a' * 100


def test_default_repr_used():
    # Covers lines 68-70, 73, 78 (happy path, fallback to builtin repr).
    assert get_shortish_repr(42) == '42'


def test_custom_repr_with_type_condition():
    # Covers the isinstance(condition, type) branch inside get_repr_function.
    class Foo(object):
        def __repr__(self):
            return 'default repr'

    result = get_shortish_repr(Foo(),
                               custom_repr=((Foo, lambda x: 'custom!'),))
    assert result == 'custom!'


def test_custom_repr_with_callable_condition():
    # Covers the non-type (callable) condition branch in get_repr_function.
    result = get_shortish_repr(
        object(), custom_repr=((lambda x: True, lambda x: 'matched'),))
    assert result == 'matched'


def test_custom_repr_not_matching_falls_back_to_repr():
    # Covers the loop falling through to the default repr.
    class Bar(object):
        def __repr__(self):
            return 'bar repr'

    result = get_shortish_repr(
        Bar(), custom_repr=((lambda x: False, lambda x: 'nope'),))
    assert result == 'bar repr'


def test_repr_failure_returns_placeholder():
    # Covers lines 71-72 (exception handler producing 'REPR FAILED').
    assert get_shortish_repr(ExplodingRepr()) == 'REPR FAILED'


def test_newlines_and_carriage_returns_removed():
    # Covers the .replace() calls on line 73.
    assert get_shortish_repr(MultilineRepr()) == 'line1line2line3'


def test_no_normalization_by_default():
    # Covers the False branch of `if normalize:`.
    assert get_shortish_repr(AddressedRepr()) == \
        '<AddressedRepr object at 0xDEADBEEF>'


def test_normalize_removes_memory_address():
    # Covers lines 74-75 (True branch of `if normalize:`).
    result = get_shortish_repr(AddressedRepr(), normalize=True)
    assert result == '<AddressedRepr object>'
    assert '0x' not in result


def test_no_truncation_when_under_max_length():
    # Covers the inner early-return of truncate() (len <= max_length).
    assert get_shortish_repr(123456, max_length=100) == '123456'


def test_truncation_when_over_max_length():
    # Covers lines 76-77 (True branch of `if max_length:` plus truncate()).
    result = get_shortish_repr(LongRepr(), max_length=11)
    left = (11 - 3) // 2    # 4
    right = 11 - 3 - left   # 4
    assert len(result) == 11
    assert result == 'a' * left + '...' + 'a' * right


def test_max_length_zero_is_ignored():
    # Covers the False branch of `if max_length:` (0 is falsy).
    assert get_shortish_repr(42, max_length=0) == '42'


def test_combined_normalize_and_truncate():
    # Exercises normalize followed by truncation in one call.
    class Big(object):
        def __repr__(self):
            return 'X' * 30 + ' at 0x1234ABCD' + 'Y' * 30

    result = get_shortish_repr(Big(), max_length=20, normalize=True)
    assert len(result) == 20
    assert '0x' not in result
    assert result == 'X' * 8 + '...' + 'Y' * 9
