# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", 0),
        ("a", 1),
        ("abcABC", 3),
        ("aA", 1),
        ("Hello, World!", 10),
        ("  ", 1),
        ("123123", 3),
        ("MiXeD CaSe", 9),
    ],
)
def test_count_distinct_characters_returns_expected_counts(string, expected):
    result = count_distinct_characters(string)

    assert result == expected
    assert result == len(set(string.lower()))
    assert isinstance(result, int)
    assert result >= 0
    assert result <= len(string)


def test_count_distinct_characters_is_case_insensitive():
    lower = count_distinct_characters("abcdef")
    upper = count_distinct_characters("ABCDEF")
    mixed = count_distinct_characters("aBcDeF")

    assert lower == upper == mixed == 6


def test_count_distinct_characters_does_not_mutate_input():
    original = "Some String"
    snapshot = str(original)

    result = count_distinct_characters(original)

    assert result == len(set(original.lower()))
    assert original == snapshot
    assert isinstance(original, str)
