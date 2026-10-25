# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f017 import parse_music


def test_parse_music_empty_string():
    assert parse_music("") == []


def test_parse_music_single_whole_note():
    assert parse_music("o") == [4]


def test_parse_music_single_half_note():
    assert parse_music("o|") == [2]


def test_parse_music_single_quarter_note():
    assert parse_music(".|") == [1]


def test_parse_music_multiple_notes():
    assert parse_music("o o| .| o| o| .| .| .| .| o o") == [
        4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4,
    ]


def test_parse_music_skips_empty_tokens_from_extra_spaces():
    # Exercises the falsy branch of `if x` in the comprehension.
    assert parse_music("o  o|   .|") == [4, 2, 1]


def test_parse_music_leading_and_trailing_spaces():
    assert parse_music("  o| .|  ") == [2, 1]


def test_parse_music_whitespace_only():
    assert parse_music("   ") == []


def test_parse_music_returns_new_list_each_call():
    first = parse_music("o .|")
    second = parse_music("o .|")
    assert first == second == [4, 1]
    assert first is not second


def test_parse_music_invalid_note_raises_key_error():
    with pytest.raises(KeyError):
        parse_music("o x .|")
