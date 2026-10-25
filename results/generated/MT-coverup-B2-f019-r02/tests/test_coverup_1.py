# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

import pytest

from f019 import sort_numbers


def test_sort_numbers_sorts_ascending():
    assert sort_numbers("three one two") == "one two three"


def test_sort_numbers_single_value():
    assert sort_numbers("nine") == "nine"


def test_sort_numbers_already_sorted():
    assert sort_numbers("zero one two three four five six seven eight nine") == (
        "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_reverse_order():
    assert sort_numbers("nine eight seven six five four three two one zero") == (
        "zero one two three four five six seven eight nine"
    )


def test_sort_numbers_ignores_empty_tokens():
    assert sort_numbers("  two   one ") == "one two"
    assert sort_numbers("") == ""


def test_sort_numbers_duplicates_preserved():
    assert sort_numbers("five five zero") == "zero five five"


def test_sort_numbers_unknown_word_raises_key_error():
    with pytest.raises(KeyError):
        sort_numbers("one banana")


def test_sort_numbers_does_not_mutate_input():
    numbers = "two one"
    result = sort_numbers(numbers)
    assert numbers == "two one"
    assert result == "one two"
