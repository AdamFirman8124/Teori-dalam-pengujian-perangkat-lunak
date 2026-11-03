# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f016.count_distinct_characters.

These tests ensure every line/branch of the function executes, including
the single statement on line 3 (``return len(set(string.lower()))``).
The function under test is pure (no I/O, globals, or mutable state), so
no monkeypatching or teardown is required to avoid state pollution.
"""

import pytest

from f016 import count_distinct_characters


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("", 0),                      # empty string -> empty set
        ("a", 1),                     # single character
        ("aaaa", 1),                  # duplicates collapse via set()
        ("abcde", 5),                 # all unique
        ("abcdeEDCBA", 5),            # mixed case collapses via .lower()
        ("xyXyYzZ", 3),               # case-insensitive counting
        ("Hello, World!", 10),        # letters, punctuation, spaces
        ("12321", 3),                 # digits
        (" \t\n ", 3),                # whitespace variants
    ],
)
def test_count_distinct_characters(string, expected):
    """Calling the function executes line 3 and returns the correct count."""
    result = count_distinct_characters(string)

    # Postconditions
    assert isinstance(result, int)
    assert result == expected
    # Never more distinct characters than total characters.
    assert result <= len(string)
    # Matches an independent reference computation.
    assert result == len({ch.lower() for ch in string})
    # Monotonic sanity: adding characters cannot decrease the count.
    if string:
        assert count_distinct_characters(string + "\x00") in (result, result + 1)


def test_case_insensitivity_exercises_lower_branch():
    """Mixed-case inputs guarantee ``str.lower()`` transforms the data
    before ``set()`` deduplicates it."""
    assert count_distinct_characters("AaBbCc") == 3
    assert count_distinct_characters("ZZzz") == 1
    # "Python PYTHON python" -> {p, y, t, h, o, n, ' '} = 7 distinct chars.
    assert count_distinct_characters("Python PYTHON python") == 7
