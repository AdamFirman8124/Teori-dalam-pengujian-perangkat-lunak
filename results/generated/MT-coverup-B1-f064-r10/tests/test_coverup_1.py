# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

import pytest

from f064 import vowels_count


def test_vowels_count_basic():
    assert vowels_count("hello") == 2
    assert vowels_count("xyz") == 0
    assert vowels_count("AEIOU") == 5


def test_vowels_count_ends_with_y():
    assert vowels_count("happy") == 2
    assert vowels_count("ACROBATY") == 4
    assert vowels_count("y") == 1


def test_vowels_count_ends_with_uppercase_y():
    assert vowels_count("HAPPY") == 2
    assert vowels_count("Y") == 1


def test_vowels_count_does_not_end_with_y():
    assert vowels_count("sky high") == 1
    assert vowels_count("hello") == 2
