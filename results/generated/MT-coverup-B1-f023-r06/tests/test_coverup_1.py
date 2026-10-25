# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


def test_strlen_empty_string():
    assert strlen("") == 0


def test_strlen_non_empty_string():
    assert strlen("hello") == 5


def test_strlen_unicode_and_whitespace():
    assert strlen("héllo wörld") == 11
    assert strlen(" ") == 1


def test_strlen_returns_int_type():
    result = strlen("abc")
    assert isinstance(result, int)
    assert result == 3
