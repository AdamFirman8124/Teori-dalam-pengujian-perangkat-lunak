# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    to_unsafe_bytes,
)


def test_to_unsafe_bytes_from_text():
    result = to_unsafe_bytes(u'hello')
    assert result == b'hello'
    assert isinstance(result, bytes)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)


def test_to_unsafe_bytes_from_bytes():
    result = to_unsafe_bytes(b'hello')
    assert result == b'hello'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)


def test_to_unsafe_bytes_with_encoding_kwarg():
    result = to_unsafe_bytes(u'caf\xe9', encoding='utf-8')
    assert result == u'caf\xe9'.encode('utf-8')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)


def test_to_unsafe_bytes_with_nonstring_kwarg():
    result = to_unsafe_bytes(123, nonstring='simplerepr')
    assert result == b'123'
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
