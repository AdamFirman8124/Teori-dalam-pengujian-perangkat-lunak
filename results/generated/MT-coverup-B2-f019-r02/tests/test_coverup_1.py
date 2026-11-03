# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    """Several words in unsorted order are sorted by their numeric value."""
    result = sort_numbers("three one five")
    assert result == "one three five"
    # Postcondition: output words are exactly the input words, re-ordered.
    assert sorted(result.split(" "), key={"one": 1, "three": 3, "five": 5}.get) == \
        ["one", "three", "five"]


def test_sort_numbers_all_words_reverse():
    """Every key of value_map is exercised (covers the full mapping)."""
    result = sort_numbers("nine eight seven six five four three two one zero")
    assert result == "zero one two three four five six seven eight nine"


def test_sort_numbers_empty_string():
    """Empty input yields empty output (exercises the `if x` filter's false branch)."""
    assert sort_numbers("") == ""


def test_sort_numbers_multiple_spaces():
    """Empty tokens produced by repeated spaces are filtered out."""
    assert sort_numbers("three  one   five") == "one three five"
    assert sort_numbers("  two ") == "two"


def test_sort_numbers_single_word():
    assert sort_numbers("seven") == "seven"


def test_sort_numbers_duplicates_and_stability():
    """Duplicates are kept and equal keys keep their relative order."""
    assert sort_numbers("two one two zero") == "zero one two two"


def test_sort_numbers_already_sorted():
    assert sort_numbers("zero one two") == "zero one two"


def test_sort_numbers_returns_only_single_spaces():
    """Postcondition: output is joined with exactly one space between words."""
    result = sort_numbers("five   one nine")
    assert result == "one five nine"
    assert "  " not in result
