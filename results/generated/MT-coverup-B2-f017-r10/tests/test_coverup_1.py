# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

"""Tests for f017.parse_music covering all lines and branches.

parse_music is a pure function (no I/O, no global state, no side effects),
so no monkeypatching or teardown is required; each test is fully isolated
and leaves no state behind.
"""

from typing import List

from f017 import parse_music


def test_parse_music_all_note_types() -> None:
    """Covers line 6 (note_map creation) and line 7 with the `if x` branch
    taken True for every token."""
    result: List[int] = parse_music('o o| .|')
    assert result == [4, 2, 1]


def test_parse_music_single_note() -> None:
    """A single-token string exercises the loop with exactly one iteration."""
    assert parse_music('.|') == [1]
    assert parse_music('o|') == [2]
    assert parse_music('o') == [4]


def test_parse_music_empty_tokens_filtered() -> None:
    """Leading, trailing, and doubled spaces produce empty tokens after
    split(' '), exercising the `if x` branch taken False (the filter)."""
    result: List[int] = parse_music(' o  o| ')
    # split(' ') -> ['', 'o', '', 'o|', '']; empty tokens are skipped.
    assert result == [4, 2]


def test_parse_music_empty_string() -> None:
    """An empty string splits to [''], so only the False side of `if x` runs
    and the comprehension yields an empty list."""
    assert parse_music('') == []


def test_parse_music_repeated_notes() -> None:
    """Multiple occurrences of the same token map consistently."""
    assert parse_music('o o o') == [4, 4, 4]
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1]
