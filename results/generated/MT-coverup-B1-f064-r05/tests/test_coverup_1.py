# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f064 import vowels_count


def test_vowels_count_without_y_suffix():
    assert vowels_count("Apple") == 2


def test_vowels_count_with_lowercase_y_suffix():
    assert vowels_count("day") == 2


def test_vowels_count_with_uppercase_y_suffix():
    assert vowels_count("DAY") == 2
