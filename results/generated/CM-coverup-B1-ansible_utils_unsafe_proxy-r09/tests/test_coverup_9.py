# file: project/ansible/utils/unsafe_proxy.py:145-146
# asked: {"lines": [146], "branches": []}
# gained: {"lines": [146], "branches": []}

import pytest

from ansible.module_utils._text import to_text
from ansible.utils.unsafe_proxy import AnsibleUnsafeText, to_unsafe_text


def test_to_unsafe_text_with_text():
    result = to_unsafe_text(u"some text")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"some text"
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_with_bytes():
    result = to_unsafe_text(b"some bytes")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"some bytes"
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_with_non_string():
    result = to_unsafe_text(123)
    assert isinstance(result, AnsibleUnsafeText)
    assert result == u"123"
    assert getattr(result, "__UNSAFE__", False) is True


def test_to_unsafe_text_with_kwargs():
    result = to_unsafe_text(b"\xff\xfe", errors="surrogateescape")
    assert isinstance(result, AnsibleUnsafeText)
    assert result == to_text(b"\xff\xfe", errors="surrogateescape")
    assert getattr(result, "__UNSAFE__", False) is True
