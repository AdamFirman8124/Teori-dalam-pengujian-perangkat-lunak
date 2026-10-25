# file: project/f017/__init__.py:4-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest

from f017 import parse_music


@pytest.mark.parametrize(
    ("music_string", "expected"),
    [
        ("", []),
        ("o", [4]),
        ("o|", [2]),
        (".|", [1]),
        ("o o| .|", [4, 2, 1]),
        ("  o  o|  .|  ", [4, 2, 1]),
    ],
)
def test_parse_music(music_string: str, expected: list[int]) -> None:
    assert parse_music(music_string) == expected
