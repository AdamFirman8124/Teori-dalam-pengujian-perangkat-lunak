# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

from f017 import parse_music


def test_parse_music_all_notes():
    """Covers lines 6-7: builds note_map and returns the parsed list."""
    result = parse_music('o o| .| o| o| .| .| .| o o')
    assert result == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]


def test_parse_music_empty_string():
    """Empty input yields an empty list (comprehension body never runs)."""
    assert parse_music('') == []


def test_parse_music_skips_empty_tokens():
    """Consecutive/leading/trailing spaces produce empty tokens,
    exercising the False branch of the `if x` filter."""
    assert parse_music('  o   .|  o| ') == [4, 1, 2]


def test_parse_music_single_note():
    """A single token exercises the True branch of the `if x` filter."""
    assert parse_music('o|') == [2]
