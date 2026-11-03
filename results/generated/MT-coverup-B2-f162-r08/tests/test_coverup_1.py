# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib

import pytest

from f162 import string_to_md5


def test_string_to_md5_nonempty_string():
    """Covers lines 3-4: import hashlib and the truthy branch of the return."""
    result = string_to_md5("hello")
    assert result == hashlib.md5(b"hello").hexdigest()
    assert result == "5d41402abc4b2a76b9719d911017c592"
    # Result must be a 32-character lowercase hex digest.
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)


def test_string_to_md5_empty_string():
    """Covers the falsy branch of line 4: empty text returns None."""
    assert string_to_md5("") is None


def test_string_to_md5_matches_hashlib_reference():
    """Cross-check against hashlib directly for another non-empty input."""
    text = "pytest coverage"
    expected = hashlib.md5(text.encode("ascii")).hexdigest()
    assert string_to_md5(text) == expected
