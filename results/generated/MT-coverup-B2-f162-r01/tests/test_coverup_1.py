# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f162 import string_to_md5


def test_string_to_md5_nonempty_text():
    """Covers the truthy branch of the conditional on line 4 (and the import on line 3)."""
    result = string_to_md5("Hello world")
    assert result == "3e25960a79dbc69b674cd4ec67a72c62"
    # Postcondition: result is a 32-character lowercase hex digest
    assert isinstance(result, str)
    assert len(result) == 32
    assert all(c in "0123456789abcdef" for c in result)


def test_string_to_md5_empty_text_returns_none():
    """Covers the falsy branch of the conditional on line 4 (and the import on line 3)."""
    assert string_to_md5("") is None


def test_string_to_md5_matches_hashlib():
    """Cross-check the truthy branch against hashlib directly."""
    import hashlib

    text = "test input"
    expected = hashlib.md5(text.encode("ascii")).hexdigest()
    assert string_to_md5(text) == expected
