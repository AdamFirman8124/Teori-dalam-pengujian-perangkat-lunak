# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

from f017 import parse_music


def test_parse_music_handles_notes_and_empty_segments():
    assert parse_music("o  o| .|") == [4, 2, 1]
    assert parse_music("") == []
