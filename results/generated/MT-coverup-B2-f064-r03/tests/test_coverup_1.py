# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f064 import vowels_count


def test_vowels_count_no_y_ending():
    """Covers lines 3-4, the False branch of the if on line 5, and line 7."""
    # No vowels at all, last char is neither 'y' nor 'Y'
    assert vowels_count("bcdfg") == 0
    # Mixed-case vowels, last char is neither 'y' nor 'Y'
    assert vowels_count("abcde") == 2
    assert vowels_count("AEIOU") == 5
    assert vowels_count("AbEcIdOfU") == 5
    # Empty vowel content but non-empty string
    assert vowels_count("xyz") == 0


def test_vowels_count_lowercase_y_ending():
    """Covers the True branch of `s[-1] == 'y'` (short-circuits the or)."""
    # 'a' is a vowel, plus the trailing-'y' bonus
    assert vowels_count("happy") == 2
    # 'y' itself is not in the vowel set; only the bonus applies
    assert vowels_count("y") == 1
    assert vowels_count("ACEDY") == 3  # A, E + bonus


def test_vowels_count_uppercase_y_ending():
    """Covers the True branch of `s[-1] == 'Y'` (second operand of the or)."""
    # First operand ('y' check) is False, second operand ('Y' check) is True
    assert vowels_count("HAPPY") == 2
    assert vowels_count("Y") == 1
    assert vowels_count("acedY") == 3  # a, e + bonus


def test_vowels_count_is_pure():
    """The function must not mutate its input or any module state."""
    s = "Happy"
    result = vowels_count(s)
    assert result == 2
    assert s == "Happy"  # input unchanged
    # Calling again yields the same result (no hidden state)
    assert vowels_count(s) == result
