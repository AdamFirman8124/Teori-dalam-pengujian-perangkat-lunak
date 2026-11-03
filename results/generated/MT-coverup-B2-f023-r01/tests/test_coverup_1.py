# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_returns_length_of_string():
    """Calling strlen executes line 3 (return len(string)) and returns the string length."""
    assert strlen("hello") == 5
    assert strlen("") == 0
    assert strlen("a b c") == 5
    assert strlen("x") == 1
