# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest

from ansible.module_utils._text import to_bytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, to_unsafe_bytes


def test_to_unsafe_bytes_from_text():
    result = to_unsafe_bytes(u'trusted')
    # line 142 executed: wrap_var(to_bytes(...)) returned
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b'trusted'


def test_to_unsafe_bytes_from_bytes():
    result = to_unsafe_bytes(b'raw\x00bytes')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'raw\x00bytes'


def test_to_unsafe_bytes_passes_through_kwargs():
    result = to_unsafe_bytes(u'caf\u00e9', encoding='utf-8', errors='strict')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == u'caf\u00e9'.encode('utf-8')


def test_to_unsafe_bytes_wraps_result_of_to_bytes(monkeypatch):
    # Verify the function delegates to to_bytes and wraps its output
    sentinel = b'sentinel'
    called = {}

    def fake_to_bytes(*args, **kwargs):
        called['args'] = args
        called['kwargs'] = kwargs
        return sentinel

    monkeypatch.setattr(
        'ansible.utils.unsafe_proxy.to_bytes', fake_to_bytes
    )
    result = to_unsafe_bytes(u'x', encoding='utf-8')
    assert called['args'] == (u'x',)
    assert called['kwargs'] == {'encoding': 'utf-8'}
    # wrap_var wraps the to_bytes result in an unsafe bytes type
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == sentinel
