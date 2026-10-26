# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f017 import parse_music


def test_parse_music_all_note_types():
    result = parse_music('o o| .|')
    assert result == [4, 2, 1]


def test_parse_music_empty_string():
    assert parse_music('') == []


def test_parse_music_multiple_spaces_ignored():
    assert parse_music('o  .|   o|') == [4, 1, 2]


def test_parse_music_single_note():
    assert parse_music('o|') == [2]
