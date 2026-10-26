# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest

from ansible.module_utils._text import to_bytes
from ansible.utils.unsafe_proxy import (
    AnsibleUnsafe,
    AnsibleUnsafeBytes,
    to_unsafe_bytes,
)


def test_to_unsafe_bytes_from_text():
    result = to_unsafe_bytes(u"café")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, AnsibleUnsafe)
    assert result == to_bytes(u"café")
    assert isinstance(result, bytes)


def test_to_unsafe_bytes_from_bytes():
    result = to_unsafe_bytes(b"raw-bytes")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"raw-bytes"


def test_to_unsafe_bytes_with_kwargs():
    result = to_unsafe_bytes(u"value", encoding="utf-8", errors="strict")
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b"value"


def test_to_unsafe_bytes_nonstring_input():
    result = to_unsafe_bytes(12345)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == to_bytes(12345)
