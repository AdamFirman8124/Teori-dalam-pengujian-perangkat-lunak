# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

# -*- coding: utf-8 -*-
# (c) Test coverage for ansible/utils/unsafe_proxy.py lines 113-114 (_wrap_sequence)
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    wrap_var,
)


def test_wrap_var_list():
    """A list input must hit _wrap_sequence and return a list of unsafe text."""
    value = [u'foo', u'bar']
    result = wrap_var(value)

    assert isinstance(result, list)
    assert result == value  # values are preserved
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    # sanity: the original items were not unsafe
    assert not any(isinstance(item, AnsibleUnsafe) for item in value)


def test_wrap_var_tuple():
    """A tuple input must hit _wrap_sequence and return a tuple of unsafe text."""
    value = (u'foo', u'bar')
    result = wrap_var(value)

    assert isinstance(result, tuple)
    assert result == value
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_var_nested_sequences():
    """Nested lists/tuples inside a sequence are recursively wrapped."""
    value = [u'foo', [u'bar'], (u'baz',)]
    result = wrap_var(value)

    assert isinstance(result, list)
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[1], list)
    assert isinstance(result[1][0], AnsibleUnsafeText)
    assert isinstance(result[2], tuple)
    assert isinstance(result[2][0], AnsibleUnsafeText)


def test_wrap_var_empty_sequences():
    """Empty list/tuple still go through _wrap_sequence."""
    empty_list = wrap_var([])
    empty_tuple = wrap_var(())

    assert isinstance(empty_list, list)
    assert empty_list == []
    assert isinstance(empty_tuple, tuple)
    assert empty_tuple == ()


def test_wrap_var_sequence_mixed_types():
    """Bytes, None and text items inside a sequence are wrapped appropriately."""
    value = [b'foo', None, u'bar']
    result = wrap_var(value)

    assert isinstance(result, list)
    assert isinstance(result[0], AnsibleUnsafeBytes)
    assert result[1] is None
    assert isinstance(result[2], AnsibleUnsafeText)


def test_wrap_var_sequence_with_unsafe_items():
    """Items that are already unsafe are passed through unchanged."""
    unsafe_item = AnsibleUnsafeText(u'foo')
    value = [unsafe_item]
    result = wrap_var(value)

    assert isinstance(result, list)
    assert result[0] is unsafe_item
