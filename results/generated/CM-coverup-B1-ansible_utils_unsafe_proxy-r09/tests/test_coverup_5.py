# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeText, AnsibleUnsafeBytes


def test_ansible_unsafe_text_encode_default():
    unsafe = AnsibleUnsafeText(u"café")
    result = unsafe.encode()
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b"caf\xc3\xa9"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_explicit_args():
    unsafe = AnsibleUnsafeText(u"hello")
    result = unsafe.encode("utf-8", "strict")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"hello"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_kwargs():
    unsafe = AnsibleUnsafeText(u"hello")
    result = unsafe.encode(encoding="utf-8", errors="replace")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"hello"
    assert result.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_preserves_unsafe_context():
    unsafe = AnsibleUnsafeText(u"data")
    result = unsafe.encode("ascii")
    assert isinstance(result, AnsibleUnsafe)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"data"
