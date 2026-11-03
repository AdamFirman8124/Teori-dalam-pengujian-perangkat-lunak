# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f016.count_distinct_characters.

The function is pure (no I/O, no global state), so no monkeypatching or
cleanup is required; simply calling it executes line 3 (the return
statement) and all of its sub-branches (set construction and .lower()).
"""

from f016 import count_distinct_characters


def test_count_distinct_characters_all_unique():
    # Every character distinct -> set size equals string length.
    assert count_distinct_characters("abcde") == 5


def test_count_distinct_characters_with_repeats():
    # Repeated characters collapse in the set.
    assert count_distinct_characters("abcdefgabc") == 7


def test_count_distinct_characters_case_insensitive():
    # Mixed case must be folded by .lower() before counting.
    assert count_distinct_characters("abcdeD") == 5
    assert count_distinct_characters("ABCdef") == 6


def test_count_distinct_characters_empty_string():
    # Empty input yields an empty set -> 0 distinct characters.
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1


def test_count_distinct_characters_non_alpha_characters():
    # Digits, punctuation and whitespace are counted as characters too.
    assert count_distinct_characters("aA!1 !") == 4


def test_count_distinct_characters_returns_int():
    result = count_distinct_characters("hello")
    assert isinstance(result, int)
    assert result == 4
