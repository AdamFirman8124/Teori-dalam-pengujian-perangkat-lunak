# file: project/ansible/utils/unsafe_proxy.py:76-79
# asked: {"lines": [79], "branches": []}
# gained: {"lines": [79], "branches": []}

import pytest

from ansible.utils.unsafe_proxy import AnsibleUnsafe, AnsibleUnsafeBytes, AnsibleUnsafeText


def test_encode_returns_unsafe_bytes():
    unsafe_text = AnsibleUnsafeText(u"hello")
    result = unsafe_text.encode()

    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b"hello"
    assert result.__UNSAFE__ is True


def test_encode_with_args_and_kwargs():
    unsafe_text = AnsibleUnsafeText(u"h\u00e9llo")
    result = unsafe_text.encode("ascii", errors="replace")

    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"h?llo"
    assert result.__UNSAFE__ is True


def test_unsafe_hierarchy():
    assert issubclass(AnsibleUnsafeText, AnsibleUnsafe)
    assert issubclass(AnsibleUnsafeBytes, AnsibleUnsafe)
    assert AnsibleUnsafeText(u"x").__UNSAFE__ is True
