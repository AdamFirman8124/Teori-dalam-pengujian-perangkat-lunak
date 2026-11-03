# file: project/f101/__init__.py:1-15
# asked: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10, 12, 14, 15], "branches": [[3, 4], [3, 6], [8, 9], [8, 14], [9, 10], [9, 12]]}

import pytest

from f101 import words_string


def test_empty_string_returns_empty_list():
    """Covers lines 3-4: the `if not s` branch returning []."""
    assert words_string("") == []


def test_string_with_commas():
    """Covers lines 6, 8-10, 14-15: comma branch replaces ',' with ' '."""
    assert words_string("One, two, three, four, five, six") == [
        "One",
        "two",
        "three",
        "four",
        "five",
        "six",
    ]


def test_string_without_commas():
    """Covers lines 8-9, 12, 14-15: else branch appends letters unchanged."""
    assert words_string("Hi my name is John") == ["Hi", "my", "name", "is", "John"]


def test_mixed_commas_and_spaces():
    """Covers both branches (lines 10 and 12) in a single call."""
    assert words_string("Hi,my,name,is,John") == ["Hi", "my", "name", "is", "John"]


def test_returns_list_type():
    """Verifies the postcondition that the result is always a list."""
    assert isinstance(words_string(""), list)
    assert isinstance(words_string("a,b"), list)
