# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    result = sort_numbers("three one five")
    assert result == "one three five"


def test_sort_numbers_all_values():
    result = sort_numbers(
        "nine eight seven six five four three two one zero"
    )
    assert result == "zero one two three four five six seven eight nine"


def test_sort_numbers_single_word():
    assert sort_numbers("four") == "four"


def test_sort_numbers_empty_string():
    # The 'if x' branch filters out empty tokens produced by split(' ')
    assert sort_numbers("") == ""


def test_sort_numbers_extra_spaces():
    # Empty tokens between spaces must be filtered out
    assert sort_numbers("two  zero   one") == "zero one two"


def test_sort_numbers_duplicates():
    assert sort_numbers("one one zero") == "zero one one"


def test_sort_numbers_stability_and_repeated_calls():
    # Verify deterministic output across calls (no state pollution)
    assert sort_numbers("five two") == "two five"
    assert sort_numbers("five two") == "two five"


def test_sort_numbers_invalid_word_raises():
    with pytest.raises(KeyError):
        sort_numbers("ten")
