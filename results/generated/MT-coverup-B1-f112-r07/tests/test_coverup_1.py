# file: project/f112/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f112 import reverse_delete


@pytest.mark.parametrize(
    ("source", "characters", "expected"),
    [
        ("abcde", "ae", ("bcd", False)),
        ("abccba", "", ("abccba", True)),
        ("aabbcc", "ab", ("cc", True)),
    ],
)
def test_reverse_delete_filters_characters_and_reports_palindrome(
    source, characters, expected
):
    assert reverse_delete(source, characters) == expected
