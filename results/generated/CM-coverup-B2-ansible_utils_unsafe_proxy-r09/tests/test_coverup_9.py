# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest

from ansible.module_utils._text import to_text
from ansible.utils.unsafe_proxy import to_unsafe_text, AnsibleUnsafeText


def test_to_unsafe_text_with_text_input():
    result = to_unsafe_text(u"hello")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"hello"
    assert result == to_text(u"hello")


def test_to_unsafe_text_with_bytes_input():
    result = to_unsafe_text(b"hello")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"hello"
    assert result == to_text(b"hello")


def test_to_unsafe_text_with_bytes_and_encoding_kwargs():
    result = to_unsafe_text(b"caf\xc3\xa9", encoding="utf-8")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"café"
    assert result == to_text(b"caf\xc3\xa9", encoding="utf-8")


def test_to_unsafe_text_with_non_string_input():
    result = to_unsafe_text(123)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"123"
    assert result == to_text(123)


def test_to_unsafe_text_with_empty_input():
    result = to_unsafe_text(u"")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u""
    assert result == to_text(u"")
