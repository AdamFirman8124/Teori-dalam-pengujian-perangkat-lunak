# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import ansible.utils.display
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeText,
    UnsafeProxy,
)


def _patch_display(monkeypatch):
    calls = []

    class FakeDisplay:
        def deprecated(self, message, **kwargs):
            calls.append((message, kwargs))

    monkeypatch.setattr(ansible.utils.display, "Display", FakeDisplay)
    return calls


def _assert_deprecation_call(calls):
    assert calls == [
        (
            "UnsafeProxy is being deprecated. Use wrap_var or "
            "AnsibleUnsafeBytes/AnsibleUnsafeText directly instead",
            {
                "version": "2.13",
                "collection_name": "ansible.builtin",
            },
        )
    ]


def test_unsafe_proxy_wraps_text(monkeypatch):
    calls = _patch_display(monkeypatch)

    result = UnsafeProxy("value")

    assert type(result) is AnsibleUnsafeText
    assert result == "value"
    assert result.__UNSAFE__ is True
    _assert_deprecation_call(calls)


def test_unsafe_proxy_returns_existing_unsafe_value(monkeypatch):
    calls = _patch_display(monkeypatch)
    unsafe_value = AnsibleUnsafeText("already unsafe")

    result = UnsafeProxy(unsafe_value)

    assert result is unsafe_value
    _assert_deprecation_call(calls)


def test_unsafe_proxy_returns_non_string_unchanged(monkeypatch):
    calls = _patch_display(monkeypatch)
    value = object()

    result = UnsafeProxy(value)

    assert result is value
    _assert_deprecation_call(calls)
