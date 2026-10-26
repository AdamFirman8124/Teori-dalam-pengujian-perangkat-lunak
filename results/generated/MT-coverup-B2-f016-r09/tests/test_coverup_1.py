# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f016 import count_distinct_characters


def test_count_distinct_characters_empty():
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1


def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("Aa") == 1
    assert count_distinct_characters("aAbBcC") == 3


def test_count_distinct_characters_distinct_and_repeated():
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("aaabbb") == 2


def test_count_distinct_characters_non_letters():
    assert count_distinct_characters("112233") == 3
    assert count_distinct_characters("a a") == 2
    assert count_distinct_characters("!@!@") == 2
