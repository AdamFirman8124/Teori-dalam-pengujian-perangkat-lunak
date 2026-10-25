# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

from ansible.utils import unsafe_proxy
from ansible.utils.display import Display


def test_unsafe_proxy_returns_existing_unsafe_object(monkeypatch):
    calls = []

    def deprecated(self, message, **kwargs):
        calls.append((message, kwargs))

    monkeypatch.setattr(Display, "deprecated", deprecated)
    value = unsafe_proxy.AnsibleUnsafeText("already unsafe")

    result = unsafe_proxy.UnsafeProxy(value)

    assert result is value
    assert calls == [
        (
            "UnsafeProxy is being deprecated. Use wrap_var or "
            "AnsibleUnsafeBytes/AnsibleUnsafeText directly instead",
            {"version": "2.13", "collection_name": "ansible.builtin"},
        )
    ]


def test_unsafe_proxy_wraps_string_as_unsafe_text(monkeypatch):
    calls = []

    def deprecated(self, message, **kwargs):
        calls.append((message, kwargs))

    monkeypatch.setattr(Display, "deprecated", deprecated)

    result = unsafe_proxy.UnsafeProxy("plain text")

    assert type(result) is unsafe_proxy.AnsibleUnsafeText
    assert result == "plain text"
    assert result.__UNSAFE__ is True
    assert calls == [
        (
            "UnsafeProxy is being deprecated. Use wrap_var or "
            "AnsibleUnsafeBytes/AnsibleUnsafeText directly instead",
            {"version": "2.13", "collection_name": "ansible.builtin"},
        )
    ]


def test_unsafe_proxy_returns_non_string_unchanged(monkeypatch):
    calls = []

    def deprecated(self, message, **kwargs):
        calls.append((message, kwargs))

    monkeypatch.setattr(Display, "deprecated", deprecated)
    value = object()

    result = unsafe_proxy.UnsafeProxy(value)

    assert result is value
    assert calls == [
        (
            "UnsafeProxy is being deprecated. Use wrap_var or "
            "AnsibleUnsafeBytes/AnsibleUnsafeText directly instead",
            {"version": "2.13", "collection_name": "ansible.builtin"},
        )
    ]
