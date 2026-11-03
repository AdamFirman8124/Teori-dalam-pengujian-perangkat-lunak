# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

"""Tests for f017.parse_music covering all previously missed lines (6-7) and branches.

parse_music is a pure function (no globals, no I/O, no mutable state), so no
monkeypatching/teardown is required; each test is fully self-contained.
"""

from f017 import parse_music


def test_parse_music_all_note_types():
    """Exercises line 6 (note_map construction) and line 7 (comprehension,
    'if x' True branch) with every note token."""
    assert parse_music('o o| .|') == [4, 2, 1]


def test_parse_music_single_tokens():
    """Each mapping key individually, covering all dict lookups on line 7."""
    assert parse_music('o') == [4]
    assert parse_music('o|') == [2]
    assert parse_music('.|') == [1]


def test_parse_music_skips_empty_tokens():
    """Covers the 'if x' False branch: consecutive, leading and trailing
    spaces produce empty tokens that must be filtered out."""
    assert parse_music('o  o|   .| ') == [4, 2, 1]
    assert parse_music(' o ') == [4]
    assert parse_music('o| .|  ') == [2, 1]


def test_parse_music_empty_string():
    """Empty input: split(' ') yields [''], the 'if x' False branch filters
    it out, and the comprehension yields an empty list."""
    assert parse_music('') == []


def test_parse_music_longer_sequence():
    """A longer mixed sequence to verify order and repeated lookups."""
    result = parse_music('o| o| .| .| .| .| .| .| o o')
    assert result == [2, 2, 1, 1, 1, 1, 1, 1, 4, 4]
    assert len(result) == 10


def test_parse_music_returns_new_list_each_call():
    """Postcondition: each call returns a fresh list (no shared state)."""
    first = parse_music('o o')
    second = parse_music('o o')
    assert first == second == [4, 4]
    assert first is not second
