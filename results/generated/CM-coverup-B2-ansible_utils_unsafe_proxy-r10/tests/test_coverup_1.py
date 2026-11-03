# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

# -*- coding: utf-8 -*-
# Tests for ansible/utils/unsafe_proxy.py::wrap_var (lines 122-138).
# wrap_var is a pure function (no global/module state is mutated), so no
# monkeypatching/cleanup is required; each test is fully self-contained.
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.common._collections_compat import Mapping, Set
from ansible.module_utils.six import binary_type, text_type
from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)


def test_wrap_var_none_returns_none():
    """Lines 122-123: ``v is None`` short-circuits to ``return v``."""
    assert wrap_var(None) is None


def test_wrap_var_already_unsafe_text_passthrough():
    """Lines 122-123: values already marked unsafe are returned unchanged."""
    value = AnsibleUnsafeText(u'unsafe')
    result = wrap_var(value)
    assert result is value
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_already_unsafe_bytes_passthrough():
    """Lines 122-123: unsafe bytes are returned unchanged."""
    value = AnsibleUnsafeBytes(b'unsafe')
    result = wrap_var(value)
    assert result is value
    assert isinstance(result, AnsibleUnsafe)


def test_wrap_var_ansible_unsafe_base_passthrough():
    """Lines 122-123: bare AnsibleUnsafe instances are returned unchanged."""
    value = AnsibleUnsafe()
    assert wrap_var(value) is value


def test_wrap_var_mapping_recursively_wrapped():
    """Lines 125-126: Mapping branch dispatches to _wrap_dict.

    _wrap_dict wraps both keys and values, so every (string) key in the
    resulting mapping must be an unsafe text instance.
    """
    value = {'a': 1, 'b': u'text', 'c': [u'x', 2], 'd': {'e': u'inner'}}
    result = wrap_var(value)
    assert isinstance(result, Mapping)
    assert result == value
    # all string keys are wrapped
    wrapped_keys = list(result)
    assert len(wrapped_keys) == len(value)
    for orig, wrapped in zip(sorted(value), sorted(wrapped_keys)):
        assert isinstance(wrapped, AnsibleUnsafe)
        assert isinstance(wrapped, AnsibleUnsafeText)
        assert wrapped == orig
    # (recursively) string values are wrapped
    assert isinstance(result['b'], AnsibleUnsafeText)
    assert isinstance(result['c'][0], AnsibleUnsafeText)
    assert isinstance(result['d']['e'], AnsibleUnsafeText)
    # non-string values are left alone
    assert result['a'] == 1
    assert result['c'][1] == 2


def test_wrap_var_mapping_does_not_double_wrap_unsafe():
    """Lines 122-123 via recursion: already-unsafe members are not re-wrapped."""
    unsafe = AnsibleUnsafeText(u'unsafe')
    result = wrap_var({'k': unsafe})
    assert result['k'] is unsafe


def test_wrap_var_set_items_wrapped():
    """Lines 127-128: Set branch dispatches to _wrap_set."""
    value = {1, u'a'}
    result = wrap_var(value)
    assert isinstance(result, Set)
    assert isinstance(result, set)
    assert result == value
    unsafe_items = [item for item in result if isinstance(item, AnsibleUnsafe)]
    assert len(unsafe_items) == 1
    assert isinstance(unsafe_items[0], AnsibleUnsafeText)
    assert unsafe_items[0] == u'a'


def test_wrap_var_frozenset_items_wrapped():
    """Lines 127-128: frozenset also takes the Set branch."""
    value = frozenset([u'a', 1])
    result = wrap_var(value)
    assert isinstance(result, Set)
    assert result == value
    assert all(not isinstance(item, text_type) or isinstance(item, AnsibleUnsafeText)
               for item in result)


def test_wrap_var_list_items_wrapped():
    """Lines 129-130: sequence branch dispatches to _wrap_sequence."""
    value = [1, u'a', b'bytes', None]
    result = wrap_var(value)
    assert isinstance(result, list)
    assert result == value
    assert isinstance(result[1], AnsibleUnsafeText)
    assert isinstance(result[2], AnsibleUnsafeBytes)
    assert result[3] is None
    assert result[0] == 1


def test_wrap_var_tuple_items_wrapped():
    """Lines 129-130: tuples keep their type via _wrap_sequence."""
    value = (1, u'a')
    result = wrap_var(value)
    assert isinstance(result, tuple)
    assert result == value
    assert isinstance(result[1], AnsibleUnsafeText)


def test_wrap_var_list_does_not_double_wrap_unsafe():
    """Lines 122-123 via recursion: already-unsafe members are not re-wrapped."""
    unsafe = AnsibleUnsafeText(u'unsafe')
    result = wrap_var([unsafe])
    assert result[0] is unsafe


def test_wrap_var_native_jinja_text():
    """Lines 131-132: NativeJinjaText branch (checked before text_type)."""
    value = NativeJinjaText(u'native')
    result = wrap_var(value)
    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'native'


def test_wrap_var_bytes():
    """Lines 133-134: binary_type branch."""
    value = b'bytes'
    result = wrap_var(value)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, binary_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'bytes'


def test_wrap_var_text():
    """Lines 135-136: text_type branch."""
    value = u'text'
    result = wrap_var(value)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'text'


def test_wrap_var_other_type_passthrough():
    """Line 138: values matching no branch fall through and are returned as-is."""
    value = 42
    assert wrap_var(value) is value


def test_wrap_var_bool_passthrough():
    """Line 138: bool matches no branch and is returned unchanged."""
    assert wrap_var(True) is True
