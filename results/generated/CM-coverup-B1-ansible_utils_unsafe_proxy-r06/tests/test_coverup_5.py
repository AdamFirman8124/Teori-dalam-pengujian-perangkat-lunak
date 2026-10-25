# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_ansible_unsafe_text_encode_default():
    unsafe_text = AnsibleUnsafeText("hello")
    result = unsafe_text.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == b"hello"
    assert getattr(result, "__UNSAFE__", False) is True


def test_ansible_unsafe_text_encode_with_encoding_arg():
    unsafe_text = AnsibleUnsafeText("héllo")
    result = unsafe_text.encode("utf-8")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == "héllo".encode("utf-8")
    assert getattr(result, "__UNSAFE__", False) is True


def test_ansible_unsafe_text_encode_with_kwargs():
    unsafe_text = AnsibleUnsafeText("héllo")
    result = unsafe_text.encode(encoding="utf-16", errors="strict")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == "héllo".encode(encoding="utf-16", errors="strict")
    assert result.decode("utf-16") == "héllo"
    assert getattr(result, "__UNSAFE__", False) is True


def test_ansible_unsafe_text_encode_empty():
    unsafe_text = AnsibleUnsafeText("")
    result = unsafe_text.encode("utf-8", "strict")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b""
    assert getattr(result, "__UNSAFE__", False) is True
