# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    """Sorting a few number words returns them in ascending numeric order."""
    result = sort_numbers("three one five")
    assert result == "one three five"


def test_sort_numbers_all_words():
    """All ten number words are sorted correctly."""
    result = sort_numbers(
        "nine eight seven six five four three two one zero"
    )
    assert result == "zero one two three four five six seven eight nine"


def test_sort_numbers_single_word():
    """A single number word is returned unchanged."""
    assert sort_numbers("four") == "four"


def test_sort_numbers_empty_string():
    """An empty string yields an empty result (exercises the `if x` filter)."""
    assert sort_numbers("") == ""


def test_sort_numbers_extra_spaces():
    """Extra spaces are filtered out by the `if x` branch."""
    assert sort_numbers("  two   zero  ") == "zero two"


def test_sort_numbers_already_sorted():
    """An already-sorted input is returned unchanged."""
    assert sort_numbers("zero one two") == "zero one two"


def test_sort_numbers_duplicates():
    """Duplicate words are preserved and sorted."""
    assert sort_numbers("three one three") == "one three three"


def test_sort_numbers_unknown_word_raises_keyerror():
    """A word not in the value_map causes a KeyError from the sort key."""
    with pytest.raises(KeyError):
        sort_numbers("ten one")
