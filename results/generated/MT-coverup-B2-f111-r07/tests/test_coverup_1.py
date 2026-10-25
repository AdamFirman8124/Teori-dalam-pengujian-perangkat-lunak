# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

from f111 import histogram


def test_histogram_returns_most_frequent_words():
    assert histogram("one two two three") == {"two": 2}


def test_histogram_returns_empty_dict_for_empty_or_space_only_input():
    assert histogram("") == {}
    assert histogram("   ") == {}


def test_histogram_returns_all_words_tied_for_highest_frequency():
    assert histogram("red blue red blue green") == {"red": 2, "blue": 2}
