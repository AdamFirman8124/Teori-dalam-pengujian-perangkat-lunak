# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.display import Display
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    AnsibleUnsafeText,
    UnsafeProxy,
)


def _patch_deprecated(monkeypatch):
    calls = []

    def _fake_deprecated(self, *args, **kwargs):
        calls.append((args, kwargs))
        return None

    monkeypatch.setattr(Display, "deprecated", _fake_deprecated)
    return calls


def test_unsafeproxy_passthrough_ansible_unsafe_text(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    original = AnsibleUnsafeText(u"already unsafe")
    result = UnsafeProxy(original)
    assert result is original
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"already unsafe"
    assert len(calls) == 1
    args, kwargs = calls[0]
    assert "UnsafeProxy is being deprecated" in args[0]
    assert kwargs.get("version") == "2.13"
    assert kwargs.get("collection_name") == "ansible.builtin"


def test_unsafeproxy_passthrough_ansible_unsafe_bytes(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    original = AnsibleUnsafeBytes(b"already unsafe bytes")
    result = UnsafeProxy(original)
    assert result is original
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert len(calls) == 1


def test_unsafeproxy_wraps_text_string(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    result = UnsafeProxy(u"hello")
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"hello"
    assert type(result) is AnsibleUnsafeText
    assert len(calls) == 1


def test_unsafeproxy_returns_byte_string_unchanged(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    original = b"hello bytes"
    result = UnsafeProxy(original)
    assert result == b"hello bytes"
    assert not isinstance(result, AnsibleUnsafe)
    assert len(calls) == 1


def test_unsafeproxy_returns_non_string_unchanged(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    sentinel_int = 42
    result_int = UnsafeProxy(sentinel_int)
    assert result_int is sentinel_int
    assert result_int == 42
    assert not isinstance(result_int, AnsibleUnsafe)

    sentinel_none = None
    result_none = UnsafeProxy(sentinel_none)
    assert result_none is None

    sentinel_list = [1, 2, 3]
    result_list = UnsafeProxy(sentinel_list)
    assert result_list is sentinel_list

    assert len(calls) == 3
