# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


@pytest.mark.parametrize(
    ("value", "characters", "expected"),
    [
        ("abcba", "x", ("abcba", True)),
        ("abc", "b", ("ac", False)),
        ("abca", "bc", ("aa", True)),
    ],
)
def test_reverse_delete_filters_characters_and_checks_palindrome(
    value, characters, expected
):
    result = reverse_delete(value, characters)

    assert result == expected
    assert result[0] == "".join(char for char in value if char not in characters)
    assert result[1] is (result[0] == result[0][::-1])
