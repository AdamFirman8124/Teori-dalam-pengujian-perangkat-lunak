# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    """Unsorted words are sorted by their numeric value."""
    assert sort_numbers("three one two") == "one two three"


def test_sort_numbers_all_words_reverse():
    """All ten number words, given in reverse order, come back sorted zero..nine."""
    words = ["nine", "eight", "seven", "six", "five",
             "four", "three", "two", "one", "zero"]
    assert sort_numbers(" ".join(words)) == \
        "zero one two three four five six seven eight nine"


def test_sort_numbers_single_word():
    """A single word input passes through (covers the value_map lookup and lambda key)."""
    assert sort_numbers("five") == "five"


def test_sort_numbers_empty_string():
    """An empty string yields an empty string; exercises the `if x` false branch."""
    assert sort_numbers("") == ""


def test_sort_numbers_multiple_spaces():
    """Extra internal spaces are filtered out by the `if x` guard."""
    assert sort_numbers("three  one") == "one three"


def test_sort_numbers_leading_trailing_spaces():
    """Leading/trailing spaces produce empty tokens that are filtered out."""
    assert sort_numbers(" four one ") == "one four"


def test_sort_numbers_already_sorted():
    """Already sorted input is unchanged."""
    assert sort_numbers("zero one two") == "zero one two"


def test_sort_numbers_duplicates():
    """Duplicate words are preserved and sorted."""
    assert sort_numbers("two zero two") == "zero two two"


def test_sort_numbers_heavier_shuffle():
    """A larger shuffled input sorts correctly, exercising the sort key lambda repeatedly."""
    result = sort_numbers("eight zero five nine two six one four seven three")
    assert result == "zero one two three four five six seven eight nine"
