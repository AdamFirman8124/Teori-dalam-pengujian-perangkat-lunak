# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.display import Display
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeText,
    UnsafeProxy,
)


@pytest.fixture
def deprecation_calls(monkeypatch):
    calls = []

    def fake_deprecated(self, message, **kwargs):
        calls.append((message, kwargs))

    monkeypatch.setattr(Display, "deprecated", fake_deprecated)
    return calls


def assert_deprecation_called(calls):
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


def test_unsafe_proxy_returns_existing_unsafe_object(deprecation_calls):
    value = AnsibleUnsafe()

    result = UnsafeProxy(value)

    assert result is value
    assert_deprecation_called(deprecation_calls)


def test_unsafe_proxy_wraps_string_as_unsafe_text(deprecation_calls):
    value = "héllo"

    result = UnsafeProxy(value)

    assert isinstance(result, AnsibleUnsafeText)
    assert result == value
    assert_deprecation_called(deprecation_calls)


def test_unsafe_proxy_returns_non_string_unchanged(deprecation_calls):
    value = object()

    result = UnsafeProxy(value)

    assert result is value
    assert not isinstance(result, AnsibleUnsafe)
    assert_deprecation_called(deprecation_calls)
