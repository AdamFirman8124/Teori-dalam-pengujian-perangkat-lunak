# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

import ansible.utils.display as display_module
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafeText,
    UnsafeProxy,
)


@pytest.fixture
def mock_display(monkeypatch):
    calls = []

    class FakeDisplay(object):
        def deprecated(self, *args, **kwargs):
            calls.append((args, kwargs))

    monkeypatch.setattr(display_module, 'Display', FakeDisplay)
    return calls


def assert_deprecation_call(calls):
    assert calls == [
        (
            (
                'UnsafeProxy is being deprecated. Use wrap_var or '
                'AnsibleUnsafeBytes/AnsibleUnsafeText directly instead',
            ),
            {
                'version': '2.13',
                'collection_name': 'ansible.builtin',
            },
        )
    ]


def test_unsafe_proxy_wraps_text_string(mock_display):
    value = u'hello'
    result = UnsafeProxy(value)

    assert isinstance(result, AnsibleUnsafeText)
    assert result == value
    assert_deprecation_call(mock_display)


def test_unsafe_proxy_returns_existing_unsafe_value_unchanged(mock_display):
    value = AnsibleUnsafeText(u'already unsafe')
    result = UnsafeProxy(value)

    assert result is value
    assert_deprecation_call(mock_display)


def test_unsafe_proxy_returns_non_string_object_unchanged(mock_display):
    value = {'key': 'value'}
    result = UnsafeProxy(value)

    assert result is value
    assert_deprecation_call(mock_display)


def test_unsafe_proxy_returns_bytes_unchanged_on_python_three(mock_display):
    value = b'bytes-value'
    result = UnsafeProxy(value)

    assert result is value
    assert result == b'bytes-value'
    assert not isinstance(result, AnsibleUnsafeText)
    assert_deprecation_call(mock_display)
