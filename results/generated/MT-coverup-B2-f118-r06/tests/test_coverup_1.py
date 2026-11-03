# file: project/f118/__init__.py:1-11
# asked: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 10, 11], "branches": [[3, 4], [3, 6], [7, 8], [7, 11], [8, 7], [8, 9], [9, 7], [9, 10]]}

import pytest

from f118 import get_closest_vowel


def test_word_shorter_than_three_returns_empty_string():
    """Covers lines 3-4: the len(word) < 3 early-return branch."""
    assert get_closest_vowel("") == ""
    assert get_closest_vowel("a") == ""
    assert get_closest_vowel("ab") == ""


def test_returns_vowel_flanked_by_consonants():
    """Covers lines 6-10: loop iteration, vowel hit, and the
    both-neighbours-are-consonants branch returning the vowel."""
    # 'i' at index 3 of "yogic" has 'g' before and 'c' after.
    assert get_closest_vowel("yogic") == "i"
    # Uppercase vowel 'U' at index 1 of "FULL" has 'F' before and 'L' after.
    assert get_closest_vowel("FULL") == "U"
    # Minimal-length word (len == 3) exercising the single loop step.
    assert get_closest_vowel("cat") == "a"
    # Closest (rightmost) qualifying vowel is picked, not the first one.
    assert get_closest_vowel("bEttEr") == "E"


def test_returns_empty_when_no_qualifying_vowel():
    """Covers line 11: loop exhausts without a match, including the
    line-9 false branch where a vowel is adjacent to another vowel."""
    # 'u' and 'i' in "quick" are both adjacent to other vowels.
    assert get_closest_vowel("quick") == ""
    # All characters are vowels, so no vowel has consonant neighbours.
    assert get_closest_vowel("aei") == ""
    # No vowels at all, so the loop body's inner branch is never taken.
    assert get_closest_vowel("bcdf") == ""
