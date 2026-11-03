# file: project/f162/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import hashlib

from f162 import string_to_md5


def test_string_to_md5_nonempty_text():
    """Covers line 3 (import hashlib) and the truthy branch of line 4."""
    result = string_to_md5("hello world")
    assert result == hashlib.md5(b"hello world").hexdigest()
    assert result == "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert isinstance(result, str)
    assert len(result) == 32


def test_string_to_md5_empty_text():
    """Covers line 3 (import hashlib) and the falsy branch of line 4."""
    result = string_to_md5("")
    assert result is None
