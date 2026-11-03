# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib

from f162 import string_to_md5


def test_string_to_md5_nonempty_text_hashes():
    """A non-empty string must execute the import (line 3) and the hashing
    branch of the conditional expression (line 4), returning the ASCII-md5
    hex digest of the text."""
    result = string_to_md5("hello")
    assert result == hashlib.md5(b"hello").hexdigest()
    assert result == "5d41402abc4b2a76b9719d911017c592"
    assert isinstance(result, str)
    assert len(result) == 32


def test_string_to_md5_empty_string_returns_none():
    """An empty string is falsy, exercising the other branch of the
    conditional expression on line 4 (and still executing line 3)."""
    assert string_to_md5("") is None


def test_string_to_md5_none_returns_none():
    """None is also falsy, covering the falsy branch again."""
    assert string_to_md5(None) is None
