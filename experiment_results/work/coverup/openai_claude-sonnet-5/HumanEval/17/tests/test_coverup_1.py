# file: script_17.py:4-18
# asked: {"lines": [17, 18], "branches": []}
# gained: {"lines": [17, 18], "branches": []}

import pytest
from script_17 import parse_music


def test_parse_music_empty_string():
    """Test that empty string returns empty list."""
    assert parse_music('') == []


def test_parse_music_single_whole_note():
    """Test parsing a single whole note."""
    assert parse_music('o') == [4]


def test_parse_music_single_half_note():
    """Test parsing a single half note."""
    assert parse_music('o|') == [2]


def test_parse_music_single_quarter_note():
    """Test parsing a single quarter note."""
    assert parse_music('.|') == [1]


def test_parse_music_multiple_notes():
    """Test parsing multiple notes."""
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


def test_parse_music_with_extra_spaces():
    """Test parsing with multiple spaces between notes."""
    assert parse_music('o  o|  .|') == [4, 2, 1]


def test_parse_music_all_note_types():
    """Test all note types are correctly mapped."""
    assert parse_music('o o| .|') == [4, 2, 1]
