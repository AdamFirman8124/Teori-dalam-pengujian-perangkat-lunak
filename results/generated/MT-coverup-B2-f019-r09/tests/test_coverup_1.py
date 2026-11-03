# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    """Sort a simple sequence of number words."""
    assert sort_numbers("three one five") == "one three five"


def test_sort_numbers_all_words():
    """Sort all ten number words given in reverse order."""
    assert (
        sort_numbers("nine eight seven six five four three two one zero")
        == "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_single_word():
    """A single word is returned unchanged."""
    assert sort_numbers("five") == "five"


def test_sort_numbers_already_sorted():
    """Already sorted input stays sorted."""
    assert sort_numbers("one two three") == "one two three"


def test_sort_numbers_duplicates():
    """Duplicate words are preserved and sorted."""
    assert sort_numbers("two two one") == "one two two"


def test_sort_numbers_empty_string():
    """Empty string yields empty string (exercises the `if x` filter with a falsy item)."""
    assert sort_numbers("") == ""


def test_sort_numbers_extra_spaces():
    """Consecutive spaces produce empty tokens that are filtered out (falsy branch of `if x`)."""
    assert sort_numbers("three  one") == "one three"


def test_sort_numbers_leading_trailing_spaces():
    """Leading/trailing spaces are filtered out as empty tokens."""
    assert sort_numbers(" two ") == "two"
