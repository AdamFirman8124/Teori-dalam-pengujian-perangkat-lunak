# file: project/ansible/utils/unsafe_proxy.py:86-102
# asked: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 90, 91, 97, 98, 100, 101, 102], "branches": [[97, 98], [97, 100], [100, 101], [100, 102]]}

import pytest

from ansible.utils.unsafe_proxy import UnsafeProxy, AnsibleUnsafe, AnsibleUnsafeText
from ansible.module_utils.six import binary_type


@pytest.fixture
def mock_display(monkeypatch):
    """Patch Display so the deprecation call is captured and silenced."""
    calls = []

    class FakeDisplay(object):
        def deprecated(self, *args, **kwargs):
            calls.append((args, kwargs))

    import ansible.utils.display
    monkeypatch.setattr(ansible.utils.display, 'Display', FakeDisplay)
    return calls


def test_unsafe_proxy_with_text_string(mock_display):
    """Covers lines 88-91 (deprecation) and 100-102 (string conversion)."""
    result = UnsafeProxy(u'some_string')

    # Deprecation was issued
    assert len(mock_display) == 1
    args, kwargs = mock_display[0]
    assert 'UnsafeProxy is being deprecated' in args[0]
    assert kwargs.get('version') == '2.13'
    assert kwargs.get('collection_name') == 'ansible.builtin'

    # Postcondition: wrapped in AnsibleUnsafeText
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u'some_string'


def test_unsafe_proxy_with_bytes_string(mock_display):
    """Bytes are not string_types on py3, so they pass through unchanged."""
    obj = b'byte_string'

    result = UnsafeProxy(obj)

    assert len(mock_display) == 1
    assert result is obj
    assert isinstance(result, binary_type)
    assert not isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_with_already_unsafe(mock_display):
    """Covers line 97-98: an already-unsafe object is returned as-is."""
    already_unsafe = AnsibleUnsafeText(u'already_unsafe')

    result = UnsafeProxy(already_unsafe)

    # Deprecation still fires (lines 88-91), but no re-wrapping happens
    assert len(mock_display) == 1
    assert result is already_unsafe
    assert isinstance(result, AnsibleUnsafe)


def test_unsafe_proxy_with_non_string(mock_display):
    """Covers line 100 branch-false and line 102: non-string passes through."""
    obj = {'key': 'value'}

    result = UnsafeProxy(obj)

    assert len(mock_display) == 1
    assert result is obj
    assert not isinstance(result, AnsibleUnsafe)
