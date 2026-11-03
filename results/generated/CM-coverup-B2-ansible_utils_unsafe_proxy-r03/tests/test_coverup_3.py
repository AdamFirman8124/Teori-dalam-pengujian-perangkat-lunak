# file: project/ansible/utils/unsafe_proxy.py:109-114
# asked: {"lines": [113, 114], "branches": []}
# gained: {"lines": [113, 114], "branches": []}

"""Tests targeting lines 113-114 of ansible/utils/unsafe_proxy.py (_wrap_sequence).

These functions are pure (no I/O, no global state), so no monkeypatching or
cleanup is required; nothing is mutated at module or interpreter level.
"""

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_sequence,
    wrap_var,
)


def test_wrap_sequence_list():
    """A list input hits lines 113-114 and is rebuilt as a list of unsafe items."""
    result = _wrap_sequence(['a', 'b'])
    assert type(result) is list
    assert result == ['a', 'b']
    for item in result:
        assert isinstance(item, AnsibleUnsafeText)
        assert isinstance(item, AnsibleUnsafe)
        assert item.__UNSAFE__ is True


def test_wrap_sequence_tuple():
    """A tuple input hits lines 113-114 and is rebuilt as a tuple of unsafe items."""
    result = _wrap_sequence(('a', 'b'))
    assert type(result) is tuple
    assert result == ('a', 'b')
    for item in result:
        assert isinstance(item, AnsibleUnsafeText)
        assert item.__UNSAFE__ is True


def test_wrap_sequence_empty_list():
    """An empty sequence still executes lines 113-114."""
    result = _wrap_sequence([])
    assert result == []
    assert type(result) is list


def test_wrap_sequence_preserves_subclass():
    """Line 113 captures type(v), so a list subclass type is preserved on line 114."""

    class MyList(list):
        pass

    result = _wrap_sequence(MyList(['a']))
    assert type(result) is MyList
    assert result == ['a']
    assert isinstance(result[0], AnsibleUnsafeText)


def test_wrap_sequence_nested_containers():
    """Nested lists/tuples are recursively wrapped via wrap_var."""
    result = _wrap_sequence([['x'], ('y',)])
    assert type(result) is list
    assert type(result[0]) is list
    assert type(result[1]) is tuple
    assert all(isinstance(item, AnsibleUnsafeText) for sub in result for item in sub)


def test_wrap_sequence_mixed_item_types():
    """Each item is wrapped per its own type; non-wrappable items pass through."""
    result = _wrap_sequence(['s', b'b', None, 42])
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[1], AnsibleUnsafeBytes)
    assert result[2] is None
    assert result[3] == 42


def test_wrap_var_list_reaches_wrap_sequence():
    """wrap_var() with a list routes through _wrap_sequence (lines 113-114)."""
    result = wrap_var(['a', 'b'])
    assert type(result) is list
    assert result == ['a', 'b']
    assert all(item.__UNSAFE__ for item in result)


def test_wrap_var_tuple_reaches_wrap_sequence():
    """wrap_var() with a tuple routes through _wrap_sequence (lines 113-114)."""
    result = wrap_var(('a', 'b'))
    assert type(result) is tuple
    assert result == ('a', 'b')
    assert all(item.__UNSAFE__ for item in result)
