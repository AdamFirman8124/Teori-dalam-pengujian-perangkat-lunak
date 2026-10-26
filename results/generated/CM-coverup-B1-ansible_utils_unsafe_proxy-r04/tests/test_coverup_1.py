# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

from __future__ import annotations

import pytest

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


def test_wrap_var_none():
    assert wrap_var(None) is None


def test_wrap_var_already_unsafe_passthrough():
    already = AnsibleUnsafeText(u"already unsafe")
    assert wrap_var(already) is already


def test_wrap_var_mapping():
    result = wrap_var({u"key": u"value"})
    assert isinstance(result, dict)
    assert result == {u"key": u"value"}
    for k, v in result.items():
        assert isinstance(k, AnsibleUnsafe)
        assert isinstance(v, AnsibleUnsafe)


def test_wrap_var_set():
    result = wrap_var({u"a", u"b"})
    assert isinstance(result, set)
    assert result == {u"a", u"b"}
    for item in result:
        assert isinstance(item, AnsibleUnsafe)


def test_wrap_var_list():
    result = wrap_var([u"a", u"b"])
    assert isinstance(result, list)
    assert result == [u"a", u"b"]
    for item in result:
        assert isinstance(item, AnsibleUnsafe)


def test_wrap_var_tuple():
    result = wrap_var((u"a", u"b"))
    assert isinstance(result, tuple)
    assert result == (u"a", u"b")
    for item in result:
        assert isinstance(item, AnsibleUnsafe)


def test_wrap_var_native_jinja_text():
    result = wrap_var(NativeJinjaText(u"native"))
    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"native"


def test_wrap_var_bytes():
    result = wrap_var(b"bytes value")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, binary_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"bytes value"


def test_wrap_var_text():
    result = wrap_var(u"text value")
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, text_type)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"text value"


def test_wrap_var_nested_structures():
    result = wrap_var({u"list": [u"a", (u"b",)], u"set": {u"c"}})
    assert isinstance(result, dict)
    assert isinstance(result[u"list"], list)
    assert isinstance(result[u"list"][0], AnsibleUnsafe)
    assert isinstance(result[u"list"][1], tuple)
    assert isinstance(result[u"set"], set)
    for item in result[u"set"]:
        assert isinstance(item, AnsibleUnsafe)


def test_wrap_var_non_sequence_non_text_passthrough():
    obj = object()
    assert wrap_var(obj) is obj
