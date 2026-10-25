# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

from f019 import sort_numbers


def test_sort_numbers_basic():
    assert sort_numbers("three one two") == "one two three"
    assert sort_numbers("zero") == "zero"
    assert sort_numbers("two one") == "one two"


def test_sort_numbers_all_words():
    assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
    assert sort_numbers("five zero nine three one eight four seven six two") == "zero one two three four five six seven eight nine"


def test_sort_numbers_empty_and_blank():
    assert sort_numbers("") == ""
    assert sort_numbers("   ") == ""


def test_sort_numbers_filters_empty_strings():
    # double / triple spaces produce empty strings that must be filtered by `if x`
    assert sort_numbers("two  one") == "one two"
    assert sort_numbers("three   one two") == "one two three"
    assert sort_numbers(" one ") == "one"
