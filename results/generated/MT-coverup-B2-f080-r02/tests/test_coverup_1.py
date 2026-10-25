# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


@pytest.mark.parametrize("value", ["", "a", "ab"])
def test_is_happy_rejects_values_shorter_than_three(value):
    assert is_happy(value) is False


@pytest.mark.parametrize("value", ["aab", "abb", "aba", "abcdc"])
def test_is_happy_rejects_repeated_characters_within_three_positions(value):
    assert is_happy(value) is False


@pytest.mark.parametrize("value", ["abc", "abcdef", "abca"])
def test_is_happy_accepts_values_without_repetition_in_any_three_character_window(value):
    assert is_happy(value) is True
