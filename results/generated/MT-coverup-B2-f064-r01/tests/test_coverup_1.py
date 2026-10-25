# file: project/f064/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[5, 6], [5, 7]]}

from f064 import vowels_count


def test_vowels_count_counts_vowels_without_y_adjustment():
    assert vowels_count("AEIOUxyz") == 5


def test_vowels_count_adds_one_for_terminal_lowercase_y():
    assert vowels_count("happy") == 2
