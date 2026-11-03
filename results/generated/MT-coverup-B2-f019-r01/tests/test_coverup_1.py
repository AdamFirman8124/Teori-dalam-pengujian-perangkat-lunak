# file: project/f019/__init__.py:4-18
# asked: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}
# gained: {"lines": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": []}

"""Tests for f019.sort_numbers.

The function under test is pure (no I/O, no global state, no monkeypatching
required), so no cleanup is necessary; each test is self-contained and leaves
no state behind.
"""

from f019 import sort_numbers


def test_sort_numbers_basic_reorders_tokens():
    # Executes the value_map construction (lines 6-17) and the return
    # statement (line 18) with non-empty tokens (truthy branch of `if x`).
    assert sort_numbers("three one five") == "one three five"


def test_sort_numbers_all_values_in_reverse():
    result = sort_numbers("nine eight seven six five four three two one zero")
    assert result == "zero one two three four five six seven eight nine"
    # Postcondition: output tokens are in nondecreasing numeric order.
    order = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    values = [order.index(tok) for tok in result.split(" ")]
    assert values == sorted(values)


def test_sort_numbers_filters_empty_tokens_from_extra_spaces():
    # Consecutive/leading/trailing spaces yield empty strings, exercising the
    # falsy branch of `if x` in the list comprehension.
    assert sort_numbers("three  one") == "one three"
    assert sort_numbers(" two ") == "two"
    assert sort_numbers("   ") == ""


def test_sort_numbers_empty_input_returns_empty_string():
    assert sort_numbers("") == ""


def test_sort_numbers_single_token():
    assert sort_numbers("seven") == "seven"


def test_sort_numbers_stable_with_duplicates():
    # sorted() is stable, so equal keys keep their relative input order.
    assert sort_numbers("one one zero") == "zero one one"


def test_sort_numbers_does_not_mutate_or_leak_state():
    original = "five zero five"
    result = sort_numbers(original)
    assert original == "five zero five"  # input string untouched (immutable)
    assert result == "zero five five"
