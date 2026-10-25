# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f064 import vowels_count


def test_vowels_count_without_trailing_y():
    assert vowels_count("Hello") == 2


def test_vowels_count_with_trailing_lowercase_y():
    assert vowels_count("happy") == 2


def test_vowels_count_with_trailing_uppercase_y():
    assert vowels_count("DAY") == 2
