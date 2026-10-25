# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


@pytest.mark.parametrize(
    ("s", "c", "expected"),
    [
        ("abcba", "x", ("abcba", True)),
        ("abcxy", "xy", ("abc", False)),
    ],
)
def test_reverse_delete_filters_characters_and_checks_palindrome(s, c, expected):
    result = reverse_delete(s, c)

    assert result == expected
    assert isinstance(result, tuple)
    assert result[0] == "".join(char for char in s if char not in c)
    assert result[1] is (result[0][::-1] == result[0])
