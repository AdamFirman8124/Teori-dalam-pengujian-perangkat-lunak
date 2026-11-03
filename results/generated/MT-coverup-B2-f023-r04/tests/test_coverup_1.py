# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_returns_length_of_string():
    """Calling strlen executes line 3 and returns the string's length."""
    result = strlen("hello")
    assert result == 5
    assert isinstance(result, int)


def test_strlen_empty_string():
    """strlen of an empty string returns 0, still exercising line 3."""
    assert strlen("") == 0


def test_strlen_unicode_string():
    """strlen counts characters (code points), not bytes."""
    assert strlen("héllo") == 5


def test_strlen_with_spaces():
    """Whitespace characters are counted too."""
    assert strlen("a b c") == 5
