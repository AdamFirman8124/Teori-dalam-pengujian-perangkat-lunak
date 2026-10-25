# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters("a") == 1
    assert count_distinct_characters("A") == 1


def test_count_distinct_characters_case_insensitive():
    assert count_distinct_characters("Aa") == 1
    assert count_distinct_characters("AaBbCc") == 3
    assert count_distinct_characters("ABCabc") == 3


def test_count_distinct_characters_repeated_and_distinct():
    assert count_distinct_characters("aaaa") == 1
    assert count_distinct_characters("abc") == 3
    assert count_distinct_characters("aabbcc") == 3
    assert count_distinct_characters("Hello") == 4


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", 0),
        ("x", 1),
        ("xx", 1),
        ("xy", 2),
        ("a a", 2),
        ("a!a!", 2),
        ("Hello, World!", 10),
        ("Éé", 1),
        ("12321", 3),
    ],
)
def test_count_distinct_characters_parametrized(value, expected):
    result = count_distinct_characters(value)
    assert isinstance(result, int)
    assert result == expected
