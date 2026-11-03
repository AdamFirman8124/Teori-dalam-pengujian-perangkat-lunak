# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from __future__ import annotations

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
    """Lines 122-123: None short-circuits and is returned as-is."""
    assert wrap_var(None) is None


def test_wrap_var_already_unsafe_returned_unchanged():
    """Lines 122-123: values already marked unsafe are returned as-is."""
    unsafe_text = AnsibleUnsafeText(u'foo')
    assert wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'foo')
    assert wrap_var(unsafe_bytes) is unsafe_bytes


def test_wrap_var_mapping():
    """Lines 125-126: Mapping is wrapped via _wrap_dict (keys and values)."""
    result = wrap_var({u'key': u'value', u'nested': {u'inner': u'item'}})
    assert isinstance(result, dict)
    assert result == {u'key': u'value', u'nested': {u'inner': u'item'}}
    assert isinstance(result[u'key'], AnsibleUnsafeText)
    assert isinstance(result[u'nested'][u'inner'], AnsibleUnsafeText)
    # keys are wrapped as well
    assert all(isinstance(k, AnsibleUnsafe) for k in result)


def test_wrap_var_set():
    """Lines 127-128: Set is wrapped via _wrap_set."""
    result = wrap_var({u'a', u'b'})
    assert isinstance(result, set)
    assert result == {u'a', u'b'}
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_var_sequence_list():
    """Lines 129-130: list is wrapped via _wrap_sequence, recursively."""
    result = wrap_var([u'a', u'b', [u'c']])
    assert isinstance(result, list)
    assert result == [u'a', u'b', [u'c']]
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[1], AnsibleUnsafeText)
    assert isinstance(result[2][0], AnsibleUnsafeText)


def test_wrap_var_sequence_tuple_preserves_type():
    """Lines 129-130: _wrap_sequence preserves the concrete sequence type."""
    result = wrap_var((u'a', u'b'))
    assert isinstance(result, tuple)
    assert result == (u'a', u'b')
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_var_native_jinja_text():
    """Lines 131-132: NativeJinjaText becomes NativeJinjaUnsafeText."""
    result = wrap_var(NativeJinjaText(u'foo'))
    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'foo'


def test_wrap_var_bytes():
    """Lines 133-134: bytes become AnsibleUnsafeBytes."""
    result = wrap_var(b'foo')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, binary_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'foo'


def test_wrap_var_text():
    """Lines 135-136: text becomes AnsibleUnsafeText."""
    result = wrap_var(u'foo')
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'foo'


def test_wrap_var_other_types_pass_through():
    """Line 138: non-wrappable types fall through and are returned unchanged."""
    assert wrap_var(1) == 1
    assert wrap_var(1.5) == 1.5
    assert wrap_var(True) is True
    obj = object()
    assert wrap_var(obj) is obj


def test_wrap_var_nested_structure():
    """Exercise several branches at once via a nested container."""
    result = wrap_var({
        u'list': [u'a', (u'b',)],
        u'set': {u'c'},
        u'bytes': b'd',
        u'nj': NativeJinjaText(u'e'),
        u'int': 1,
    })
    assert isinstance(result, dict)
    assert isinstance(result[u'list'][0], AnsibleUnsafeText)
    assert isinstance(result[u'list'][1][0], AnsibleUnsafeText)
    assert isinstance(result[u'set'], set)
    assert all(isinstance(i, AnsibleUnsafeText) for i in result[u'set'])
    assert isinstance(result[u'bytes'], AnsibleUnsafeBytes)
    assert isinstance(result[u'nj'], NativeJinjaUnsafeText)
    assert result[u'int'] == 1
