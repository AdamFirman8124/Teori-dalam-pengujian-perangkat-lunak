# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

import pytest

from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)
from ansible.utils.native_jinja import NativeJinjaText


def test_wrap_var_none_and_already_unsafe():
    assert wrap_var(None) is None

    unsafe_text = AnsibleUnsafeText(u'unsafe')
    assert wrap_var(unsafe_text) is unsafe_text

    unsafe_bytes = AnsibleUnsafeBytes(b'unsafe')
    assert wrap_var(unsafe_bytes) is unsafe_bytes


def test_wrap_var_mapping():
    result = wrap_var({u'key': u'value', u'nested': {u'inner': u'deep'}})

    assert isinstance(result, dict)
    assert isinstance(result[u'key'], AnsibleUnsafeText)
    assert result[u'key'] == u'value'
    assert isinstance(result[u'nested'], dict)
    assert isinstance(result[u'nested'][u'inner'], AnsibleUnsafeText)
    assert result[u'nested'][u'inner'] == u'deep'


def test_wrap_var_set():
    result = wrap_var({u'a', u'b'})

    assert isinstance(result, set)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(item) for item in result} == {u'a', u'b'}


def test_wrap_var_sequence():
    result = wrap_var([u'a', u'b'])

    assert isinstance(result, list)
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert [str(item) for item in result] == [u'a', u'b']

    tuple_result = wrap_var((u'a', u'b'))
    assert isinstance(tuple_result, tuple)
    assert all(isinstance(item, AnsibleUnsafeText) for item in tuple_result)
    assert [str(item) for item in tuple_result] == [u'a', u'b']


def test_wrap_var_native_jinja_text():
    native = NativeJinjaText(u'native')
    result = wrap_var(native)

    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, NativeJinjaText)
    assert result == u'native'


def test_wrap_var_bytes():
    result = wrap_var(b'bytes')

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b'bytes'


def test_wrap_var_text():
    result = wrap_var(u'text')

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'text'


def test_wrap_var_other_type_unchanged():
    sentinel = object()
    assert wrap_var(sentinel) is sentinel

    assert wrap_var(42) == 42
    assert not isinstance(wrap_var(42), AnsibleUnsafe)
