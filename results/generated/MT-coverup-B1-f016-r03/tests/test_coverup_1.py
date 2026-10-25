# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1


def test_count_distinct_characters_all_distinct():
    assert count_distinct_characters("abc") == 3


def test_count_distinct_characters_repeated_characters():
    assert count_distinct_characters("aabbcc") == 3
    assert count_distinct_characters("aaa") == 1


def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("AaBbCc") == 3
    assert count_distinct_characters("Hello") == 4
    assert count_distinct_characters("ABCabc") == 3


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("a a", 2),
        ("123123", 3),
        ("!@!@", 2),
        ("Python", 6),
        ("Mississippi", 4),
    ],
)
def test_count_distinct_characters_parametrized(string, expected):
    assert count_distinct_characters(string) == expected
