# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f016 import count_distinct_characters


def test_empty_string():
    assert count_distinct_characters("") == 0


def test_all_same_character_case_insensitive():
    assert count_distinct_characters("aaaAAA") == 1


def test_hello_distinct_count():
    assert count_distinct_characters("hello") == 4


def test_case_insensitivity():
    assert count_distinct_characters("AaBbCc") == 3
    assert count_distinct_characters("ABCabc") == 3


def test_mixed_with_digits_and_symbols():
    assert count_distinct_characters("123!@#123") == 6


def test_single_character():
    assert count_distinct_characters("Z") == 1
    assert count_distinct_characters("z") == 1
