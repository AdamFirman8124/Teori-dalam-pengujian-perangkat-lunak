# file: project/ansible/utils/unsafe_proxy.py:141-142
# asked: {"lines": [142], "branches": []}
# gained: {"lines": [142], "branches": []}

import pytest

from ansible.module_utils._text import to_bytes
from ansible.utils.unsafe_proxy import AnsibleUnsafeBytes, to_unsafe_bytes


def test_to_unsafe_bytes_from_text():
    result = to_unsafe_bytes(u'text value')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert isinstance(result, bytes)
    assert result == b'text value'


def test_to_unsafe_bytes_from_bytes():
    result = to_unsafe_bytes(b'byte value')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'byte value'


def test_to_unsafe_bytes_with_kwargs():
    result = to_unsafe_bytes(u'caf\u00e9', encoding='utf-8', errors='strict')
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == to_bytes(u'caf\u00e9', encoding='utf-8', errors='strict')


def test_to_unsafe_bytes_non_string_input():
    result = to_unsafe_bytes(12345)
    assert isinstance(result, AnsibleUnsafeBytes)
    assert result == b'12345'
