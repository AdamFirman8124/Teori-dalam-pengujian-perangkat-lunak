# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    """Covers value_map construction and sorting of a simple input."""
    assert sort_numbers("three one five") == "one three five"


def test_sort_numbers_all_words():
    """Covers every entry of value_map being used as a sort key."""
    assert (
        sort_numbers("nine eight seven six five four three two one zero")
        == "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_single_word():
    assert sort_numbers("five") == "five"


def test_sort_numbers_already_sorted():
    assert sort_numbers("zero one two") == "zero one two"


def test_sort_numbers_reverse_sorted():
    assert sort_numbers("nine eight seven") == "seven eight nine"


def test_sort_numbers_duplicates():
    assert sort_numbers("two one two") == "one two two"


def test_sort_numbers_empty_string():
    """Empty string: split yields [''], the `if x` filter drops it, join gives ''."""
    assert sort_numbers("") == ""


def test_sort_numbers_multiple_spaces():
    """Exercises the falsy branch of the `if x` filter (empty tokens removed)."""
    assert sort_numbers("three  one") == "one three"
    assert sort_numbers("  four   two  ") == "two four"
