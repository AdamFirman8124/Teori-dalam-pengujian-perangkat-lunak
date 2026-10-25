# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    result = sort_numbers("three one two")
    assert result == "one two three"


def test_sort_numbers_all_words():
    result = sort_numbers("nine eight seven six five four three two one zero")
    assert result == "zero one two three four five six seven eight nine"


def test_sort_numbers_single_word():
    result = sort_numbers("five")
    assert result == "five"


def test_sort_numbers_duplicates():
    result = sort_numbers("two zero two")
    assert result == "zero two two"


def test_sort_numbers_empty_string():
    result = sort_numbers("")
    assert result == ""


def test_sort_numbers_extra_spaces():
    result = sort_numbers("  four   one  ")
    assert result == "one four"
