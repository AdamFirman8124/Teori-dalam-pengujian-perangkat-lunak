# file: project/ansible/utils/unsafe_proxy.py:121-138
# asked: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}
# gained: {"lines": [122, 123, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 138], "branches": [[122, 123], [122, 125], [125, 126], [125, 127], [127, 128], [127, 129], [129, 130], [129, 131], [131, 132], [131, 133], [133, 134], [133, 135], [135, 136], [135, 138]]}

import pytest

from ansible.utils.native_jinja import NativeJinjaText
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    NativeJinjaUnsafeText,
    wrap_var,
)


def test_wrap_var_none_returns_none():
    assert wrap_var(None) is None


def test_wrap_var_already_unsafe_text_returns_same_object():
    v = AnsibleUnsafeText("already unsafe")
    assert wrap_var(v) is v


def test_wrap_var_already_unsafe_bytes_returns_same_object():
    v = AnsibleUnsafeBytes(b"already unsafe")
    assert wrap_var(v) is v


def test_wrap_var_already_unsafe_native_jinja_returns_same_object():
    v = NativeJinjaUnsafeText("already unsafe")
    assert wrap_var(v) is v


def test_wrap_var_mapping_is_wrapped():
    v = {"key": "value", "num": 1, "none": None}
    result = wrap_var(v)
    assert isinstance(result, dict)
    assert result is not v
    # keys and string values are wrapped as unsafe
    for k, item in result.items():
        assert isinstance(k, AnsibleUnsafeText)
    assert isinstance(result["key"], AnsibleUnsafeText)
    assert result["key"] == "value"
    assert result["num"] == 1
    assert type(result["num"]) is int
    assert result["none"] is None


def test_wrap_var_set_is_wrapped():
    v = {"a", "b"}
    result = wrap_var(v)
    assert isinstance(result, set)
    assert result is not v
    assert result == {"a", "b"}
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)


def test_wrap_var_sequence_list_is_wrapped():
    v = ["a", b"b", 1, None]
    result = wrap_var(v)
    assert isinstance(result, list)
    assert result is not v
    assert result[0] == "a"
    assert isinstance(result[0], AnsibleUnsafeText)
    assert isinstance(result[0], AnsibleUnsafe)
    assert result[1] == b"b"
    assert isinstance(result[1], AnsibleUnsafeBytes)
    assert result[2] == 1
    assert type(result[2]) is int
    assert result[3] is None


def test_wrap_var_sequence_tuple_preserves_type():
    v = ("a", 42)
    result = wrap_var(v)
    assert isinstance(result, tuple)
    assert type(result) is tuple
    assert result[0] == "a"
    assert isinstance(result[0], AnsibleUnsafeText)
    assert result[1] == 42


def test_wrap_var_native_jinja_text_becomes_native_jinja_unsafe():
    v = NativeJinjaText("jinja text")
    result = wrap_var(v)
    assert isinstance(result, NativeJinjaUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, NativeJinjaText)
    assert result == "jinja text"


def test_wrap_var_bytes_becomes_unsafe_bytes():
    v = b"hello bytes"
    result = wrap_var(v)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"hello bytes"


def test_wrap_var_text_becomes_unsafe_text():
    v = "hello"
    result = wrap_var(v)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == "hello"


def test_wrap_var_passthrough_non_string_returns_as_is():
    v = 42
    result = wrap_var(v)
    assert result == 42
    assert type(result) is int
    assert result is v

    f = 3.14
    assert wrap_var(f) is f
