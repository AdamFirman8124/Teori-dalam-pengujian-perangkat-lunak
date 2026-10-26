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


@pytest.fixture
def deprecated_calls(monkeypatch):
    """Capture Display.deprecated calls instead of emitting real warnings."""
    calls = []

    def fake_deprecated(self, msg, version=None, removed=False, date=None, collection_name=None):
        calls.append(
            {
                'msg': msg,
                'version': version,
                'removed': removed,
                'date': date,
                'collection_name': collection_name,
            }
        )

    monkeypatch.setattr(Display, 'deprecated', fake_deprecated)
    return calls


def test_unsafe_proxy_wraps_plain_text(deprecated_calls):
    obj = 'unsafe me'

    result = UnsafeProxy(obj)

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == obj
    assert result is not obj
    assert result.__UNSAFE__ is True

    assert len(deprecated_calls) == 1
    call = deprecated_calls[0]
    assert 'UnsafeProxy is being deprecated' in call['msg']
    assert 'wrap_var' in call['msg']
    assert call['version'] == '2.13'
    assert call['collection_name'] == 'ansible.builtin'
    assert call['removed'] is False


def test_unsafe_proxy_returns_existing_unsafe_text_unchanged(deprecated_calls):
    obj = AnsibleUnsafeText('already unsafe')

    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafeText)
    assert result == 'already unsafe'
    assert len(deprecated_calls) == 1


def test_unsafe_proxy_returns_existing_unsafe_bytes_unchanged(deprecated_calls):
    obj = AnsibleUnsafeBytes(b'already unsafe')

    result = UnsafeProxy(obj)

    assert result is obj
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'already unsafe'
    assert len(deprecated_calls) == 1


def test_unsafe_proxy_passes_through_non_string_unchanged(deprecated_calls):
    obj = 42

    result = UnsafeProxy(obj)

    assert result is obj
    assert result == 42
    assert not isinstance(result, AnsibleUnsafe)
    assert len(deprecated_calls) == 1
