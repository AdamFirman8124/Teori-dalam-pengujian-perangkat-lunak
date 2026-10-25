# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    to_unsafe_bytes,
    wrap_var,
)


def test_to_unsafe_bytes_from_text():
    result = to_unsafe_bytes("hello")
    assert result == b"hello"
    assert isinstance(result, bytes)
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeBytes)


def test_to_unsafe_bytes_from_bytes():
    result = to_unsafe_bytes(b"hello")
    assert result == b"hello"
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeBytes)


def test_to_unsafe_bytes_with_encoding_kwarg():
    result = to_unsafe_bytes("héllo", encoding="utf-8")
    assert result == "héllo".encode("utf-8")
    assert isinstance(result, AnsibleUnsafeBytes)


def test_to_unsafe_bytes_with_errors_kwarg():
    result = to_unsafe_bytes("hello", encoding="ascii", errors="strict")
    assert result == b"hello"
    assert isinstance(result, AnsibleUnsafeBytes)


def test_to_unsafe_bytes_forwards_args_and_kwargs(monkeypatch):
    import ansible.utils.unsafe_proxy as proxy_module

    captured = {}

    def fake_to_bytes(*args, **kwargs):
        captured["args"] = args
        captured["kwargs"] = kwargs
        return b"fake-bytes"

    monkeypatch.setattr(proxy_module, "to_bytes", fake_to_bytes)

    result = to_unsafe_bytes("orig", encoding="utf-8", errors="surrogate_or_strict")

    assert captured["args"] == ("orig",)
    assert captured["kwargs"] == {"encoding": "utf-8", "errors": "surrogate_or_strict"}
    assert result == b"fake-bytes"
    assert isinstance(result, AnsibleUnsafeBytes)


def test_to_unsafe_bytes_applies_wrap_var(monkeypatch):
    import ansible.utils.unsafe_proxy as proxy_module
    from ansible.module_utils._text import to_bytes as real_to_bytes

    called = {}

    orig_wrap_var = proxy_module.wrap_var

    def fake_wrap_var(v):
        called["value"] = v
        return orig_wrap_var(v)

    monkeypatch.setattr(proxy_module, "wrap_var", fake_wrap_var)

    result = to_unsafe_bytes("hello")

    assert called["value"] == real_to_bytes("hello")
    assert result == b"hello"
    assert isinstance(result, AnsibleUnsafe)
