# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_returns_length_of_string():
    """Calling strlen executes line 3 (the return statement) and returns the
    correct length for a non-empty string."""
    assert strlen("hello") == 5


def test_strlen_empty_string():
    """strlen returns 0 for the empty string, also exercising line 3."""
    assert strlen("") == 0


def test_strlen_unicode_string():
    """strlen counts characters (not bytes) for unicode strings."""
    assert strlen("héllo") == 5
