# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f017 import parse_music


def test_parse_music_all_note_types():
    """Execute lines 6-7 with a string containing every note type."""
    result = parse_music('o o| .|')
    assert result == [4, 2, 1]


def test_parse_music_empty_string_hits_filter_branch():
    """Empty string exercises the 'if x' filter branch (falsy x)."""
    assert parse_music('') == []


def test_parse_music_extra_spaces_filtered_out():
    """Consecutive spaces produce empty tokens that are filtered out."""
    assert parse_music('o  o|   .| ') == [4, 2, 1]


def test_parse_music_single_note():
    assert parse_music('o|') == [2]


def test_parse_music_longer_sequence():
    music_string = 'o .| o| o .| .|'
    assert parse_music(music_string) == [4, 1, 2, 4, 1, 1]


def test_parse_music_unknown_note_raises_keyerror():
    """An unrecognized token should raise KeyError since note_map[x] is indexed."""
    with pytest.raises(KeyError):
        parse_music('x')
