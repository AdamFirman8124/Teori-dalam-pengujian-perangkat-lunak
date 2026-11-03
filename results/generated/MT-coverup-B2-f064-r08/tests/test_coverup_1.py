# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f064 import vowels_count


def test_vowels_count_counts_vowels_no_y_ending():
    """Covers lines 3-4 and 7, and the branch where neither
    s[-1] == 'y' nor s[-1] == 'Y' is true (line 5 both False)."""
    assert vowels_count("abcde") == 2
    assert vowels_count("Alone") == 3
    assert vowels_count("xyz") == 0
    assert vowels_count("bYe") == 1  # 'Y' is not in the vowel set


def test_vowels_count_ends_with_lowercase_y():
    """Covers the branch where s[-1] == 'y' is True (short-circuits
    the 'or', so s[-1] == 'Y' is never evaluated) and line 6."""
    assert vowels_count("key") == 2  # 'e' plus trailing 'y'
    assert vowels_count("my") == 1  # no vowels, only the trailing 'y'


def test_vowels_count_ends_with_uppercase_y():
    """Covers the branch where s[-1] == 'y' is False but
    s[-1] == 'Y' is True, plus line 6."""
    assert vowels_count("keY") == 2  # 'e' plus trailing 'Y'
    assert vowels_count("ACEDY") == 3  # 'A', 'E' plus trailing 'Y'
    assert vowels_count("MY") == 1  # no vowels, only the trailing 'Y'


def test_vowels_count_mixed_case_vowels():
    """Exercises the membership test over the full vowel string
    (lines 3-4) with both lower- and upper-case vowels."""
    assert vowels_count("AEIOUaeiou") == 10
    assert vowels_count("bcdfg") == 0
