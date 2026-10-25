# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_basic():
    assert sort_numbers("three one five") == "one three five"


def test_sort_numbers_all_digits():
    assert (
        sort_numbers("nine eight seven six five four three two one zero")
        == "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_single_word():
    assert sort_numbers("four") == "four"


def test_sort_numbers_duplicates():
    assert sort_numbers("two one two") == "one two two"


def test_sort_numbers_empty_string():
    assert sort_numbers("") == ""


def test_sort_numbers_extra_spaces():
    assert sort_numbers("  three   one  ") == "one three"
