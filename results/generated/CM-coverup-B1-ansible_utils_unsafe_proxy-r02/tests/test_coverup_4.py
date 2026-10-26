# file: project/ansible/utils/unsafe_proxy.py:70-73
# asked: {"lines": [73], "branches": []}
# gained: {"lines": [73], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_bytes_decode_returns_unsafe_text():
    unsafe_bytes = AnsibleUnsafeBytes(b"secret value")
    assert isinstance(unsafe_bytes, AnsibleUnsafe)

    result = unsafe_bytes.decode()

    # Line 73: decode must return an AnsibleUnsafeText preserving unsafe context
    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"secret value"


def test_ansible_unsafe_bytes_decode_with_args_and_kwargs():
    unsafe_bytes = AnsibleUnsafeBytes(b"caf\xc3\xa9")

    result = unsafe_bytes.decode("utf-8", errors="strict")

    assert isinstance(result, AnsibleUnsafeText)
    assert isinstance(result, AnsibleUnsafe)
    assert result == u"caf\xe9"
