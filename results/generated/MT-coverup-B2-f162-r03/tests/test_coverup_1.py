# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib

from f162 import string_to_md5


def test_string_to_md5_non_empty_text():
    """Covers lines 3-4 (import + truthy branch): a real digest is returned."""
    result = string_to_md5("hello")
    expected = hashlib.md5(b"hello").hexdigest()
    assert result == expected
    assert result == "5d41402abc4b2a76b9719d911017c592"
    # Sanity check: result is a 32-char lowercase hex string
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)


def test_string_to_md5_empty_text():
    """Covers the falsy branch of line 4: empty string yields None."""
    assert string_to_md5("") is None


def test_string_to_md5_none_text():
    """Covers the falsy branch of line 4 with None input (encode never called)."""
    assert string_to_md5(None) is None
