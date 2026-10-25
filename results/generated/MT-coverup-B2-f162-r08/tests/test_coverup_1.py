# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib
from f162 import string_to_md5


def test_string_to_md5_with_text():
    text = "hello"
    expected = hashlib.md5(text.encode('ascii')).hexdigest()
    result = string_to_md5(text)
    assert result == expected
    assert result == "5d41402abc4b2a76b9719d911017c592"


def test_string_to_md5_empty_string_returns_none():
    assert string_to_md5("") is None


def test_string_to_md5_none_returns_none():
    assert string_to_md5(None) is None
