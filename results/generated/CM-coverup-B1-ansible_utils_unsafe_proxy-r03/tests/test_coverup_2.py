# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.display import Display
from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, UnsafeProxy


def _patch_deprecated(monkeypatch):
    calls = []

    def _fake_deprecated(self, *args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr(Display, "deprecated", _fake_deprecated)
    return calls


def test_unsafe_proxy_wraps_text_string(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    value = "hello world"
    result = UnsafeProxy(value)
    assert len(calls) == 1
    args, kwargs = calls[0]
    assert "UnsafeProxy is being deprecated" in args[0]
    assert kwargs.get("version") == "2.13"
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert str(result) == value
    assert result == value


def test_unsafe_proxy_returns_ansible_unsafe_as_is(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    unsafe = AnsibleUnsafeText("already unsafe")
    result = UnsafeProxy(unsafe)
    assert len(calls) == 1
    assert result is unsafe
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_returns_plain_ansible_unsafe_as_is(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    unsafe = AnsibleUnsafe()
    result = UnsafeProxy(unsafe)
    assert len(calls) == 1
    assert result is unsafe
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_returns_non_string_unchanged(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    for obj in (123, 4.5, None, ["a"], {"k": "v"}, ("t",), object()):
        calls.clear()
        result = UnsafeProxy(obj)
        assert len(calls) == 1
        assert result is obj
