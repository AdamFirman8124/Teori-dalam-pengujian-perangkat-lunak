# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


@pytest.mark.parametrize(
    ("source", "chars", "expected"),
    [
        ("abcde", "a", ("bcde", False)),
        ("abcba", "", ("abcba", True)),
        ("abc", "abc", ("", True)),
    ],
)
def test_reverse_delete_filters_characters_and_checks_palindrome(
    source, chars, expected
):
    assert reverse_delete(source, chars) == expected


def test_reverse_delete_does_not_mutate_inputs():
    source = "abca"
    chars = "a"
    original_source = source
    original_chars = chars

    result = reverse_delete(source, chars)

    assert result == ("bc", False)
    assert source == original_source
    assert chars == original_chars
