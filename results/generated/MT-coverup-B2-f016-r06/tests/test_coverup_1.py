# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_lowercase_only():
    assert count_distinct_characters("abcabc") == 3


def test_count_distinct_characters_mixed_case_is_case_insensitive():
    assert count_distinct_characters("AaBbCc") == 3


def test_count_distinct_characters_empty_string():
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters("z") == 1


def test_count_distinct_characters_with_spaces_and_punctuation():
    assert count_distinct_characters("Hello, World!") == 10


@pytest.mark.parametrize(
    "string, expected",
    [
        ("a", 1),
        ("aaaa", 1),
        ("ab", 2),
        ("ABC", 3),
        ("aA", 1),
        ("123123", 3),
        ("", 0),
    ],
)
def test_count_distinct_characters_parametrized(string, expected):
    result = count_distinct_characters(string)
    assert result == expected
    assert isinstance(result, int)
    assert 0 <= result <= len(string)
