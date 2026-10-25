# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.utils.unsafe_proxy import UnsafeProxy
from ansible.utils.display import Display


def _patch_deprecated(monkeypatch):
    calls = []

    def _fake_deprecated(self, msg, *args, **kwargs):
        calls.append({"msg": msg, "args": args, "kwargs": kwargs})

    monkeypatch.setattr(Display, "deprecated", _fake_deprecated)
    return calls


def test_unsafe_proxy_wraps_text_string(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    value = "hello world"
    result = UnsafeProxy(value)
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert str(result) == value
    assert len(calls) == 1
    assert "UnsafeProxy is being deprecated" in calls[0]["msg"]
    assert calls[0]["kwargs"].get("version") == "2.13"
    assert calls[0]["kwargs"].get("collection_name") == "ansible.builtin"


def test_unsafe_proxy_passthrough_ansible_unsafe_text(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    original = AnsibleUnsafeText("already unsafe")
    result = UnsafeProxy(original)
    assert result is original
    assert isinstance(result, AnsibleUnsafeText)
    assert len(calls) == 1


def test_unsafe_proxy_passthrough_ansible_unsafe_bytes(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    original = AnsibleUnsafeBytes(b"already unsafe bytes")
    result = UnsafeProxy(original)
    assert result is original
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert len(calls) == 1


def test_unsafe_proxy_passthrough_non_string(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    for obj in (123, 4.5, None, True, ["a"], {"k": "v"}, (1, 2), object()):
        result = UnsafeProxy(obj)
        assert result is obj
    assert len(calls) == 8


def test_unsafe_proxy_bytes_not_wrapped_as_text(monkeypatch):
    calls = _patch_deprecated(monkeypatch)
    value = b"plain bytes"
    result = UnsafeProxy(value)
    assert result is value
    assert not isinstance(result, AnsibleUnsafe)
    assert len(calls) == 1
