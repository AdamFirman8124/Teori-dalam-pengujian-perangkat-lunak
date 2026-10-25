# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafeText, AnsibleUnsafeBytes, AnsibleUnsafe


def test_ansible_unsafe_text_encode_default():
    """AnsibleUnsafeText.encode() must return an AnsibleUnsafeBytes instance (line 79)."""
    unsafe = AnsibleUnsafeText(u"café")
    result = unsafe.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"caf\xc3\xa9"
    # underlying bytes content must match a normal str encode
    assert bytes(result) == u"café".encode()


def test_ansible_unsafe_text_encode_with_args_kwargs():
    """encode() must forward args/kwargs to str.encode and stay unsafe."""
    unsafe = AnsibleUnsafeText(u"café")
    result = unsafe.encode("latin-1", "strict")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"caf\xe9"

    # kwargs path
    result_kw = unsafe.encode(encoding="utf-8", errors="replace")
    assert isinstance(result_kw, AnsibleUnsafeBytes)
    assert result_kw == b"caf\xc3\xa9"
