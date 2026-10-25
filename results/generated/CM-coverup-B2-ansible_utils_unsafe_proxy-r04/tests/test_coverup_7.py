# file: project/ansible/utils/unsafe_proxy.py:117-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    _wrap_set,
    wrap_var,
)


def test_wrap_set_empty():
    result = _wrap_set(set())
    assert result == set()
    assert isinstance(result, set)


def test_wrap_set_wraps_strings():
    result = _wrap_set({"a", "b"})
    assert isinstance(result, set)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert all(isinstance(item, AnsibleUnsafe) for item in result)
    assert set(str(item) for item in result) == {"a", "b"}


def test_wrap_set_mixed_hashable_types():
    original = {"hello", b"bytes", 42, None}
    original_copy = set(original)
    result = _wrap_set(original)
    assert isinstance(result, set)
    # original must not be mutated
    assert original == original_copy
    # result is a new object
    assert result is not original
    str_items = [i for i in result if isinstance(i, AnsibleUnsafeText)]
    bytes_items = [i for i in result if isinstance(i, AnsibleUnsafeBytes)]
    assert len(str_items) == 1
    assert str(str_items[0]) == "hello"
    assert len(bytes_items) == 1
    assert bytes(bytes_items[0]) == b"bytes"
    assert 42 in result
    assert None in result


def test_wrap_set_preserves_already_unsafe():
    unsafe_str = AnsibleUnsafeText("already")
    unsafe_bytes = AnsibleUnsafeBytes(b"already-b")
    result = _wrap_set({unsafe_str, unsafe_bytes, "plain"})
    assert unsafe_str in result
    assert unsafe_bytes in result
    assert all(isinstance(item, AnsibleUnsafe) for item in result)


def test_wrap_set_via_wrap_var_dispatch():
    value = {"x", "y"}
    result = wrap_var(value)
    assert isinstance(result, set)
    assert len(result) == 2
    assert all(isinstance(item, AnsibleUnsafeText) for item in result)
    assert {str(i) for i in result} == {"x", "y"}


def test_wrap_set_frozenset_input_returns_set():
    result = _wrap_set(frozenset(["a", 1]))
    assert isinstance(result, set)
    assert type(result) is set
    assert len(result) == 2
    assert any(isinstance(i, AnsibleUnsafeText) and str(i) == "a" for i in result)
    assert 1 in result
