# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f064 import vowels_count


def test_vowels_count_no_trailing_y():
    assert vowels_count("hello") == 2
    assert vowels_count("aeiouAEIOU") == 10
    assert vowels_count("bcdfg") == 0
    assert vowels_count("AbC") == 1


def test_vowels_count_trailing_lower_y():
    assert vowels_count("happy") == 2
    assert vowels_count("sky") == 1
    assert vowels_count("y") == 1


def test_vowels_count_trailing_upper_Y():
    assert vowels_count("HAPPY") == 2
    assert vowels_count("SKY") == 1
    assert vowels_count("Y") == 1


def test_vowels_count_mixed_vowels_and_y():
    assert vowels_count("aeiouy") == 6
    assert vowels_count("aeiouY") == 6
    assert vowels_count("AEIOU") == 5
