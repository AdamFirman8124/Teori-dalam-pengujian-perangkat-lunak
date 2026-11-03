# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_returns_length_of_string():
    """Calling strlen must execute the return statement (line 3)."""
    result = strlen("hello")
    assert result == 5


def test_strlen_empty_string():
    """strlen of an empty string returns 0."""
    assert strlen("") == 0


def test_strlen_unicode_string():
    """strlen counts characters, not bytes."""
    assert strlen("héllo") == 5
