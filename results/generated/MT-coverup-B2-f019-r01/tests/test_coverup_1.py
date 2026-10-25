# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

from f019 import sort_numbers


def test_sort_numbers_basic_ordering():
    assert sort_numbers("three one five") == "one three five"
    assert sort_numbers("nine zero one") == "zero one nine"
    assert sort_numbers("two") == "two"


def test_sort_numbers_all_values():
    assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
    assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"


def test_sort_numbers_empty_and_extra_spaces():
    # empty input filters everything out
    assert sort_numbers("") == ""
    # multiple / leading / trailing spaces produce empty strings that are filtered by `if x`
    assert sort_numbers("two  one   three") == "one two three"
    assert sort_numbers("  ") == ""
    assert sort_numbers(" one ") == "one"


def test_sort_numbers_duplicates_and_stability():
    assert sort_numbers("one one zero") == "zero one one"
    assert sort_numbers("five three five one") == "one three five five"
