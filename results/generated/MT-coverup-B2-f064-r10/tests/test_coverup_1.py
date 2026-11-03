# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f064 import vowels_count


def test_vowels_count_no_trailing_y_covers_false_branch():
    # Executes lines 3, 4, 5 (both conditions of the 'or' evaluate False) and 7.
    assert vowels_count("abcde") == 2
    assert vowels_count("AEIOU") == 5
    assert vowels_count("bcdfg") == 0
    assert vowels_count("xyz") == 0  # no vowels, and does not end with y/Y


def test_vowels_count_ends_with_lowercase_y():
    # Executes line 5 with s[-1] == 'y' True (short-circuits before checking 'Y'),
    # then line 6 increments, and line 7 returns.
    assert vowels_count("acy") == 2  # 'a' counts, trailing 'y' adds 1
    assert vowels_count("yy") == 1   # 'y' alone is not in the vowel set, only the bonus
    assert vowels_count("y") == 1


def test_vowels_count_ends_with_uppercase_y():
    # Executes line 5 where s[-1] == 'y' is False but s[-1] == 'Y' is True,
    # then line 6 increments, and line 7 returns.
    assert vowels_count("acY") == 2
    assert vowels_count("bY") == 1
    assert vowels_count("Y") == 1


def test_vowels_count_mixed_case_with_trailing_y():
    # Combines uppercase/lowercase vowel counting with the trailing-y bonus.
    assert vowels_count("AEIOUy") == 6
    assert vowels_count("aEiOuY") == 6
