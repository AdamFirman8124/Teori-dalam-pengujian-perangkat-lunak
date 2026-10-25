# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f017 import parse_music


def test_parse_music_executes_body():
    # Whole notes, half notes, quarter notes, and extra spaces (filtered by `if x`)
    result = parse_music('o o| .| o o| .| .| .| .| o o o')
    assert result == [4, 2, 1, 4, 2, 1, 1, 1, 1, 4, 4, 4]


def test_parse_music_empty_string():
    # Empty string: split(' ') yields [''], which is filtered out by `if x`
    assert parse_music('') == []


def test_parse_music_only_spaces():
    assert parse_music('   ') == []


def test_parse_music_single_note():
    assert parse_music('o|') == [2]
