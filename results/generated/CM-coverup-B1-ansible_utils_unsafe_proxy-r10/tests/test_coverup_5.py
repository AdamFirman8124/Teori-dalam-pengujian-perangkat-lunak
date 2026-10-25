# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeText


def test_ansible_unsafe_text_encode_returns_unsafe_bytes():
    value = AnsibleUnsafeText("hello")
    encoded = value.encode()

    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == b"hello"
    assert encoded.__UNSAFE__ is True


def test_ansible_unsafe_text_encode_forwards_encoding_arguments():
    value = AnsibleUnsafeText("café")
    encoded = value.encode("utf-8", errors="strict")

    assert type(encoded) is AnsibleUnsafeBytes
    assert encoded == "café".encode("utf-8", errors="strict")
    assert encoded.decode("utf-8") == "café"
    assert encoded.__UNSAFE__ is True
