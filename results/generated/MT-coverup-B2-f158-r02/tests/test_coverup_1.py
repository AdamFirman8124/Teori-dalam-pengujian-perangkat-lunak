# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        (["apple", "banana", "cherry"], "cherry"),
        (["abc", "bca", "cab"], "abc"),
        (["aaaa", "ab", "abc"], "abc"),
        (["z"], "z"),
    ],
)
def test_find_max(words, expected):
    original_words = words.copy()

    assert find_max(words) == expected
    assert words == original_words
